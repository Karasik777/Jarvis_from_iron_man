import os 
import sys 
import pyttsx3
import gtts
import selenium
import wolframclient as wolframalpha
import playsound
import speech_recognition as sr 
#Other useful libraries for cli and speech recognition 


NotShutdown = 1
MessageNum = 1 #Keep track of how many things you said
def say(message):
    global MessageNum

    MessageNum += 1
    print("Assistant : ", message)

    toSay = gtts.gTTS(text=message, lang='en', slow=False)
    #Save message
    file = str(MessageNum)+".mp3"
    toSay.save(file)
    #Play message
    playsound.playsound(file, True)
    #remove old message
    os.remove(file)
    


#If the return is an ambigous value the function failed
def get_instruction():

    rObject = sr.Recogniser()
    userMessage = ''

    with sr.Microphone() as source:
        print("Awaiting Instructions...\n")
        #Record message from user
        audio = rObject.listen(source, phrase_time_limit = 5)
    #Timeout
    print("Maximum instruction duration achieved\n")

    try:
        text = rObject.recognise_google(audio, language='en-US')
        return text
    
    except:
        say("I couldn't understand that, please say again!")
        return -1


#Function to open applications 
def open_application():
    if "chrome" in input:
        say("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "firefox" in input or "mozilla" in input:
        say("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in input:
        say("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input:
        say("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    else:
        say("App not found.")
        return


#Function to do a web search of whatever
def search_web(input):
    #initialise webdriver
    driver = selenium.webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()
 
    if 'youtube' in input.lower():
        say("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return
 
    elif 'wikipedia' in input.lower():
        say("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
 
    else:
        if 'google' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
 
        elif 'search' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
 
        else:
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
        return

#Input into text and process instructions
def process_instruction(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        elif "who are you" in input or "define yourself" in input:
            speak = "I am your personal assistant Jarvis, here to make your workflow faster!"
            say(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Sheetansh Kumar."
            say(speak)
            return

        elif "calculate" in input.lower(): ##Will be fully implemented later on 
            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id)
            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            say("The answer is " + answer)
            return

        elif 'open' in input:
            # another function to open 
            # different application available
            open_application(input.lower()) 
            return

        else:
            say("I can search the web for you, Would you like to search right now?")
            ans = get_instruction()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except:
        say("I'm not quite sure, would you like me to google it?")
        ans = get_instruction()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


def main():
    #Introductions
    say("Hello! I am your virtual assistant Jarvis, what can I call you?")
    say("Please respond with one word.")
    name = "User"
    name = get_instruction()
    say("Hello, " + name + '.')

    #Main loop execution
    while(1 and NotShutdown):
        say("How may I help?")
        instruction = get_instruction().lower()
        
        if instruction == 0:
            continue

        if "exit" or "shutdown" or "sleep" or "Bye" or "goodbye" in str(instruction):
            NotShutdown = 0
            break
        process_instruction(instruction)


    

if __name__ == "__main__":
    main()
