import pafy
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

print("\033[1m" + "Youtube Download MP3" + "\033[0m")

url = input("link : ")
video = pafy.new(url)

clearConsole()

audiostreams = video.audiostreams
for i in audiostreams:
    print(i.bitrate, i.extension, i.get_filesize())
  
best = video.getbestaudio

audiostreams[3].download("download")


os.chdir('download')

filemp3 = video.title + ".webm" or '.m4a'
if filemp3 == video.title + ".mp3":
    print("pass")
else:
    print('no')
    base = os.path.splitext(filemp3)[0]
    os.rename(filemp3, base + '.mp3')

clearConsole()

print("\033[1m" + video.title + "\033[0m")
print(video.author)
print('\nSucess...\n')

input("Press Enter to continue...")

__main__()