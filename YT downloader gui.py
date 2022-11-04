import tkinter as tk
import os
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from pytube import YouTube
import ffmpeg
from pytube.exceptions import RegexMatchError
from tkinter import messagebox


def get_video_with_audio():
    try:
        i = entry_link.get()
        youtube = YouTube(i)
        video1 = youtube.streams.get_highest_resolution()
        video1.download(filename="v1")
        destination = asksaveasfilename(initialfile=youtube.title, defaultextension=".mp4", title="Zapisz jako:")
        source = "v1"
        os.replace(source, destination)
        messagebox.showinfo("YT downloader", "Pobrano!")
    except FileNotFoundError:
        messagebox.showinfo("YT downloader", "Pobieranie przerwane!")
        os.remove("v1")
    except RegexMatchError:
        messagebox.showinfo("YT downloader", "Nieprawidłowy link!")
        entry_link.delete(0, tk.END)
        pass


def get_video_only_1080():
    try:
        i = entry_link.get()
        youtube = YouTube(i)
        video = youtube.streams.filter(res="1080p", progressive=False).first()
        video.download(filename="v2")
        destination = asksaveasfilename(initialfile=youtube.title, defaultextension=".mp4", title="Zapisz jako:")
        source = "v2"
        os.replace(source, destination)
        messagebox.showinfo("YT downloader", "Pobrano!")
    except FileNotFoundError:
        messagebox.showinfo("YT downloader", "Pobieranie przerwane!")
        os.remove("v2")
    except AttributeError:
        messagebox.showinfo("YT downloader", "Nie ma wybranej rozdzielczości dla tego filmu.")
        pass
    except RegexMatchError:
        messagebox.showinfo("YT downloader", "Nieprawidłowy link!")
        entry_link.delete(0, tk.END)
        pass


def get_video_only_1440():
    try:
        i = entry_link.get()
        youtube = YouTube(i)
        video = youtube.streams.filter(res="1440p", progressive=False).first()
        video.download(filename="v2")
        destination = asksaveasfilename(initialfile=youtube.title, defaultextension=".mp4", title="Zapisz jako:")
        source = "v2"
        os.replace(source, destination)
        messagebox.showinfo("YT downloader", "Pobrano!")
    except FileNotFoundError:
        messagebox.showinfo("YT downloader", "Pobieranie przerwane!")
        os.remove("v2")
    except AttributeError:
        messagebox.showinfo("YT downloader", "Nie ma wybranej rozdzielczości dla tego filmu.")
        pass
    except RegexMatchError:
        messagebox.showinfo("YT downloader", "Nieprawidłowy link!")
        entry_link.delete(0, tk.END)
        pass


def get_video_only_2160():
    try:
        i = entry_link.get()
        youtube = YouTube(i)
        video = youtube.streams.filter(res="2160p", progressive=False).first()
        video.download(filename="v2")
        destination = asksaveasfilename(initialfile=youtube.title, defaultextension=".mp4", title="Zapisz jako:")
        source = "v2"
        os.replace(source, destination)
        messagebox.showinfo("YT downloader", "Pobrano!")
    except FileNotFoundError:
        messagebox.showinfo("YT downloader", "Pobieranie przerwane!")
        os.remove("v2")
    except AttributeError:
        messagebox.showinfo("YT downloader", "Nie ma wybranej rozdzielczości dla tego filmu.")
        pass
    except RegexMatchError:
        messagebox.showinfo("YT downloader", "Nieprawidłowy link!")
        entry_link.delete(0, tk.END)
        pass


def get_only_audio():
    try:
        i = entry_link.get()
        youtube = YouTube(i)
        audio = youtube.streams.filter(abr="160kbps", progressive=False).first()
        audio.download(filename="a1")
        destination = asksaveasfilename(defaultextension='.mp3', initialfile=youtube.title, title="Zapisz jako:")
        source = "a1"
        os.replace(source, destination)
        messagebox.showinfo("YT downloader", "Pobrano!")
    except FileNotFoundError:
        messagebox.showinfo("YT downloader", "Pobieranie przerwane!")
        os.remove("a1")
    except RegexMatchError:
        messagebox.showinfo("YT downloader", "Nieprawidłowy link!")
        entry_link.delete(0, tk.END)
        pass


def merge_files():
    messagebox.showinfo("YT downloader", 'Po kliknięciu "ok" i wybraniu plików nastąpi ich łączenie,'
                                         ' \nmoże to potrwać dłuższą chwilę!')
    video = ffmpeg.input(askopenfilename(title="Wybierz plik wideo:"))
    audio = ffmpeg.input(askopenfilename(title="Wybierz plik audio:"))
    destination = asksaveasfilename(
        title="Wybierz miejsce zapisu:", defaultextension='.mp4', initialfile="merged_video.mp4")
    ffmpeg.output(audio, video, "finished_video.mp4").run(overwrite_output=True)
    source = "finished_video.mp4"
    os.replace(source, destination)
    messagebox.showinfo("YT downloader", "Połączono!")


root = tk.Tk()
root.geometry("330x330")
root.resizable(False, False)
root.title("YT downloader")

label = tk.Label(root, text="Wklej link:")
label.pack(fill=tk.BOTH)
entry_link = tk.Entry(root, width=50, justify="left")
entry_link.pack(pady=10)

button = tk.Button(root, text="Pobierz wideo z audio (720p)", width=22, height=1, command=get_video_with_audio)
button.pack(pady=5)

button2 = tk.Button(text="Pobierz wideo: 1080p", width=22, height=1, command=get_video_only_1080)
button2.pack(pady=5)

button3 = tk.Button(text="Pobierz wideo: 1440p", width=22, height=1, command=get_video_only_1440)
button3.pack(pady=5)

button4 = tk.Button(text="Pobierz wideo: 2160p", width=22, height=1, command=get_video_only_2160)
button4.pack(pady=5)

button5 = tk.Button(text="Pobierz audio", width=22, height=1, command=get_only_audio)
button5.pack(pady=5)

button6 = tk.Button(text="Połącz wideo i audio", width=22, height=1, command=merge_files)
button6.pack(pady=5)

button7 = tk.Button(text="Wyjdź", width=22, height=1, command=root.destroy)
button7.pack(pady=5)

root.mainloop()
