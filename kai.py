import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import keyboard
import pyautogui
import requests
import speedtest                          #pip install speedtest-cli
import json
import datetime
from time import sleep
from  playsound import playsound
from PyDictionary import PyDictionary
from googletrans import Translator        # pip install googletrans==3.1.0a0 (new version work)
from pywikihow import search_wikihow      # pip install pywikihow

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
#print(voices)
Assistant.setProperty('voice', voices[0].id)

def Speak(audio):
    print(" ")
    Assistant.say(audio)
    print(f"KAI- {audio}")
    print("  ")
    Assistant.runAndWait()

#Speak('hello there,  how are you')

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("------------------------------------------------------------------------------------------")
        print("Listening your voice.......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Getting voice......\n")
            print("------------------------------------------------------------------------------------------")
            query = command.recognize_google(audio, language='en-in')
            print(f"YOU SAID- {query}")

        except:
            return "None"

        return query.lower()
Speak("hello i am kai . how can i help you? BUT i wont talk to a girl whose name is srishti")

#query = takecommand()
#for opening apps and websites


def NewsReader():
    Speak("ok. welcome to news section. Listen today's top 5 news. ")
    print("----------------------------------------------------------Top 5 NEWS FOR THE DAY ----------------------------------------------------------------")
    url = ("https://newsapi.org/v2/top-headlines?country=in&apiKey=f6372b28d4994aaa822e846cee5de4d0")
    news = requests.get(url).text
    news_dict = json.loads(news)
    for i in range(5):
        if i == 4:

            Speak('this is the last news for the day. listen carefully.')
            #print("News", i + 1, "-", news_dict['articles'][i]['title'])
            Speak(news_dict['articles'][i]['title'])
            print("For full article click on to the link-\n", news_dict['articles'][i]['url'])
            Speak('Thank you!. for listening')
            print(
                "---------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Thank you! for listening")

        else:
            #print("News", i + 1, "-", news_dict['articles'][i]['title'])
            Speak(news_dict['articles'][i]['title'])
            print("For full article click on to the link-\n", news_dict['articles'][i]['url'])
            Speak('Now, moving toward another news headlines')

        print(
            "---------------------------------------------------------------------------------------------------------------------------------------------------")

def Dict():
    Speak("ok. tell me the word. and also tell me what you want? Meaning, antonym or synonym? ")
    word = takecommand()

    if 'meaning' in word:
        word = word.replace("KAI", "")
        word = word.replace("what is", "")
        word = word.replace("meaning of","")
        ans = PyDictionary.meaning(word)
        Speak(f"The Meaning of {word} is {ans}")

    elif 'antonym' in word:
        word = word.replace("KAI", "")
        word = word.replace("what is", "")
        word = word.replace("antonym of", "")
        ans = PyDictionary.antonym(word)
        Speak(f"The Antonym of {word} is {ans}")

    elif 'synonym' in word:
        word = word.replace("KAI", "")
        word = word.replace("what is", "")
        word = word.replace("synonym of", "")
        ans = PyDictionary.synonym(word)
        Speak(f"The Synonym of {word} is {ans}")

def Alarm():
    Speak("please enter the time of alarm ")
    set_alarm= input("Enter the Time")
    while True:
        time = datetime.datetime.now()
        time_str = time.strftime("%H:%M")

        if time_str == set_alarm:
            Speak("Wake up!. Wake up!.Wake up!")
            Speak("you set an alarm. now its time to wake up. Please.. ")
            playsound('Kabir Singh Bekhayali.mp3')
            Speak("alarm is now closing. I hope you wake up!")
        elif time_str>set_alarm:
            break

def Hindi_Command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("------------------------------------------------------------------------------------------")
        print("Listening your voice.......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Getting voice......\n")
            print("------------------------------------------------------------------------------------------")
            query = command.recognize_google(audio, language='hi')
            print(f"YOU SAID- {query}")

        except:
            return "None"

        return query.lower()

