import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import yt_dlp as youtube_dl

def download_youtube_video(url):
    ydl_opts = {
        'format': 'best',  # Select the best available format
        'outtmpl': '%(title)s.%(ext)s'  # Save the file with its title and correct extension
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = ydl.prepare_filename(info_dict)  # Get the file name of the downloaded video
        return video_title

# Load the YOLO model
model = YOLO("yolov8s.pt")

# Initialize DeepSORT
deepsort = DeepSort()
youtube_video_url = 'https://www.youtube.com/watch?v=1YqVEVbXQ1c'
#print("Downloading video...")
video_path = download_youtube_video(youtube_video_url)
# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Couldn't open video file.")
    exit()

frame_skip = 25  # Skip every 25 frames
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if count % frame_skip != 0:
        count += 1
        continue

    # Resize frame for faster processing
    frame_resized = cv2.resize(frame, (640, 480))

    # Perform detection
    results = model(frame_resized, classes=0)  # Detect only persons (class ID 0)

    # Extract bounding boxes and confidences
    boxes = results[0].boxes.xyxy.numpy()  # Bounding boxes in (x1, y1, x2, y2)
    confidences = results[0].boxes.conf.numpy()  # Confidence scores

    # Prepare detections for DeepSORT
    detections = [(box.tolist(), conf) for box, conf in zip(boxes, confidences) if conf > 0.5]

    # Update DeepSORT tracker
    tracks = deepsort.update_tracks(detections, frame=frame_resized)

    # Draw results on the frame
    for track in tracks:
        if track.is_confirmed() and track.time_since_update < 1:
            x1, y1, x2, y2 = map(int, track.to_tlbr())
            track_id = track.track_id
            cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame_resized, f'ID: {track_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Resize back to original size for display
    annotated_frame_resized = cv2.resize(frame_resized, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_LINEAR)

    # Display the frame
    cv2.imshow('Detection and Tracking', annotated_frame_resized)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    count += 1

cap.release()
cv2.destroyAllWindows()
