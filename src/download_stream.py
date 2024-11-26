import subprocess
import os

def get_stream_url(video_url):
    """Use yt-dlp to get the direct stream URL."""
    result = subprocess.run(
        ["yt-dlp", "-g", video_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to get stream URL: {result.stderr.decode()}")
    return result.stdout.decode().strip()

def download_stream(video_url, output_path="data/video.mp4"):
    """Download or stream a YouTube video."""
    try:
        stream_url = get_stream_url(video_url)
        print(f"Streaming from URL: {stream_url}")
        
        # Use ffmpeg to process the stream
        subprocess.run(
            ["ffmpeg", "-i", stream_url, "-c", "copy", output_path],
            check=True
        )
        print(f"Video saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=example"  # Replace with your video URL
    os.makedirs("data", exist_ok=True)
    download_stream(video_url)
