import os
import re
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from pytube import YouTube
import ffmpeg
import cowsay
from pytube.exceptions import RegexMatchError


def show_info(s):
    youtube = YouTube(s)
    print()
    print("Tytuł:", youtube.title)
    print("Autor:", youtube.author)
    print("Data opublikowania:", youtube.publish_date.strftime("%d-%m-%Y"))
    print("Długość:", youtube.length, "sekund")
    print("Pobrano!")


def get_video_with_audio(i):
    youtube = YouTube(i)
    print("Pobieranie..")
    video1 = youtube.streams.get_highest_resolution()
    video1.download(filename="v1")
    destination = asksaveasfilename(initialfile=youtube.title, defaultextension=".mp4", title="Zapisz jako:")
    source = "v1"
    os.replace(source, destination)


def get_video_only(v, resolution):
    youtube = YouTube(v)
    print("Pobieranie..")
    video = youtube.streams.filter(res=resolution, progressive=False).first()
    video.download(filename="v2")
    destination = asksaveasfilename(initialfile=youtube.title, defaultextension=".mp4", title="Zapisz jako:")
    source = "v2"
    os.replace(source, destination)


def get_only_audio(a):
    youtube = YouTube(a)
    print("Pobieranie..")
    audio = youtube.streams.filter(abr="160kbps", progressive=False).first()
    audio.download(filename="a1")
    destination = asksaveasfilename(defaultextension='.mp3', initialfile=youtube.title, title="Zapisz jako:")
    source = "a1"
    os.replace(source, destination)


def restart():
    while True:
        try:
            print()
            i = input("Czy chcesz zrobić coś jeszcze? (t/n) ")
            if i == "t" or i == "T":
                print()
                main()
            if i == "n" or i == "N":
                quit()
        except ValueError:
            continue


def main():
    while True:
        try:
            print("[1] Pobierz wideo z audio (720p).")
            print("[2] Pobierz wideo.")
            print("[3] Pobierz audio.")
            print("[4] Połącz wideo i audio.")
            print("[5] Wyjdź.")
            user_choice = int(input("Wybierz opcję: "))
            if user_choice == 1:
                while True:
                    try:
                        user_input = input("Wklej link: ")
                        if re.search(r"youtube.com", user_input):
                            get_video_with_audio(user_input)
                            show_info(user_input)
                            restart()
                        else:
                            print("Podaj prawidłowy link.")
                            continue
                    except FileNotFoundError:
                        os.remove("v1")
                        print("Pobieranie przerwane.")
                        print()
                    except RegexMatchError:
                        print("Nieprawidłowy link.")
                        print()
                    break
            if user_choice == 2:
                while True:
                    try:
                        print("[1] 1080p")
                        print("[2] 1440p")
                        print("[3] 2160p")
                        print("[4] Wróć")
                        user_choice = int(input("Wybierz opcję: "))
                    except ValueError:
                        print("Wybierz opcję od 1-4.")
                        print()
                        continue
                    if user_choice == 1:
                        while True:
                            try:
                                user_input = input("Wklej link: ")
                                if re.search(r"youtube.com", user_input):
                                    get_video_only(user_input, "1080p")
                                    show_info(user_input)
                                    restart()
                                else:
                                    print("Podaj prawidłowy link.")
                                    continue
                            except FileNotFoundError:
                                os.remove("v2")
                                print("Pobieranie przerwane.")
                                print()
                            except AttributeError:
                                print("Nie ma wybranej rozdzielczości dla tego filmu.")
                                print()
                            except RegexMatchError:
                                print("Nieprawidłowy link.")
                                print()
                            break
                    if user_choice == 2:
                        while True:
                            try:
                                user_input = input("Wklej link: ")
                                if re.search(r"youtube.com", user_input):
                                    get_video_only(user_input, "1440p")
                                    show_info(user_input)
                                    restart()
                                else:
                                    print("Podaj prawidłowy link.")
                                    continue
                            except FileNotFoundError:
                                os.remove("v2")
                                print("Pobieranie przerwane.")
                                print()
                            except AttributeError:
                                print("Nie ma wybranej rozdzielczości dla tego filmu.")
                                print()
                            except RegexMatchError:
                                print("Nieprawidłowy link.")
                                print()
                            break
                    if user_choice == 3:
                        while True:
                            try:
                                user_input = input("Wklej link: ")
                                if re.search(r"youtube.com", user_input):
                                    get_video_only(user_input, "2160p")
                                    show_info(user_input)
                                    restart()
                                else:
                                    print("Podaj prawidłowy link.")
                                    continue
                            except FileNotFoundError:
                                os.remove("v2")
                                print("Pobieranie przerwane.")
                                print()
                            except AttributeError:
                                print("Nie ma wybranej rozdzielczości dla tego filmu.")
                                print()
                            except RegexMatchError:
                                print("Nieprawidłowy link.")
                                print()
                            break
                    if user_choice == 4:
                        print()
                        break
                continue
            if user_choice == 3:
                while True:
                    try:
                        user_input = input("Wklej link: ")
                        if re.search(r"youtube.com", user_input):
                            get_only_audio(user_input)
                            show_info(user_input)
                            restart()
                        else:
                            print("Podaj prawidłowy link.")
                            continue
                    except FileNotFoundError:
                        os.remove("a1")
                        print("Pobieranie przerwane.")
                        print()
                        break
            if user_choice == 4:
                video = ffmpeg.input(askopenfilename(title="Wybierz plik wideo:"))
                audio = ffmpeg.input(askopenfilename(title="Wybierz plik audio:"))
                destination = asksaveasfilename(
                    title="Wybierz miejsce zapisu:", defaultextension='.mp4', initialfile="merged_video.mp4")
                print("Merging in progress...")
                ffmpeg.output(audio, video, "finished_video.mp4").run(overwrite_output=True)
                source = "finished_video.mp4"
                os.replace(source, destination)
                cowsay.cow("Połączono!")
                print()
                restart()
            if user_choice == 5:
                quit()
        except ValueError:
            print("Wybierz opcję od 1-5.")
            print()


if __name__ == '__main__':
    main()