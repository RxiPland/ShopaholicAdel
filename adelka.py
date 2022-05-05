from scrapetube import get_channel
from pyperclip import copy
from os import system
from webbrowser import open_new_tab

def clear_obrazovku():

    system('cls')

def main():

    clear_obrazovku()

    videos = get_channel("UCSCbqi3AZ_JCdnubIUZZ_jw", sort_by='newest')      # adela youtube ID --> UCSCbqi3AZ_JCdnubIUZZ_jw

    for video in videos:

        break

    video = str(video['videoId'])

    try:

        f = open("posledni_video.txt", "rb")
        posledni = f.readlines()
        f.close()
        posledni = str(posledni[0].decode("UTF-8"))

    except:

        posledni = ""

    if posledni == video:

        url = "https://www.youtube.com/watch?v=" + video + posledni

        print("Žádné nové video.\n\nStaré: " + url)

    else:

        f = open("posledni_video.txt", "wb")
        f.write(video.encode("UTF-8"))
        f.close()

        url = "https://www.youtube.com/watch?v=" + video

        print("Nové video!\n\n" + url)


    konec = input("\n[K]opírovat URL\n[O]tevřít v prohlížeči\n[E]xit\n\n").upper()

    if konec == "K":

        copy(url)

    elif konec == "O":

        open_new_tab(url)

    else:

        pass

main()