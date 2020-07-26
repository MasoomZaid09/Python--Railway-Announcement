from pydub  import AudioSegment
import pandas as pd
from gtts import gTTS

#pip install 'xlrd' for pandas dependency

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS( text = mytext, lang=language,slow = False)
    myobj.save(filename)

def mergeAudios(audios):
    combind = AudioSegment.empty()
    for audio in audios:
        combind += AudioSegment.from_mp3(audio)
    return combind

def generate_HindiSound():

    #load audio using pydub
    audio = AudioSegment.from_mp3('railway.mp3')

    #generate - kripya dhyaan dijiye
    start = 41000
    finish = 44000

    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format = "mp3")


    # Generate  - se chalkar
    start = 45000
    finish = 46000

    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format = "mp3")

    # Generate - ke Raste
    start = 47500
    finish = 48500

    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format = "mp3")

    # Generate - ko jaane wali
    start = 49500
    finish = 52500

    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format = "mp3")


    # Generate - kuchh hi samay me pltfrm no
    start = 59000
    finish = 62000

    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format = "mp3")


    # Generate  - Music
    start = 41000
    finish = 42000

    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format = "mp3")






def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    # print(df)
    for index,item in df.iterrows():
        # Generate - train no and train name
        textToSpeech(item['train_no'] + " " + item['train_name'] , '2_hindi.mp3')
        # Generate - from
        textToSpeech(item['from'] , '4_hindi.mp3')
        # Generate - to
        textToSpeech(item['to'] , '6_hindi.mp3')
        # Generate - via
        textToSpeech(item['via'] , '8_hindi.mp3')
        # Generate - platform number
        textToSpeech(item['platform'] , '10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)

        announcement.export(f"announcement_hindi_{item['train_no']}_{index+1}.mp3", format="mp3")
        


if __name__ == "__main__":
    print("generating Audios:")
    generate_HindiSound()
    generateAnnouncement("announce_hindi.xlsx")
    print("generate announcement completed")