def Hindi_Translator():
    Speak("Tell me what you want to translate?")
    query = Hindi_Command()
    translate = Translator()
    output = translate.translate(query)
    Text = output.text
    Speak(Text)

def Reminder():
    Speak("Tell me what reminder you want to save?")
    reminderVoice = takecommand()
    reminder = open('reminder.text','w')
    reminder.write(reminderVoice)
    Speak("you tell me to save-"+reminderVoice)
    Speak("ok. i remember it. you can ask me any time")
    reminder.close()

def WhatsAppMsg(name, message):
    os.startfile("C:\\Users\\VANSHIKA\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    pyautogui.click(x=203, y=138)
    sleep(1)
    keyboard.write(name)
    sleep(1)
    pyautogui.click(x=243, y=306)
    sleep(1)
    pyautogui.click(x=822, y=997)
    sleep(1)
    keyboard.write(message)
    keyboard.press('enter')

def WhatsAppCall(name):
    os.startfile("C:\\Users\\VANSHIKA\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    pyautogui.click(x=203, y=138)
    sleep(1)
    keyboard.write(name)
    sleep(1)
    pyautogui.click(x=243, y=306)
    sleep(1)
    pyautogui.click(x=1733, y=67)

def WhatsAppVideoCall(name):
    os.startfile("C:\\Users\\VANSHIKA\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    pyautogui.click(x=203, y=138)
    sleep(1)
    keyboard.write(name)
    sleep(1)
    pyautogui.click(x=243, y=306)
    sleep(1)
    pyautogui.click(x=1668, y=71)


def Task_doing():
    while True:
        query = takecommand()


    #wishing command
        if 'hello' in query or 'hey' in query:
            Speak("hello, nice to see you")

        elif 'how are you' in query:
            Speak("I am good, what about you?")

        elif 'what is your name' in query:
            Speak("My name is KAI. I am a chat bot.")



    #time
        elif 'time' in query or 'date' in query:
            time = datetime.datetime.now()
            time_str = time.strftime("%H:%M")
            date_str = time.strftime("%D")
            #time_f = time_str.ctime()
            Speak(f"Todays Time is {time_str}")
            Speak(f"Todays Date is {date_str}")



    #Repeating my voice
        elif 'repeat' in query:
            Speak("ok. I am ready to say. now tell me")
            my_instruction = takecommand()
            Speak(my_instruction)


    #stoping commands for chat bot
        elif 'KAI stop' in query or 'stop' in query:
            Speak("ok. I am stopping my self. you can call me any time. thank you")
            break

        elif 'quit' in query:
            Speak("ok. I am quiting my self. you can call me any time. thank you")
            break

        elif 'exit' in query:
            Speak("ok. I am exiting my self. you can call me any time. thank you")
            break

        elif 'sleep' in query:
            Speak("ok bye. you can call me any time. thank you ")
            break



    #youtube search
        elif 'youtube search' in query or 'search on youtube' in query:
            Speak("what you want to search in youtube?")
            if "None" in takecommand():
                Speak("It seems like you don't say anything. please say, youtube search, again, and then say what you want to search in youtube.")
            else:
                query = takecommand()
                Speak("ok. i am searching")
                query = query.replace("KAI", "")
                query = query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                Speak("Done")



    # music online play from youtube
        elif 'play music' in query or 'play song' in query:
            Speak("tell me the name of song")
            musicName = takecommand()
            if "None" in takecommand():
                Speak("It seems like you don't say anything. please say, play music again, and then say the name of music")
            else:
                pywhatkit.playonyt(musicName)
                Speak("playing your song.")



    # youtube automation
        elif 'pause' in query:
            keyboard.press('space bar')
            Speak("ok")

        elif 'play' in query:
            keyboard.press('space bar')
            Speak("ok")

        elif 'full screen' in query:
            keyboard.press("f")
            Speak("ok")

        elif 'resize' in query or 'normal screen' in query:
            keyboard.press("f")
            Speak("ok")

        elif 'restart' in query:
            keyboard.press('0')
            Speak("ok")

        elif 'move' in query or 'skip forward' in query:                                                                                                                                     
            keyboard.press('1')
            Speak("ok")

        elif 'back' in query or 'skip backward' in query:
            keyboard.press('j')
            Speak("ok")

        elif 'skip ad' in query or 'ad' in query:
            pyautogui.click(x=1220, y=734)
            Speak("ok")



        #system volume controler
        elif 'volume up' in query or 'volume increase' in query:
            pyautogui.press("volumeup",10)
            Speak("ok")

        elif 'volume down' in query or 'volume decrease' in query:
            pyautogui.press("volumedown",10)
            Speak("ok")

        elif 'mute volume' in  query or 'mute' in query:
            pyautogui.press("volumemute")
            Speak("ok")




    #google search
        elif 'google search' in query or 'search on google' in query:
            Speak("what you want to search in google?")
            if "None" in takecommand():
                Speak("It seems like you don't say anything. please say, google search, again, and then search what you want.")
            else:
                query = takecommand()
                Speak("ok. i am searching")
                #query = query.replace("KAI","")
                #query = query.replace("google search","")
                pywhatkit.search(query)
                Speak("done")



    #website open
        elif 'website' in query:
            Speak("tell me the name of website")
            if "None" in takecommand():
                Speak("It seems like you don't say anything. please say, open website again, and then say the name of website")
            else:
                query = takecommand()
                Speak("ok. i am opening")
                query = query.replace("KAI","")
                query = query.replace("open", "")
                query = query.replace("website", "")
                query = query.replace(" ", "")
                web = 'https://www.'+ query + '.com'
                webbrowser.open(web)
                Speak("done")



    #chrome automation
        elif 'new window' in query or 'new tab' in query:
            keyboard.press_and_release('ctrl + t')
            Speak("ok")

        elif 'close tab' in query or 'close window' in query:
            keyboard.press_and_release('ctrl + w')
            Speak("ok")

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            Speak("ok")

        elif 'download' in query:
            keyboard.press_and_release('ctrl + j')
            Speak("ok")

        elif 'incognito' in query:
            keyboard.press_and_release('ctrl + shift + n')
            Speak("ok")



    #wikipedia search
        elif 'wikipedia' in query:
            Speak("what you want to search in wikipedia?")
            if "None" in takecommand():
                Speak("It seems like you don't say anything. please say, wikipedia again, and then search what you want.")
            else:
                query = takecommand()
                query = query.replace("KAI", "")
                query = query.replace("search", "")
                query = query.replace("in", "")
                wiki = wikipedia.summary(query,2)
                Speak(f"According to wikipedia : {wiki}")



    #wikihow, ask any thing from KAI. This will scrap data from internet and give output
        elif 'how' in query:
            Speak("ok. I am telling you. please wait for a second")
            query = query.replace("KAI", "")
            result = search_wikihow(query)
            #result[0].print()
            Speak(result[0].summary)



    #open app function
        elif 'open code' in query:
            Speak("ok. opening")
            os.startfile("C:\\Users\\VANSHIKA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'open whatsapp' in query:
            Speak("ok. opening")
            os.startfile("C:\\Users\\VANSHIKA\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

        elif 'open chrome' in query:
            Speak("ok. opening")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open pycharm' in query:
            Speak("ok. opening")
            os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2\\bin\\pycharm64.exe")

        elif 'open facebook' in query:
            Speak("ok. opening")
            webbrowser.open("https://www.facebook.com/")

        elif 'open instagram' in query:
            Speak("ok. opening")
            webbrowser.open("https://www.instagram.com/")

        elif 'open youtube' in query:
            Speak("ok. opening")
            webbrowser.open("https://www.youtube.com/")

        elif 'open gmail' in query:
            Speak("ok. opening")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")



    # close app function
        elif 'close code' in query:
            Speak("ok. closing")
            os.system("TASKKILL /F /im Code.exe")

        elif 'close whatsapp' in query or 'cut call' in query:
            Speak("ok. closing")
            os.system("TASKKILL /F /im WhatsApp.exe")


        elif 'close chrome' in query:
            Speak("ok. closing")
            os.system("TASKKILL /F /im Chrome.exe")


        elif 'close pycharm' in query:
            Speak("ok. closing")
            os.system("TASKKILL /F /im pycharm64.exe")


        elif 'close facebook' in query:
            Speak("ok. closing")
            keyboard.press_and_release('ctrl + w')



        elif 'close instagram' in query:
            Speak("ok. closing")
            keyboard.press_and_release('ctrl + w')


        elif 'close youtube' in query:
            Speak("ok. closing")
            keyboard.press_and_release('ctrl + w')


        elif 'close gmail' in query:
            Speak("ok. closing")
            keyboard.press_and_release('ctrl + w')




    #news reader function call
        elif 'news' in query:
            NewsReader()



    #checking speed of internet
        elif 'speed' in query or 'internet speed' in query:
            Speak("Checking your internet speed. It will take little bit of time. Please wait")
            print("Processing..........")
            speed = speedtest.Speedtest()
            downSpeed = speed.download()
            downSp_MBPS = int(downSpeed/800000)    # to convert mbpt into mbps divide by800000
            upSpeed = speed.upload()
            upSp_MBPS = int(upSpeed/800000)
            Speak(f"Your internet speed is.\n Downloading speed= {downSp_MBPS} mbps.\n Uploading speed= {upSp_MBPS} mbps.")




    #Alarm function call
        elif 'alarm' in query:
            Alarm()



    #Transalation function call
        elif 'translate' in query:
            Hindi_Translator()



    #Reminder function call
        elif 'reminder' in query or 'note' in query:
            Reminder()


    #what reminder is saved?
        elif 'remember' in query or 'what i say you to save' in query:
            remember = open('reminder.text', 'r')
            Speak("You save a reminder that says-"+remember.read())


    #Dictionary (meaning , antonym, synonym)
        elif 'dictionary' in query:
            Dict()      #this function call the dict function.if you want to open dictionary, say dictionary then say the word


                                #this will directly give the disctionary property without speaking dictionary. you just say meaning of then "word".
        elif 'meaning' in query:
            word = takecommand()
            word = word.replace("KAI", "")
            word = word.replace("what is", "")
            word = word.replace("meaning of", "")
            ans = PyDictionary.meaning(word)
            Speak(f"The Meaning of {word} is {ans}")

        elif 'antonym' in query:
            word = takecommand()
            word = word.replace("KAI", "")
            word = word.replace("what is", "")
            word = word.replace("antonym of", "")
            ans = PyDictionary.antonym(word)
            Speak(f"The Antonym of {word} is {ans}")

        elif 'synonym' in query:
            word = takecommand()
            word = word.replace("KAI", "")
            word = word.replace("what is", "")
            word = word.replace("synonym of", "")
            ans = PyDictionary.synonym(word)
            Speak(f"The Synonym of {word} is {ans}")



    # sending msg via whats aap
        elif 'whatsapp message' in query or 'send message' in query:
            Speak("Tell me the name of person.")
            contactName = str(takecommand())
            Speak(f"Tell me the message that you want to send {contactName}?")
            sendMsg = takecommand()
            Speak("ok. sending your message. It will take ten second")
            WhatsAppMsg(contactName, sendMsg)



    # sending voice call via whats aap
        elif 'whatsapp call' in query or 'voice call' in query:
            Speak("Tell me the name of person.")
            contactName = str(takecommand())
            Speak(f"ok. calling to {contactName}. It will take ten second")
            WhatsAppCall(contactName)




    # sending video call via whats aap
        elif 'whatsapp video call' in query or 'video call' in query:
            Speak("Tell me the name of person.")
            contactName = str(takecommand())
            Speak(f"ok. video calling to {contactName}. It will take ten second")
            WhatsAppVideoCall(contactName)


Task_doing()














