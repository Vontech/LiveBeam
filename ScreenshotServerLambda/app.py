import cv2
import streamlink
import subprocess
import datetime
import numpy as np
import logging
import os
import io

logging.basicConfig(level=logging.INFO)

def capture_screenshot(stream_url: str, identifier: str) -> np.array:
    streams = streamlink.streams(stream_url)
    url = streams['best'].url
    cap = cv2.VideoCapture(url)
    success, img_bgr = cap.read()
    retval, buffer = cv2.imencode('.png', img_bgr)
    return buffer

from subprocess import Popen, PIPE, STDOUT
import os
import threading
import time

def log_subprocess_output(pipe):
    for line in iter(pipe.readline, b''): # b'\n'-separated lines
        print(line)
    pipe.close()
    
def get_file_size(path):
    if not os.path.exists(path):
        return None
    size_bytes = os.stat(path).st_size
    return size_bytes/(1024**2)
        
def kill_process_when_size_reached(process, path, size_mb):
    while True:
        file_size = get_file_size(path)
        if file_size is not None and file_size >= size_mb:
            process.kill()
            break
        time.sleep(0.1)

MAX_SIZE = 3
def get_twitch_screenshot(token: str, user: str) -> np.array:
    timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    
    # First, download some raw video from the stream
    filename_orig = '{}-{}.rawvideo'.format(user, timestamp)
    command = [
        'streamlink', 
        '--twitch-disable-reruns', 
        '--twitch-disable-ads',
        '--twitch-disable-hosting',
        '--twitch-low-latency',
        'https://twitch.tv/{}'.format(user),
        'best',
        '-o',
        filename_orig
    ]
    #print(' '.join(command))
    process = Popen(command, stdout=PIPE, stderr=STDOUT)
    process_watcher = threading.Thread(target=kill_process_when_size_reached, args=(process, filename_orig, MAX_SIZE))
    process_watcher.start()
    exitcode = process.wait() # 0 means success
    process_watcher.join()
    
    # Next, extract a frame using ffmpeg
    output_image_path = '{}-{}.jpg'.format(user, timestamp)
    command = [
        'ffmpeg',
        '-ss',
        '00:00:00',
        '-i', filename_orig,
        '-vframes', '1', '-q:v', '1',
        output_image_path
    ]
    process = Popen(command, stdout=PIPE, stderr=STDOUT)
    exitcode = process.wait() # 0 means success
    
    # Remove the original video file
    os.remove(filename_orig)
    
    return output_image_path

OAUTH_TOKEN = "5w18kn21v8saevz2egvcspvy2pqjvt"
USER = "tsm_imperialhal"#"nokokopuffs"#

print(os.listdir('/usr/local/bin'))
import sysconfig
print(sysconfig.get_path('purelib'))
def handler(event, context):
    return twitch_screenshot(event.get('username'))

def twitch_screenshot(username):
    logging.info("Capturing Twitch.tv screenshot for " + username)
    stream = 'http://twitch.tv/' + username
    path = get_twitch_screenshot(OAUTH_TOKEN, username)
    print(path)
    return path
    # img = capture_screenshot(stream, username)
    # return send_file(io.BytesIO(img), mimetype='image/png')
