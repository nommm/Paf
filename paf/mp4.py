import pytube
import os
import Run

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

n = video.title + "_video.mp4"
x = video.title + ".mp4"

if os.path.exists(n):
    os.remove(n)

if x == video.title + ".mp4":
    print("Yes")
    base = os.path.splitext(x)[0]
    os.rename(x, base + '_video.mp4')

clearConsole()


print("\033[1m" + video.title + "\033[0m")
print(video.resolution, video.fps + "fps")
print("\nSuccess... \n")

os.system('pause')

Run.Rn()
