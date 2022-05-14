from scrapetube import get_channel
from pyperclip import copy
from os import system
from webbrowser import open_new_tab
from time import sleep

def clear_obrazovku():

    system('cls')

def main():

    clear_obrazovku()

    CHANNEL_ID = "UCSCbqi3AZ_JCdnubIUZZ_jw"      # adela youtube ID --> UCSCbqi3AZ_JCdnubIUZZ_jw

    videos = get_channel(CHANNEL_ID, sort_by='newest')

    for video in videos:

        break
        
    video_id = str(video['videoId'])
    nazev_videa = str(video['title']['runs'][0]['text'])
    vydani_videa_cas = str(video['publishedTimeText']['simpleText'])
    pocet_zhlednuti = str(video['viewCountText']['simpleText'])

    try:

        f = open("posledni_video.txt", "rb")
        posledni = f.readlines()
        f.close()
        posledni = str(posledni[0].decode("UTF-8"))

    except:

        posledni = ""

    if posledni == video_id:

        url = "https://www.youtube.com/watch?v=" + video_id + posledni

        print("Žádné nové video.\n\nStaré: " + url + "\n")

    else:

        f = open("posledni_video.txt", "wb")
        f.write(video_id.encode("UTF-8"))
        f.close()

        url = "https://www.youtube.com/watch?v=" + video_id

        print("Nové video!\n\nOdkaz: " + url + "\n")

    print("Název:", nazev_videa)
    print("Vydáno:", vydani_videa_cas)
    print("Počet zhlédnutí:", pocet_zhlednuti)

    print()


    konec = input("\n[K]opírovat URL\n[O]tevřít v prohlížeči\n[Y]outube kanál\n[E]xit\n\n").upper()

    if konec == "K":

        copy(url)

        print("\nURL byla uložena do schránky")

        for i in reversed(range(3)):

            print("Zavřu program za", i+1)
            sleep(1)

    elif konec == "O":

        open_new_tab(url)

    elif konec == "Y":

        open_new_tab("https://www.youtube.com/channel/" + CHANNEL_ID + "/videos")

    else:

        pass

main()



