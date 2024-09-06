import webbrowser
import subprocess # it will open the  file in the default program associated with .txt files
import pywhatkit
import pyjokes
import os # it will open the next file thgat you have enetered in the path
import datetime
import pyautogui
import wikipedia
import random
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty( 'voices' )
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


print("\t\t\t\t\t--------------CHATBOT----------------")
speak ("Hello! I am your chatbot.")
speak("Enter your name")
name = input("\t\t\tEnter your name : ").capitalize()
print("\t\t\t",name)

d_t=datetime.datetime.now().hour

if d_t>=0 and d_t<12:
    print("\t\t\t Good Morning!")
    speak(f"Good morning {name}")
elif 12<=d_t<16:
    print("\t\t\t Good Afternoon!")
    speak(f"Good afternoon {name}")
else:
    print("\t\t\t Good Evening!")
    speak(f"Good evening {name}")

print()
print("---------------------------------------------------------------------------------------------")

while True:
    
    _input=input("\t\t\tMe :").lower()
    word=['hello','hi','hey','hii',"helooo"]
    word1=['how are you','whats up','how are you doing']
    word2=['open google','google']
    word3=['open youtube','youtube','yt']
    word4=['open facebook','facebook']
    word5=['open instagram','insta','instagram']
    word6=['open spotify','spotify']
    word7=['open notepad','notepad']
    word8=['open controlpanel','controlpanel','open control panel','control panel']
    word9=['open cmd','cmd']
    word10=['exit','quit','bye','goodbye']
    word11=['jokes','joke','tell a joke',]
    word12=['volume up','volup','v+']
    word13=['volume down','voldown','v-']
    word14=['volume mute','mute']
    word15=['b+','bright']
    word17=['game','play game','start game']
    word16="wikipedia"
    

    if _input in word1:
     speak("I Am Fine Thank You")
     print("\t\t\tBOT : I Am Fine Thank You")

    elif _input in word:
      speak(f"Hello{name} How can i help you.")
      print("\t\t\tBOT : Hello, How can i help you.")


    elif _input in word2:
      speak("Opening Google")
      print("\t\t\tBOT : Opening Google")
      speak("What do you want me to search")
      print("\t\t\tWhat do you want me to search")
      _input=input("\t\t\tMe : ").lower()
      pywhatkit.search(_input)


    elif _input in word3:
      speak("Opening Youtube")
      print("\t\t\tBOT : Opening Youtube")
      speak("What do you want me to play for you")
      print("\t\t\tBOT : What do you want me to play for you")
      _input=input("\t\t\tMe : ").lower()
      speak("now playing"+_input)
      pywhatkit.playonyt(_input)


    elif _input in word4:
      speak("Opening Facebook")
      print("\t\t\tBOT : Opening Facebook")
      webbrowser.open("http://www.facebook.com")
    elif _input in word5:
      speak("Opening instagram")
      print("\t\t\tBOT : Opening Instagram")
      webbrowser.open("http://www.instagram.com")
    elif _input in word10:
      speak("OK It's Time ,I am going OFFLINE now ") 
      print("\t\t\tBOT : OK It's Time ,I am going OFFLINE")
      exit()

    elif _input in word6:
      speak(" Opening Spotify")
      print("\t\t\tBOT : Opening Spotify")
      subprocess.Popen("spotify")
    
    elif _input in word8:
        speak("Opening Control Panel")
        print("\t\t\tBOT : Opening Control Panel")
        subprocess.Popen('control panel')

    elif _input in word9:
        speak("Opening CMD")
        print("\t\t\tBOT : Opening CMD")
        subprocess.run('cmd')

    elif _input in word11: #joke section
       speak(pyjokes.get_joke())
      

    elif _input in word7:
       speak("Opening Notepad")
       print("\t\t\tBOT : Opening Notepad")
       os.system("c:\\Windows\\System32\\notepad.exe") 

    elif _input in word12:
       speak("Increasing the volume")
       print("\t\t\tBOT : Maxing The Volume")
       pyautogui.press("volumeup")
    elif _input in word13:
       speak("decreasing the volume")
       print("\t\t\tBOT : Minimising The Volume")
       pyautogui.press("volumedown")
    elif _input in word14:
       speak("Muting the volume")
       print("\t\t\tBOT : Muting the System")
       pyautogui.press("volumemute")
    elif _input in word15:
       print("\t\t\tBOT : Bright the Screen")
       pyautogui.press("brightnessup")

    elif word16 in _input:
       search = _input.replace(word16,"")
       print(wikipedia.summary(search, sentences=5))
       speak(wikipedia.summary(search, sentences=5))


    elif _input in word17:
      speak("Choose the game you want to play")
      choose=input("\t\t\tChoose the game you want to play\n\t\t\t1.Toss the Coin\n\t\t\t2.Guess the Number\n\t\t\tchoice is :").lower()
      print()
      print("\t\t\t----------------------------")
      while True:
         if 'toss the coin' in choose:
            speak("Enter Heads or Tails")
            user_side=input("\t\t\tEnter Heads or Tails :").capitalize()
            com_side=random.choice(['Heads','Tails'])
            print("\t\t\t",user_side,com_side)
            if user_side==com_side:
                speak("Congrats! You got it Right")
                print("\t\t\tCongrats! You got it Right......")
            else:
                speak("Sorry! You Lost this Time")
                speak("Better luck for Next Time")
                print("\t\t\tSorry! You Lost this Time.......")
                print("\t\t\tBetter luck for Next Time.......")
            speak("Do you want to continue? (yes/no)")    
            ask=input("\t\t\tDo you want to continue? (yes/no) :").lower()
            
            while ask =='no':
               exit()

         if 'guess the number' in choose:
            speak("Choose one number between 0 to 100 :")
            user_ch=int(input("\t\t\tChoose one number between 0 to 100 :"))
            com_ch=random.randint(0,100)
            print("\t\t\t",user_ch,com_ch)
            if user_ch==com_ch:
                speak("Congrats! You got it Right")
                print("\t\t\tCongrats! You got it Right......")
            else:
                speak("Sorry! You Lost this Time")
                speak("Better luck for Next Time")
                print("\t\t\tSorry! You Lost this Time.......")
                print("\t\t\tBetter luck for Next Time.......")
            speak("Do you want to continue? (yes/no)")    
            ask=input("\t\t\tDo you want to continue? (yes/no) :").lower()
            while ask =='no':
               exit()  
         # if 'rock paper scissors' in choose:
    else:
       speak("Sorry I didn't understand that")
       print("\t\t\tBOT : Sorry, I didn't understand that  ....!!!!!")