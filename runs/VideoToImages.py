import cv2
import os
import sys

def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the frames and save them as images
    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    cap.release()

if __name__ == "__main__":
    # Replace 'input_video.mp4' with the path to your video file
    video_path = "/Users/jayasakthibalajig/Sakthi/Traffic/TrafficManagement/runs/detect/predict2/traffic_mumbai.mp4"
    
    # Replace 'output_frames' with the desired output folder
    output_folder = "/Users/jayasakthibalajig/Sakthi/Traffic/TrafficManagement/runs/Pics"

    extract_frames(video_path, output_folder)
