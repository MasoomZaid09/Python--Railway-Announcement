from pydub  import AudioSegment
import pandas as pd
from gtts import gTTS

#pip install 'xlrd' for pandas dependency

def textToSpeech(text, filename):
    mytext = str(text)
    language = 'en-in'
    myobj = gTTS( text = mytext, lang=language)
    myobj.save(filename)

def mergeAudios(audios):
    combind = AudioSegment.empty()
    for audio in audios:
        combind += AudioSegment.from_mp3(audio)
    return combind



def generate_EnglishSound():
    #load audio by pydub
    audio = AudioSegment.from_mp3('railway.mp3')


    #generate - may i have attention
    start = 19000
    finish = 24000

    audioProcessed = audio[start:finish]
    audioProcessed.export("1_english.mp3", format = "mp3")


    # Generate  - From 
    start = 30000
    finish = 31000

    audioProcessed = audio[start:finish]
    audioProcessed.export("3_english.mp3", format = "mp3")

    # Generate - To
    start = 32000
    finish = 33000

    audioProcessed = audio[start:finish]
    audioProcessed.export("5_english.mp3", format = "mp3")

    # Generate - via
    start = 34000
    finish = 35000

    audioProcessed = audio[start:finish]
    audioProcessed.export("7_english.mp3", format = "mp3")


    # Generate - is arriving
    start = 36000
    finish = 40000

    audioProcessed = audio[start:finish]
    audioProcessed.export("9_english.mp3", format = "mp3")


    # Generate  - Music
    start = 41000
    finish = 42000

    audioProcessed = audio[start:finish]
    audioProcessed.export("11_english.mp3", format = "mp3")




def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    # print(df)
    for index,item in df.iterrows():#iterrows is used for itrate rows in a excel file
        # Generate - train no and train name
        textToSpeech(item['train_no'] + " " + item['train_name'] , '2_english.mp3')
        # Generate - from
        textToSpeech(item['from'] , '4_english.mp3')
        # Generate - to
        textToSpeech(item['to'] , '6_english.mp3')
        # Generate - via
        textToSpeech(item['via'] , '8_english.mp3')
        # Generate - platform number
        textToSpeech(item['platform'] , '10_english.mp3')

        audios = [f"{i}_english.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)

        announcement.export(f"announcement_english_{{item['train_no']}}_{index+1}.mp3", format="mp3")
        


if __name__ == "__main__":
    print("generating Audios:")
    generate_EnglishSound()
    generateAnnouncement("announce_hindi.xlsx")
    print("generate announcement completed")




