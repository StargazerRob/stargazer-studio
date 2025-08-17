import subprocess
from pathlib import Path
from PyQt5.QtCore import QThread, pyqtSignal
import cv2

class TimelapseWorker(QThread):
    """Worker thread for processing images and creating timelapse"""
    progress = pyqtSignal(int)
    status = pyqtSignal(str)
    finished = pyqtSignal(bool, str)
    
    def __init__(self, image_paths, output_path, fps, resolution):
        super().__init__()
        self.image_paths = image_paths
        self.output_path = output_path
        self.fps = fps
        self.resolution = resolution
        
    def run(self):
        try:
            self.status.emit("Processing images...")
            temp_dir = Path("temp_timelapse")
            temp_dir.mkdir(exist_ok=True)
            
            # Process and resize images
            total_images = len(self.image_paths)
            for i, img_path in enumerate(self.image_paths):
                # Load and resize image
                img = cv2.imread(str(img_path))
                if img is None:
                    continue
                    
                # Resize to target resolution
                img_resized = cv2.resize(img, self.resolution)
                
                # Save with sequential naming
                temp_path = temp_dir / f"frame_{i:06d}.jpg"
                cv2.imwrite(str(temp_path), img_resized)
                
                progress = int((i + 1) / total_images * 50)  # First 50% for processing
                self.progress.emit(progress)
            
            self.status.emit("Creating video...")
            self.progress.emit(50) # Mark image processing as complete
            
            # Use FFmpeg to create video
            ffmpeg_cmd = [
                'ffmpeg', '-y',  # -y to overwrite output file
                '-framerate', str(self.fps),
                '-i', str(temp_dir / 'frame_%06d.jpg'),
                '-c:v', 'libx264',
                '-pix_fmt', 'yuv420p',
                '-crf', '18',  # High quality
                str(self.output_path)
            ]
            
            process = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
            
            if process.returncode == 0:
                self.progress.emit(100)
                self.status.emit("Timelapse created successfully!")
                self.finished.emit(True, "Video created successfully!")
            else:
                self.finished.emit(False, f"FFmpeg error: {process.stderr}")
                
            # Cleanup temp files
            for temp_file in temp_dir.glob("*.jpg"):
                temp_file.unlink()
            temp_dir.rmdir()
            
        except Exception as e:
            self.finished.emit(False, f"Error: {str(e)}")
