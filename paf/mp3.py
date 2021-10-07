import pytube
import os
import defL

defL.chckfolder

defL.clearConsole()


print("\033[1m" + "Youtube Dowload Audio" + "\033[0m")

url = input("link : ")
youtube = pytube.YouTube(url)
video = youtube.streams.get_audio_only()
video.download("download")

os.chdir('download')

x = video.title + ".mp4"

n = video.title + "_video.mp3"
if os.path.exists(n):
    os.remove(n)

if x == video.title + ".mp4":

    base = os.path.splitext(x)[0]
    os.rename(x, base + '_audio.mp3')

defL.clearConsole()

print("\033[1m" + video.title + "\033[0m")
print("\nSuccess... \n")

os.system('pause')
defL.Rn()
