# Timelapse Creator

A simple GUI application for creating timelapse videos from a sequence of still images.

## Description

The intention with this project is to make a small, relatively simple tool for making timelapses out of photos. Using a full video editor for doing this was a bit of a faff in my experience.

My own personal work flow is batch processing raw images in Darktable, and then exporting, the idea is that this tool would then do the next step, so I don't foresee image editing being part of this really.

## Features

*   **Easy-to-use GUI:** Simple and intuitive interface for creating timelapses.
*   **Image Selection:** Add multiple images from your computer.
*   **Customizable Settings:**
    *   Set the output video's Frames Per Second (FPS).
    *   Choose from standard resolutions (e.g., 1080p, 720p, 4K) or define a custom resolution.
*   **Responsive UI:** A separate thread for video processing keeps the UI from freezing.
*   **Progress Tracking:** A progress bar and status messages show the current status of the timelapse creation.

## Future functionality 

Some things I'm thinking about adding:

* Addition of frames to make a star trail image (and ability to save increments to make star trail timelapse
* boomerang timelapse creation (video goes foward to the end, and then reverses, and goes back to the start)
* 

## Requirements

*   Python 3
*   PyQt5
*   OpenCV (for Python)
*   Pillow
*   FFmpeg

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/TimelapseTool.git
    cd TimelapseTool
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required Python libraries:**
    ```bash
    pip install PyQt5 opencv-python-headless pillow
    ```

4.  **Install FFmpeg:**
    You need to install FFmpeg on your system. You can download it from the [official FFmpeg website](https://ffmpeg.org/download.html) or install it using a package manager.

    *   **On Debian/Ubuntu:**
        ```bash
        sudo apt update
        sudo apt install ffmpeg
        ```
    *   **On macOS (using Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    *   **On Windows:**
        Download the binaries from the [FFmpeg website](https://ffmpeg.org/download.html) and add the `bin` directory to your system's PATH.

## Usage

1.  **Run the application:**
    ```bash
    python3 timelapse_gui.py
    ```

2.  **Add images:** Click the "Add Images" button to select the images you want to include in your timelapse.

3.  **Choose settings:**
    *   Set the desired FPS.
    *   Select a resolution from the dropdown or choose "Custom" to enter a custom resolution.

4.  **Select output file:** Click the "Choose Output File" button to specify the name and location of the output video.

5.  **Create the timelapse:** Click the "Create Timelapse" button to start the process.

