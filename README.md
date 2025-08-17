# Timelapse Creator

Yes I did vibe code this, and also yes I have no idea what I'm doing.

It's meant to be a GUI application for creating star timelapse videos from a sequence of still images on Linux.

## Description

The intention for this project is to make a small tool for making timelapses out of photos because using a full video editor felt like a faff.

## Features

* Simple and intuitive interface for creating timelapses.
* Add multiple images from your computer.
*  Customizable Settings
    *   Set the output video's Frames Per Second (FPS).
    *   Choose from standard resolutions (e.g., 1080p, 720p, 4K) or define a custom resolution.
*  A separate thread for video processing keeps the UI from freezing.
*  A progress bar and status messages show the current status of the timelapse creation.

## Future functionality 

Some things I'm thinking about adding:

* Addition of frames to make star trail timelapses
* Boomerang timelapse creation (video goes foward to the end, and then reverses, and goes back to the start)

## Requirements

*   Python 3
*   PyQt5
*   OpenCV (for Python)
*   Pillow
*   FFmpeg

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/TimelapseTool.git
    cd TimelapseTool
    ```

2.  Virtual environment - n.b the run.sh starts a venv at launch
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install the required Python libraries in the venv:

    ```bash
    pip install PyQt5 opencv-python-headless pillow
    ```

4.  Install FFmpeg:
    You need to install FFmpeg on your system if you don't have it already. You can download it from the [official FFmpeg website](https://ffmpeg.org/download.html) or install it using a package manager. I tried experimenting with including FFMpeg in the project, it was very far beyond me!! 

## Usage

1.  Run the application:
    ./run.sh

2.  Add images:Click the "Add Images" button to select the images you want to include in your timelapse.

3.  Choose settings:
    *   Set the desired FPS.
    *   Select a resolution from the dropdown or choose "Custom" to enter a custom resolution.

4.  Select output file: Click the "Choose Output File" button to specify the name and location of the output video.

5.  Create the timelapse:Click the "Create Timelapse" button to start the process.

