import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def tite():
    print("\033[1m" + "Video[0]" + "\033[0m")
    print("\033[1m" + "Audio[1]" + "\033[0m")

clearConsole()


tite()

while True:
    x = input('> ')
    if x == "0":

        import mp4 
        break

    elif x == "1":

        import mp3
        break

    else :

        clearConsole()
        tite()

        