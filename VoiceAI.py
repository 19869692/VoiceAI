from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
import speech_recognition as sr
import pyttsx3
import time

root = Tk()
root.geometry('900x700')
load = Image.open('bg.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image =render)
img.place(x=0,y=0)

def record():
    robot_mouth = pyttsx3.init()
    robot_ear = sr.Recognizer()
    while True:
     
        with sr.Microphone() as mic: 
                robot_ear.adjust_for_ambient_noise(mic)
                print("AI Recognition: I'm listening")
                audio = robot_ear.listen(mic)
                time.sleep(1)
        try:        
                user = robot_ear.recognize_google(audio)  
                user = user.lower()
                print("User: " + user)
        except sr.UnknownValueError:
                
                robot_brain = "Could you please repeat that"
                robot_ear = sr.Recognizer()
                user = ""
                continue
        
        if "hello" in user:
            robot_brain = "Hello user"
        elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" in user:
            robot_brain = user
        elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power"and "Three Quarters Power" and "Full Power" in user:
            robot_brain = user
        elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power"and "Three Quarters Power" and "Full Power" + "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power"and "Three Quarters Power" and "Full Power" in user:
            robot_brain = user
        elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power"and "Three Quarters Power" and "Full Power" + "Aft" and "Fore, Port" and "Starboard" and "Port Quarter"and "Starboard Quarter" in user:
            robot_brain = user
        elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + " and " + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "Aft" and "Fore, Port" and "Starboard" and "Port Quarter"and "Starboard Quarter" in user:
            robot_brain = user
        elif "exit" in user:
            robot_brain = "Bye!"
            print("AI Recognition: " + robot_brain)
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            break
        
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()

    
def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("FAQ")
    newWindow.geometry("400x400")
    Label(newWindow, text ="This is FAQ \n What should be clicked to start recording my live audio? \n "
    "-Please click on the mic button\n\n\n\nAvaialble commands\n[Tug Name], pull/push* [Power Amount]\n"
    "[Tug Name], pull directly* astern\n[Tug Name], all stop\n[Tug Name], move to pull/push - [Tug Name], be ready to pull/push\n"
    "[Tug Name], move to [Position]\n[Tug Name], square up\n\n<Tug Name>'s\nTug Alpha, Bravo, Charlie\nTug 1,2,3\nTug A,B,C\n\n"
    "<Position>\nAft, Fore, Port, Starboard, Port Quarter, Starboard Quarter\n\n<Power Amount>\n5%, 10%, 25%, 50%, 75%, 100%\nminimum, minimum Weight, Bare Weight\n"
    "Quarter Power*, Half Power*, Three Quarters Power*, Full Power*").pack()

def filepath():
    filepath = filedialog.askopenfilename(title="open file",filetypes=(("Insert mp3 files only!!","*.mp3") ,("text files","*.txt")))
    file = open(filepath)
    print(filepath)
    file.close()

def func():
    top = Toplevel()
    top.title('File browser')
    top.geometry("600x400")
    load1 = Image.open('w1.png')
    render1 = ImageTk.PhotoImage(load1)
    img11 = Label(top,image =render1)
    img11.place(x=0,y=0) 
    img7 = PhotoImage(file = 'button.w.png')
    button7 = Button(top,image=img7,command =filepath)
    button7.pack(pady=10)
    button7.place(x=250, y=100)
    Label(top, text ="Please insert your pre-recorded audio here").pack()
    Label.place(x=100,y=100)

def chatLog():
    chatBox = Toplevel()
    chatBox.title('Chat Log')
    chatBox.geometry("300x500")
    extract = Button(chatBox, text = 'Extract')
    extract.place(x = 125, y = 450)
    txt = Text(chatBox, height=27)
    txt.grid(row=1, column=0, columnspan=1)
    txt.insert(END ,"User: Tug Alpha, pull 50%\n")
    txt.insert(END ,"\nAI: Tug Alpha is now at 50% power\n")
    txt.insert(END ,"\nUser: Tug Alpha, push Full Power\n")
    txt.insert(END ,"\nAI: Tug Alpha is now at Full Power\n")
    txt.insert(END ,"\nUser: sdvezxv\n")
    txt.insert(END ,"\nAI: Tug Alpha, could you please \nrepeat that again?\n\n")
    txt.config(state=DISABLED)
    

#record button
img3 = PhotoImage(file = 'record.png')
button3 = Button(root,image = img3,border=00, command = record)
button3.place(x=10, y=10)

#FAQ Button
img1 = PhotoImage(file = 'button.png')
button1 = Button(root,image = img1,border=2,command = openNewWindow, justify = 'right')
button1.place(x=770, y=630)


#Chat Log
img2 = PhotoImage(file = 'chatlog.png')
button2 = Button(root,image = img2,border=0, command = chatLog)
button2.place(x=100, y=10)


#FIle Browser Icon
img4 = PhotoImage(file = 'folder.png')
button4 = Button(root,image = img4,border=00,command = func)
button4.place(x=10, y=630)

#logo but used as a buttons
img5 = PhotoImage(file = 'logo111.png')
labelLogo = Label(root, image = img5)
labelLogo.place(x=680, y=10)


root.mainloop()