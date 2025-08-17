import os
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QPushButton, QLabel, QListWidget, QSpinBox,
                             QProgressBar, QFileDialog, QMessageBox, QComboBox,
                             QGroupBox, QGridLayout, QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from worker import TimelapseWorker

class TimelapseGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_paths = []
        self.worker = None
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Timelapse Creator")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Title
        title = QLabel("Timelapse Creator")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Image selection section
        image_group = QGroupBox("Select Images")
        image_layout = QVBoxLayout(image_group)
        
        # Buttons for image operations
        button_layout = QHBoxLayout()
        self.add_images_btn = QPushButton("Add Images")
        self.clear_images_btn = QPushButton("Clear All")
        self.add_images_btn.clicked.connect(self.add_images)
        self.clear_images_btn.clicked.connect(self.clear_images)
        
        button_layout.addWidget(self.add_images_btn)
        button_layout.addWidget(self.clear_images_btn)
        button_layout.addStretch()
        
        image_layout.addLayout(button_layout)
        
        # Image list
        self.image_list = QListWidget()
        self.image_list.setMaximumHeight(150)
        image_layout.addWidget(self.image_list)
        
        layout.addWidget(image_group)
        
        # Settings section
        settings_group = QGroupBox("Timelapse Settings")
        settings_layout = QGridLayout(settings_group)
        
        # FPS setting
        settings_layout.addWidget(QLabel("Frames per Second:"), 0, 0)
        self.fps_spin = QSpinBox()
        self.fps_spin.setRange(1, 60)
        self.fps_spin.setValue(24)
        settings_layout.addWidget(self.fps_spin, 0, 1)
        
        # Resolution setting
        settings_layout.addWidget(QLabel("Resolution:"), 1, 0)
        self.resolution_combo = QComboBox()
        self.resolution_combo.addItems([
            "1920x1080 (Full HD)",
            "1280x720 (HD)",
            "3840x2160 (4K)",
            "Custom"
        ])
        settings_layout.addWidget(self.resolution_combo, 1, 1)
        
        # Custom resolution inputs (initially hidden)
        self.custom_width = QLineEdit()
        self.custom_height = QLineEdit()
        self.custom_width.setPlaceholderText("Width")
        self.custom_height.setPlaceholderText("Height")
        
        custom_layout = QHBoxLayout()
        self.custom_res_label = QLabel("Custom:")
        self.custom_res_x_label = QLabel("x")
        custom_layout.addWidget(self.custom_res_label)
        custom_layout.addWidget(self.custom_width)
        custom_layout.addWidget(self.custom_res_x_label)
        custom_layout.addWidget(self.custom_height)
        
        settings_layout.addLayout(custom_layout, 2, 0, 1, 2)
        
        # Hide custom resolution by default
        self.custom_width.setVisible(False)
        self.custom_height.setVisible(False)
        self.custom_res_label.setVisible(False)
        self.custom_res_x_label.setVisible(False)
        
        self.resolution_combo.currentTextChanged.connect(self.on_resolution_changed)
        
        layout.addWidget(settings_group)
        
        # Output section
        output_group = QGroupBox("Output")
        output_layout = QHBoxLayout(output_group)
        
        self.output_path_label = QLabel("No output file selected")
        self.browse_output_btn = QPushButton("Choose Output File")
        self.browse_output_btn.clicked.connect(self.choose_output_file)
        
        output_layout.addWidget(self.output_path_label)
        output_layout.addWidget(self.browse_output_btn)
        
        layout.addWidget(output_group)
        
        # Progress section
        progress_group = QGroupBox("Progress")
        progress_layout = QVBoxLayout(progress_group)
        
        self.status_label = QLabel("Ready")
        self.progress_bar = QProgressBar()
        
        progress_layout.addWidget(self.status_label)
        progress_layout.addWidget(self.progress_bar)
        
        layout.addWidget(progress_group)
        
        # Action buttons
        action_layout = QHBoxLayout()
        self.create_btn = QPushButton("Create Timelapse")
        self.create_btn.clicked.connect(self.create_timelapse)
        self.create_btn.setEnabled(False)
        
        action_layout.addStretch()
        action_layout.addWidget(self.create_btn)
        
        layout.addLayout(action_layout)
        
    def add_images(self):
        """Add images to the list"""
        files, _ = QFileDialog.getOpenFileNames(
            self, 
            "Select Images",
            "",
            "Image Files (*.jpg *.jpeg *.png *.bmp *.tiff *.tif)"
        )
        
        if files:
            for file_path in files:
                if file_path not in self.image_paths:
                    self.image_paths.append(file_path)
                    self.image_list.addItem(os.path.basename(file_path))
            
            self.update_ui_state()
            
    def clear_images(self):
        """Clear all images from the list"""
        self.image_paths.clear()
        self.image_list.clear()
        self.update_ui_state()
        
    def on_resolution_changed(self):
        """Handle resolution combo box change"""
        is_custom = self.resolution_combo.currentText() == "Custom"
        self.custom_width.setVisible(is_custom)
        self.custom_height.setVisible(is_custom)
        
        # Show/hide labels
        self.custom_res_label.setVisible(is_custom)
        self.custom_res_x_label.setVisible(is_custom)
        
    def choose_output_file(self):
        """Choose output file location"""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Timelapse As",
            "timelapse.mp4",
            "Video Files (*.mp4 *.avi *.mov)"
        )
        
        if file_path:
            self.output_path = file_path
            self.output_path_label.setText(os.path.basename(file_path))
            self.update_ui_state()
            
    def get_resolution(self):
        """Get the selected resolution as tuple"""
        resolution_text = self.resolution_combo.currentText()
        
        if resolution_text == "1920x1080 (Full HD)":
            return (1920, 1080)
        elif resolution_text == "1280x720 (HD)":
            return (1280, 720)
        elif resolution_text == "3840x2160 (4K)":
            return (3840, 2160)
        elif resolution_text == "Custom":
            try:
                width = int(self.custom_width.text())
                height = int(self.custom_height.text())
                return (width, height)
            except ValueError:
                return (1920, 1080)  # Default fallback
        
        return (1920, 1080)
        
    def update_ui_state(self):
        """Update UI state based on current selections"""
        has_images = len(self.image_paths) > 0
        has_output = hasattr(self, 'output_path') and bool(self.output_path)
        
        self.create_btn.setEnabled(has_images and has_output)
        
    def create_timelapse(self):
        """Start timelapse creation"""
        if not self.image_paths:
            QMessageBox.warning(self, "Warning", "Please select some images first.")
            return
            
        if not hasattr(self, 'output_path'):
            QMessageBox.warning(self, "Warning", "Please choose an output file.")
            return
            
        # Sort images by filename (assuming they have sequential names)
        self.image_paths.sort()
        
        # Get settings
        fps = self.fps_spin.value()
        resolution = self.get_resolution()
        
        # Create and start worker thread
        self.worker = TimelapseWorker(self.image_paths, self.output_path, fps, resolution)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.status.connect(self.status_label.setText)
        self.worker.finished.connect(self.on_timelapse_finished)
        
        # Disable UI during processing
        self.create_btn.setEnabled(False)
        self.add_images_btn.setEnabled(False)
        
        self.worker.start()
        
    def on_timelapse_finished(self, success, message):
        """Handle timelapse creation completion"""
        # Re-enable UI
        self.create_btn.setEnabled(True)
        self.add_images_btn.setEnabled(True)
        
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.critical(self, "Error", message)
            
        self.progress_bar.setValue(0)
        self.status_label.setText("Ready")
