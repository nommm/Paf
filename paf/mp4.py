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

video = youtube.streams.get_highest_resolution()

video.download('download')


clearConsole()


print("\033[1m" + video.title + "\033[0m")
print(video.resolution, video.fps + "fps")
print("\nSuccess... \n")


