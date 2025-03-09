import os
import subprocess
import time
from datetime import datetime
from tkinter import Tk, Button, Label, filedialog

def take_screenshot():
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    output_path = os.path.join(os.getcwd(), filename)
    
    command = ["idevicescreenshot", output_path]
    subprocess.run(command)
    
    status_label.config(text=f"Screenshot saved: {output_path}")

def start_recording():
    global recording_process, recording_filename
    recording_filename = f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    output_path = os.path.join(os.getcwd(), recording_filename)
    
    command = ["ffmpeg", "-f", "avfoundation", "-i", "iPhone", "-r", "30", output_path]
    recording_process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    status_label.config(text="Recording started...")

def stop_recording():
    global recording_process
    if recording_process:
        recording_process.terminate()
        status_label.config(text=f"Recording saved: {recording_filename}")
        recording_process = None

# GUI Setup
root = Tk()
root.title("iPhone Screen Capture")
root.geometry("300x200")

status_label = Label(root, text="Connect your iPhone via USB", wraplength=250)
status_label.pack(pady=10)

screenshot_button = Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=5)

record_button = Button(root, text="Start Recording", command=start_recording)
record_button.pack(pady=5)

stop_button = Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=5)

root.mainloop()

