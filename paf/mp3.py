import pytube
import os

if not os.path.exists('download'):
    os.makedirs('download')


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


clearConsole()


print("\033[1m" + "Youtube Dowload Video" + "\033[0m")

url = input("link : ")
youtube = pytube.YouTube(url)

video = youtube.streams.get_audio_only()

video.download('download')

os.chdir('download')

x = video.title + ".mp4"

if x == video.title + ".mp4":
    print("no")
    base = os.path.splitext(x)[0]
    os.rename(x, base + '.mp3')

clearConsole()

print("\033[1m" + video.title + "\033[0m")

print("\nSuccess... \n")
