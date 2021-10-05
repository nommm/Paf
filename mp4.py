import pytube
import os
import __main__

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

video.download(os.chdir('download'))


clearConsole()


print("\033[1m" + video.title + "\033[0m")

print(video.resolution, video.fps)

print("\nSuccess... \n")


input("Press Enter to continue...")

__main__()