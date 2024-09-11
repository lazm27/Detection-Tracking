This project implements an optimized inference pipeline that can process long-duration videos to identify and track persons of interest, specifically distinguishing between children and therapists. The pipeline utilizes YOLOv8 for object detection and DeepSORT for tracking, providing real-time visualization of bounding boxes and unique IDs for detected individuals.

Features
Optimized Inference Pipeline: Efficiently processes long-duration videos to identify and track people.
Bounding Box Predictions: Accurately detects and displays bounding boxes for children and therapists.
Unique ID Assignment: Each detected person is assigned a unique ID for continuous tracking across frames.
Real-Time Visualization: The predictions are plotted and displayed in real-time, facilitating immediate feedback and analysis.
Requirements
Python 3.8+
Libraries:
OpenCV
ultralytics
deep_sort_realtime
yt-dlp
Setup
Clone the Repository

If you haven’t already cloned the repository, you can do so with:

sh
Copy code
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
Install Required Libraries

Install the required Python libraries using the provided requirements.txt file:

sh
Copy code
pip install -r requirements.txt
Download YOLOv8 Model

Ensure you have the YOLOv8 model file (yolov8s.pt). Place this file in the same directory as your script.

Download Video from YouTube

The script can download a YouTube video automatically. Ensure you have the yt-dlp library installed.

Usage
Modify YouTube Video URL

Open the predict.py script and locate the following line:

python
Copy code
youtube_video_url = 'https://www.youtube.com/watch?v=1YqVEVbXQ1c'
Replace 'https://www.youtube.com/watch?v=1YqVEVbXQ1c' with the URL of the YouTube video you want to process.

Run the Script

You can run the script directly using Python:

sh
Copy code
python predict.py
Interact with the Output

The video will be displayed with bounding boxes and tracking IDs. Press 'q' to quit the video window.

Code Explanation
Imports and Setup

The script imports necessary libraries, sets up the YOLOv8 model, initializes DeepSORT, and defines a function to download YouTube videos.

Video Processing

The script opens the video file, performs detection and tracking on each frame, and displays the results. YOLOv8 detects people, and DeepSORT tracks them across frames, maintaining unique IDs for each person.

Detection and Tracking

YOLOv8 is used for object detection to identify people in the video frames. DeepSORT is then used to track these detections across frames, maintaining unique IDs for each person.

Troubleshooting
ModuleNotFoundError: Ensure all required libraries are installed. Use pip to install missing modules.
Video File Issues: Ensure the video file is properly downloaded and in the correct format.
Model File: Ensure the YOLOv8 model file (yolov8s.pt) is correctly placed in the working directory.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
YOLOv8
DeepSORT
yt-dlp
