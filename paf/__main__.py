import os
import sys

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


clearConsole()


print("\033[1m" + "Video[0]" + "\033[0m")
print("\033[1m" + "Audio[1]" + "\033[0m")

def to_infinity():
    index=0
    while 1:
        yield index
        index += 1

for i in to_infinity():
    x = int(input('> '))
if x == 0:
    import mp4 
elif x == 1:
    import mp3
else:
    import __main__

