import cv2

def extract_frames(video_path, output_dir, frame_interval=30):
    """Extract frames from a video."""
    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0
    saved_count = 0

    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            output_file = f"{output_dir}/frame_{saved_count:04d}.jpg"
            cv2.imwrite(output_file, frame)
            saved_count += 1
        frame_count += 1

    video_capture.release()
    print(f"Extracted {saved_count} frames to {output_dir}.")

if __name__ == "__main__":
    extract_frames("data/video.mp4", "data/frames")
