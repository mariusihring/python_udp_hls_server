from flask import Flask, send_from_directory
from flask_cors import CORS
import subprocess
import threading

# Function to start the subprocess
def start_ffmpeg():

# source = "rtsp://10.3.141.1:8554/stream"
    source = "rtsp://rtspstream:e08e1f1629e05280f3441da63fe80eaf@zephyr.rtsp.stream/movie"
    command = [
    "ffmpeg",
    "-rtsp_transport", "udp",
    "-i", source,
    "-c:v", "h264",
    "-preset", "ultrafast",
    "-b:v", "2000k",
    "-g", "48",
    "-hls_time", "1",
    "-hls_list_size", "6",
    "-start_number", "1",
    "-hls_flags", "delete_segments",
    "stream.m3u8"
]
    subprocess.run(command)

# Directory where the ffmpeg output files are
OUTPUT_DIR = '.'

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(OUTPUT_DIR, path)

if __name__ == '__main__':
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=app.run, kwargs={'port': 8001})
    flask_thread.start()

    # Start the subprocess in the main thread
    start_ffmpeg()
