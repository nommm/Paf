import pytube
import os
import defL

defL.chckfolder()
defL.clearConsole()

print("\033[1m" + "Youtube Dowload Video" + "\033[0m")

url = input("link : ")
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download('download')


os.chdir('download')

n = video.title + "_video.mp4"
if os.path.exists(n):
    os.remove(n)

x = video.title + ".mp4"
if x == video.title + ".mp4":

    base = os.path.splitext(x)[0]
    os.rename(x, base + '_video.mp4')


defL.clearConsole()


print("\033[1m" + video.title + "\033[0m")
print(video.resolution, str(video.fps) + "fps")

print("\nSuccess... \n")
os.system('pause')
defL.Rn()
