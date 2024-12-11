# Imports
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube
import subprocess

# Functions
def download_with_ytdlp(url, save_path, options):
    try:
        command = ['yt-dlp', '-o', f'{save_path}/%(title)s.%(ext)s'] + options + [url]
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Download completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def high_quality_download():
    url = myentry.get()
    if not url.startswith("https://www.youtube.com/"):
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return
    save_path = filedialog.askdirectory(title="Select Download Folder")
    if not save_path:
        messagebox.showinfo("Cancelled", "Download cancelled")
        return
    download_with_ytdlp(url, save_path, ['-f', 'best'])

def low_quality_download():
    url = myentry.get()
    if not url.startswith("https://www.youtube.com/"):
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return
    save_path = filedialog.askdirectory(title="Select Download Folder")
    if not save_path:
        messagebox.showinfo("Cancelled", "Download cancelled")
        return
    download_with_ytdlp(url, save_path, ['-f', 'worst'])

def audio_download():
    url = myentry.get()
    if not url.startswith("https://www.youtube.com/"):
        messagebox.showerror("Error", "Please enter a valid YouTube URL")
        return
    save_path = filedialog.askdirectory(title="Select Download Folder")
    if not save_path:
        messagebox.showinfo("Cancelled", "Download cancelled")
        return
    download_with_ytdlp(url, save_path, ['-f', 'bestaudio', '--extract-audio', '--audio-format', 'mp3'])

# GUI
root = Tk()
root.geometry("500x300")
root.title("YouTube Downloader")
root.resizable(False, False)

# Label
mylabel = Label(root, text="Enter the video link", font=("Arial", 12))
mylabel.pack(pady=10)

# Entry field
myentry = ttk.Entry(root, width=50, font=("Arial", 12))
myentry.pack(pady=10)

# Buttons
button1 = ttk.Button(root, text="High quality download", command=high_quality_download)
button1.place(x=100, y=100)

# Low Quality Button at bottom-left
button2 = ttk.Button(root, text="Low quality download", command=low_quality_download)
button2.place(x=250, y=100)  # Bottom-left corner

# Audio Only Button at bottom-right
button3 = ttk.Button(root, text="Only audio", command=audio_download)
button3.place(x=200, y=140)  # Bottom-right corner

# Make the app last forever until you close it
root.mainloop()