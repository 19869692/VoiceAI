from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog
import speech_recognition as sr
import pyttsx3
import time
import os

root = Tk()
root.geometry('900x700')
load = Image.open('bg.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image =render)
img.place(x=0,y=0)

userString = ""

def close():
    chatBox.withdraw()

def record():
    txt = Text(chatBox, height=27)
    txt.grid(row=1, column=0, columnspan=1)
    robot_mouth = pyttsx3.init()
    robot_ear = sr.Recognizer()
    
    #while True:
    with sr.Microphone() as mic: 
            #robot_ear.adjust_for_ambient_noise(mic)
            print("AI Recognition: I'm listening...")  
            audio = robot_ear.listen(mic)
            time.sleep(1.0)
    try:        
            user = robot_ear.recognize_google(audio)  
            user = user.lower()
            
            #replacement for "tug"
            time.sleep(1)
            user2 = user.replace("dolphin", "tug")
            while True:
                if "dog" in user:    
                    user2 = user.replace("dog", "tug")
                if "nothing" in user:   
                    user2 = user.replace("nothing", "tug")
                if "thug" in user:   
                    user2 = user.replace("thug", "tug")
                if "tuck" in user:   
                    user2 = user.replace("tuck", "tug")
                if "death" in user:   
                    user2 = user.replace("death", "tug")
                if "tough" in user:   
                    user2 = user.replace("tough", "tug")
                if "talk" in user:   
                    user2 = user.replace("talk", "tug")
                if "duck" in user:   
                    user2 = user.replace("duck", "tug")
                if "trap" in user:   
                    user2 = user.replace("trap", "tug")
                if "top" in user:   
                    user2 = user.replace("top", "tug")

                #replacement for "Charlie"
                while True:  
                    if "johnny" in user:
                        user2 = user.replace("johnny","charlie")
                    if "johnny " in user:
                        user2 = user.replace("johnny ","charlie")
                    if " johnny" in user:
                        user2 = user.replace(" johnny","charlie")
                    if "chinese" in user:
                        user2 = user.replace("chinese", "charlie")
                    if "shawnee" in user:
                        user2 = user.replace("shawnee", "charlie")
                    if "sunny" in user:
                        user2 = user.replace("sunny", "charlie")
                    if "tony" in user:
                        user2 = user.replace("tony", "charlie")
                    if "sony" in user:
                        user2 = user.replace("sony", "charlie")
                    break
                #replacement for "Bravo"
                if "grapple" in user:
                    user2 = user.replace("grapple", "bravo")
                if "breville" in user:
                    user2 = user.replace("breville", "bravo")
                if "grogol" in user:
                    user2 = user.replace("grogol", "bravo")
                if "wobble" in user:
                    user2 = user.replace("wobble", "bravo")
                if "trouble" in user:
                    user2 = user.replace("trouble", "bravo")
                if "gravel" in user:
                    user2 = user.replace("gravel", "bravo")
                if "roswell" in user:
                    user2 = user.replace("roswell", "bravo")
                if "rival" in user:
                    user2 = user.replace("rival", "bravo")
                if "garoppolo" in user:
                    user2 = user.replace("garoppolo", "bravo")
                if "graupel" in user:
                    user2 = user.replace("garoppolo", "bravo")          
                if "nuovo" in user:
                    user2 = user.replace("nuovo", "bravo")  
                if "rubble" in user:
                    user2 = user.replace("rubble", "bravo") 
                if "bubble" in user:
                    user2 = user.replace("bubble", "bravo") 
                if "bible" in user:
                    user2 = user.replace("bible", "bravo") 
                if "level" in user:
                    user2 = user.replace("level", "bravo")
                if "marvel" in user:
                    user2 = user.replace("marvel", "bravo")
                if "apple" in user:
                    user2 = user.replace("apple", "bravo")
                if "ravel" in user:
                    user2 = user.replace("ravel", "bravo")
                if "waffle" in user:
                    user2 = user.replace("waffle", "bravo")
                if "revelstoke" in user:
                    user2 = user.replace("revelstoke", "bravo stop")
                if "rainbow" in user:
                    user2 = user.replace("rainbow", "bravo")
                
                #Replacement for numbers and letters
                if "run" in user:
                    user2 = user.replace("run", "1")
                if "tree" in user:
                    user2 = user.replace("tree", "3")
                if "see" in user:
                    user2 = user.replace("see", "c")
                if "sea" in user:
                    user2 = user.replace("sea", "c")
                if "hey" in user:
                    user2 = user.replace("hey", "a")
                if "bee" in user:
                    user2 = user.replace("bee", "b")
                if "city" in user:
                    user2 = user.replace("city", "50")
                
                # Direction
                if "after" in user:
                    user2 = user.replace("after", "astern")
                if "austin" in user:
                    user2 = user.replace("austin", "astern")
                if "aftor" in user:
                    user2 = user.replace("aftor", "astern")
                if "active" in user:
                    user2 = user.replace("active", "astern")
                
                #replacement for "starboard"
                if "starbucks" in user:
                    user2 = user.replace("starbucks", "starboard")
                if "sabo" in user:
                    user2 = user.replace("sabo", "starboard")
                if "starmart" in user:
                    user2 = user.replace("starmart", "starboard")
                
                #replacement for positions
                while True:
                    if "potter" in user:
                        user2 = user.replace("potter", "quarter")
                    if "quantum" in user:
                        user2 = user.replace("quantum", "quarter")
                    if "water" in user:
                        user2 = user.replace("water", "quarter")   
                    if "water " in user:
                        user2 = user.replace("water ", "quarter")    
                    if "carter" in user:
                        user2 = user.replace("carter", "quarter")
                    if "father" in user:
                        user2 = user.replace("father", "quarter")
                    if "portel" in user:
                        user2 = user.replace("portel", "quarter")
                    if "portal" in user:
                        user2 = user.replace("portal", "quarter")
                    if "bottle" in user:
                        user2 = user.replace("bottle", "quarter")
                    if "bottle " in user:
                        user2 = user.replace("bottle ", "quarter")
                    if "butter" in user:
                        user2 = user.replace("butter","quarter")
                    if "cutter" in user:
                        user2 = user.replace("cutter","quarter")
                    if "park" in user:
                        user2 = user.replace("park", "port")
                    if "pot" in user:
                        user2 = user.replace("pot", "port")
                    if "part" in user:
                        user2 = user.replace("part", "port")
                    if "pop" in user:
                        user2 = user.replace("pop", "port")
                    if "pops" in user:
                        user2 = user.replace("pops", "port")
                    if "report" in user:
                        user2 = user.replace("report", "port")
                    if "fort" in user:
                        user2 = user.replace("fort", "port")
                    if "hot" in user:
                        user2 = user.replace("hot", "port")
                    if "four"in user:
                        user2 = user.replace("four", "fore")
                    if "fall"in user:
                        user2 = user.replace("fall", "fore")
                    if "app" in user:
                        user2 = user.replace("app", "up")
                    if "act" in user:
                        user2 = user.replace("act", "aft")
                    if "hospital" in user:
                        user2 = user.replace("hospital", "port quarter")
                    if "postpartum" in user:
                        user2 = user.replace("postpartum", "port quarter")
                    if "partquarter" in user:
                        user2 = user.replace("partquarter", "port quarter")
                    if "portwater" in user:
                        user2 = user.replace("portwater", "port quarter")
                    if "port water" in user:
                        user2 = user.replace("port water", "port quarter")
                    if "push water" in user:
                        user2 = user.replace("push water", "push quarter")
                    break
                
                #replacement for actions
                if "pool" in user:
                    user2 = user.replace("pool", "pull")
                if "pool " in user:
                    user2 = user.replace("pool ", "pull")
                if "poo" in user:
                    user2 = user.replace("poo", "pull")
                if "poor" in user:
                    user2 = user.replace("poor", "pull")
                if "bush" in user:
                    user2 = user.replace("bush", "push")
                if "put" in user:
                    user2 = user.replace("put", "push")
                if "busca" in user:
                    user2 = user.replace("busca", "push")
                if "pushpay" in user:
                    user2 = user.replace("pushpay", "push")
                if "pasta" in user:
                    user2 = user.replace("pasta", "push")
                if "pushy" in user:
                    user2 = user.replace("pushy", "push")
                if "pushed" in user:
                    user2 = user.replace("pushed", "push")
                if "food" in user:
                    user2 = user.replace("food", "push")
                if "who's" in user:
                    user2 = user.replace("who's", "push")
                if "push's" in user:
                    user2 = user.replace("push's", "push")
                if "verse" in user:
                    user2 = user.replace("verse", "push")
                if "who" in user:
                    user2 = user.replace("who", "push")
                if "puth" in user:
                    user2 = user.replace("puth", "push")
                if "boost" in user:
                    user2 = user.replace("boost", "push")
                if "fish" in user:
                    user2 = user.replace("fish", "push")
                if "music" in user:
                    user2 = user.replace("music", "push")
                if "stock" in user:
                    user2 = user.replace("stock", "stop")
                if "stopped" in user:
                    user2 = user.replace("stopped", "stop")
                if "way" in user:
                    user2 = user.replace("way","square")
                if "flare" in user:
                    user2 = user.replace("flare","square")
                if "squareup" in user:
                    user2 = user.replace("squareup", "square up")
                # Replacement for sentence
                while True:  
                    if "politically" in user:
                        user2 = user.replace("politically", "pull directly")
                    if "bluetooth" in user:
                        user2 = user.replace("bluetooth", "move to")
                    if "moto" in user:
                        user2 = user.replace("moto", "move to")
                    if "mutliple" in user:
                        user2 = user.replace("multiple", "move to pull")
                    if "tupac" in user:
                        user2 = user.replace("tupac","to port")
                    if "tupac potter" in user:
                        user2 = user.replace("tupac potter","to port quarter")
                    if "tupac bottle" in user:
                        user2 = user.replace("tupac bottle","to port quarter")
                    if "port father" in user:
                        user2 = user.replace("port father","port quarter")
                    if "port bottle" in user:
                        user2 = user.replace("port bottle","port quarter")
                    if "pop bottle" in user:
                        user2 = user.replace("pop bottle","port quarter")
                    if "bottle power" in user:
                        user2 = user.replace("bottle power","quarter power")
                    if "portal power" in user:
                        user2 = user.replace("portal power","quarter power")
                    if "potter power" in user:
                        user2 = user.replace("potter power","quarter power")
                    if "quattro power" in user:
                        user2 = user.replace("quattro power","quarter power")
                    if "water power" in user:
                        user2 = user.replace("water power","quarter power")
                    if "squatter power" in user:
                        user2 = user.replace("squatter power","quarter power")
                    if "father power" in user:
                        user2 = user.replace("father power","quarter power")
                    if "father powell" in user:
                        user2 = user.replace("father powell","quarter power")
                    if "waterfowl" in user:
                        user2 = user.replace("waterfowl","quarter power")
                    if "puth quarter power" in user:
                        user2 = user.replace("puth quarter power","push quarter power")
                    if "pushpaka power" in user:
                        user2 = user.replace("pushpaka power","push quarter power")
                    if "quarter-pound" in user:
                        user2 = user.replace("quarter-pound","quarter power")
                    if "charlie push" in user:
                        user2 = user.replace("charlie push","charlie push")
                    if "charlie multiport portter and pushbutton power" in user:
                        user2 = user.replace("charlie multiport portter and pushbutton power","Tug Charlie is moving to port quarter and pushing quarter power")
                    break
                # replacement for words
                if "wait" in user:
                    user2 = user.replace("wait", "weight")
                if "movie" in user:
                    user2 = user.replace("movie", "move")
                if "book" in user:
                    user2 = user.replace("book", "move")
                break
            
            print("User: " + user2)
            log.append(user2)
                
    except sr.UnknownValueError:
            robot_brain = "Could you please repeat that!"
            robot_ear = sr.Recognizer()
            user2 = ""
            
    except Exception as e:
            robot_brain = "System down!"       
            print(e)
            
    
    #Responses
    if "hello" in user2:
        robot_brain = "Hello user"    
    elif "tug" in user2:
        robot_brain = "Which tug are you refering to?"
    
    # Added together commands
    elif "charlie" in user2 and "square" in user2 and "ready" and "pull" in user2:
        robot_brain = "Tug Charlie is squaring up and ready to pull!"
    elif "bravo" in user2 and "square" in user2 and "ready" and "pull" in user2:
        robot_brain = "Tug Bravo is squaring up and ready to pull!"
    elif "alpha" in user2 and "square" in user2 and "ready" and "pull" in user2:
        robot_brain = "Tug Alpha is squaring up and ready to pull!"
    elif "charlie" in user2 and "square" in user2 and "ready" and "push" in user2:
        robot_brain = "Tug Charlie is squaring up and ready to push!"
    elif "bravo" in user2 and "square" in user2 and "ready" and "push" in user2:
        robot_brain = "Tug Bravo is squaring up and ready to push!"
    elif "alpha" in user2 and "square" in user2 and "ready" and "push" in user2:
        robot_brain = "Tug Alpha is squaring up and ready to push!"
    elif "charlie" in user2 and "move" and "port" in user2 and "quarter" in user2 and "and" and "push" in user2 and "quarter power" in user2:
        robot_brain = "Tug Charlie is moving to port quarter and pushing quarter power"
     
    # Push Command
    elif "bravo" in user2 and "push" and "100%" in user2:
        robot_brain = "Tug Bravo, pushed to 100% power!"
    elif "bravo" in user2 and "push" and "100" in user2 and "percent" in user2:
        robot_brain = "Tug Bravo, pushed to 100% power!"
    elif "bravo" in user2 and "push" and "full" and "power" in user2:
        robot_brain = "Tug Bravo, pushed to maximum power!"
    elif "bravo" in user2 and "push" and "75%" in user2:
        robot_brain = "Tug Bravo, pushed to 75% power!"
    elif "bravo" in user2 and "push" and "75" in user2 and "percent" in user2:
        robot_brain = "Tug Bravo, pushed to 75% power!"
    elif "bravo" in user2 and "push" and "50%" in user2:
        robot_brain = "Tug Bravo, pushed to 50% power!"
    elif "bravo" in user2 and "push"  and "50" in user2 and "percent" in user2:
        robot_brain = "Tug Bravo, pushed to 50% power!"
    elif "bravo" in user2 and "push" and "25%" in user2:
        robot_brain = "Tug Bravo, pushed to 25% power!"
    elif "bravo" in user2 and "push" and "25" in user2 and "percent" in user2:
        robot_brain = "Tug Bravo, pushed to 25% power!"
    elif "bravo" in user2 and "push" and "10%" in user2:
        robot_brain = "Tug Bravo, pushed to 10% power!"
    elif "bravo" in user2 and "push" and "10" in user2 and "percent" in user2:
        robot_brain = "Tug Bravo, pushed to 10% power!"
    elif "bravo" in user2 and "push" and "5"  and "%" in user2:
        robot_brain = "Tug Bravo, pushed to 5% power!"
    elif "bravo" in user2 and "push" and "5" in user2 and "percent" in user2:
        robot_brain = "Tug Bravo, pushed to 5% power!"
    
    elif "alpha" in user2 and "push" and "100%" in user2:
        robot_brain = "Tug Alpha, pushed to 100% power!"
    elif "alpha" in user2 and "push" and "100" in user2 and "percent" in user2:
        robot_brain = "Tug Alpha, pushed to 100% power!"
    elif "alpha" in user2 and "push" and "full" and "power" in user2:
        robot_brain = "Tug Alpha, pushed to maximum power!"
    elif "alpha" in user2 and "push" and "75%" in user2:
        robot_brain = "Tug Alpha, pushed to 75% power!"
    elif "alpha" in user2 and "push" and "75" in user2 and "percent" in user2:
        robot_brain = "Tug Alpha, pushed to 75% power!"
    elif "alpha" in user2 and "push" and "50%" in user2:
        robot_brain = "Tug Alpha, pushed to 50% power!"
    elif "alpha" in user2 and "push" and "50" in user2 and "percent" in user2:
        robot_brain = "Tug Alpha, pushed to 50% power!"
    elif "alpha" in user2 and "push" and "25%" in user2:
        robot_brain = "Tug Alpha, pushed to 25% power!"
    elif "alpha" in user2 and "push" and "25" in user2 and "percent" in user2:
        robot_brain = "Tug Alpha, pushed to 25% power!"
    elif "alpha" in user2 and "push" and "10%" in user2:
        robot_brain = "Tug Alpha, pushed to 10% power!"
    elif "alpha" in user2 and "push" and "10" in user2 and "percent" in user2:
        robot_brain = "Tug Alpha, pushed to 10% power!"
    elif "alpha" in user2 and "push" and "5" and "%" in user2:
        robot_brain = "Tug Alpha, pushed to 5% power!"
    elif "alpha" in user2 and "push" and "5" in user2 and "percent" in user2:
        robot_brain = "Tug Alpha, pushed to 5% power!"

    elif "charlie" in user2 and "push" and "100%" in user2:
        robot_brain = "Tug Charlie, pushed to 100% power!"
    elif "charlie" in user2 and "push" and "100" in user2 and "percent" in user2:
        robot_brain = "Tug Charlie, pushed to 100% power!"
    elif "charlie" in user2 and "push" and "75%" in user2:
        robot_brain = "Tug Charlie, pushed to 75% power!"
    elif "charlie" in user2 and "push" and "75" in user2 and "percent" in user2:
        robot_brain = "Tug Charlie, pushed to 75% power!"
    elif "charlie" in user2 and "push" and "50%" in user2:
        robot_brain = "Tug Charlie, pushed to 50% power!"
    elif "charlie" in user2 and "push" and "50" in user2 and "percent" in user2:
        robot_brain = "Tug Charlie, pushed to 50% power!"
    elif "charlie" in user2 and "push" and "25%" in user2:
        robot_brain = "Tug Charlie, pushed to 25% power!"
    elif "charlie" in user2 and "push" and "25" in user2 and "percent" in user2:
        robot_brain = "Tug Charlie, pushed to 25% power!"
    elif "charlie" in user2 and "push" and "10%" in user2:
        robot_brain = "Tug Charlie, pushed to 10% power!"
    elif "charlie" in user2 and "push" and "10" in user2 and "percent" in user2:
        robot_brain = "Tug Charlie, pushed to 10% power!"
    elif "charlie" in user2 and "push" and "5" and "%" in user2:
        robot_brain = "Tug Charlie, pushed to 5% power!"
    elif "charlie" in user2 and "push" and "5" in user2 and "percent" in user2:
        robot_brain = "Tug Charlie, pushed to 5% power!"
    
    # Push directly astern
    elif "bravo" in user2 and "pull" in user2 and "astern" in user2:
        robot_brain = "Tug Bravo, pulling directly astern!"
    elif "alpha" in user2 and "pull" in user2 and "astern" in user2:
        robot_brain = "Tug Alpha, pulling directly astern!"
    elif "charlie" in user2 and "pull" in user2 and "astern" in user2:
        robot_brain = "Tug Charlie, pulling directly astern!"
    
    # All stop command
    elif "bravo" in user2 and "stop" in user2:
        robot_brain = "Tug Bravo is now stopped!"
    elif "alpha" in user2 and "stop" in user2:
        robot_brain = "Tug Alpha is now stopped!"
    elif "charlie" in user2 and "stop" in user2:
        robot_brain = "Tug Charlie is now stopped!"
    
    # Square up
    elif "bravo" in user2 and "square" in user2:
        robot_brain = "Tug Bravo is now squaring up!"
    elif "alpha" in user2 and "square" in user2:
        robot_brain = "Tug Alpha is now squaring up!"
    elif "charlie" in user2 and "square" in user2:
        robot_brain = "Tug Charlie is now squaring up!"
    
    # Positions
    elif "bravo" in user2 and "move" in user2 and "fore" in user2:
        robot_brain = "Tug Bravo is moving to fore!"
    elif "charlie" in user2 and "move" in user2 and "fore" in user2:
        robot_brain = "Tug Charlie is moving to fore!"
    elif "alpha" in user2 and "move" in user2 and "fore" in user2:
        robot_brain = "Tug Alpha is moving to fore!"
    elif "bravo" in user2 and "move" in user2 and "port" in user2 and "quarter" in user2:
        robot_brain = "Tug Bravo is moving to port quarter!"
    elif "charlie" in user2 and "move" in user2 and "port" in user2 and "quarter" in user2:
        robot_brain = "Tug Charlie is moving to port quarter!"
    elif "alpha" in user2 and "move" in user2 and "port" in user2 and "quarter" in user2:
        robot_brain = "Tug Alpha is moving to port quarter!"
    elif "bravo" in user2 and "move" in user2 and "port" in user2:
        robot_brain = "Tug Bravo is moving to port!"
    elif "charlie" in user2 and "move" in user2 and "port" in user2:
        robot_brain = "Tug Charlie is moving to port!"
    elif "alpha" in user2 and "move" in user2 and "port" in user2:
        robot_brain = "Tug Alpha is moving to port!"
    
    # Ready to pull/push
    elif "alpha" in user2 and "move" in user2 and "pull" in user2:
        robot_brain = "Tug Alpha is moving to pull mode!"
    elif "alpha" in user2 and "ready" in user2 and "pull" in user2:
        robot_brain = "Tug Alpha is ready to pull!"
    elif "bravo" in user2 and "move" in user2 and "pull" in user2:
        robot_brain = "Tug Bravo is moving to pull mode!"
    elif "bravo" in user2 and "ready" in user2 and "pull" in user2:
        robot_brain = "Tug Bravo is ready to pull!"
    elif "charlie" in user2 and "move" in user2 and "pull" in user2:
        robot_brain = "Tug Charlie is moving to pull mode!"
    elif "charlie" in user2 and "ready" in user2 and "pull" in user2:
        robot_brain = "Tug Charlie is ready to pull!"
    
    elif "alpha" in user2 and "move" in user2 and "push" in user2:
        robot_brain = "Tug Alpha is moving to push mode!"
    elif "alpha" in user2 and "ready" in user2 and "push" in user2:
        robot_brain = "Tug Alpha is ready to push!"
    elif "bravo" in user2 and "move" in user2 and "push" in user2:
        robot_brain = "Tug Bravo is moving to push mode!"
    elif "bravo" in user2 and "ready" in user2 and "push" in user2:
        robot_brain = "Tug Bravo is ready to push!"
    elif "charlie" in user2 and "move" in user2 and "push" in user2:
        robot_brain = "Tug Charlie is moving to push mode!"
    elif "charlie" in user2 and "ready" in user2 and "push" in user2:
        robot_brain = "Tug Charlie is ready to push!"
    
    
    elif "exit" in user2 or "bye" in user2:
        robot_brain = "See you again!"       
    else:
         robot_brain = "Unknown Command! Could you please repeat that"
        
   
    
    print("AI Recognition: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    
    log.append(robot_brain)
    count = 0
    for x in log:
        if count % 2 == 1:
            txt.insert(INSERT, "User: ")
            txt.insert(INSERT,x + "\n")
        else:
            txt.insert(INSERT, "AI: ")
            txt.insert(INSERT,x + "\n")
        count += 1   
    user2 = ""

def openNewWindow():
    newWindow = Toplevel(root)
    newWindow.title("FAQ")
    newWindow.geometry("550x500")
    Label(newWindow, text ="This is FAQ \n What should be clicked to start recording my live audio? \n "
    "-Please click on the mic button\n\n\n\nAvaialble commands\n[Tug Name], pull/push* [Power Amount]\n"
    "[Tug Name], pull directly* astern\n[Tug Name], all stop\n[Tug Name], move to pull/push - [Tug Name], be ready to pull/push\n"
    "[Tug Name], move to [Position]\n[Tug Name], square up\n\n<Tug Name>'s\nTug Alpha, Bravo, Charlie\nTug 1,2,3\nTug A,B,C\n\n"
    "<Position>\nAft, Fore, Port, Starboard, Port Quarter, Starboard Quarter\n\n<Power Amount>\n5%, 10%, 25%, 50%, 75%, 100%\nminimum, minimum Weight, Bare Weight\n"
    "Quarter Power*, Half Power*, Three Quarters Power*, Full Power*").pack()


# Chat box but invisible
chatBox = Toplevel()
chatBox.title('Chat Log')
chatBox.geometry("400x500")
txt = Text(chatBox, width = 49,height=27)
txt.grid(row=1, column=0, columnspan=1)
closeBut = Button(chatBox, text = 'Close', command= close)
closeBut.place(x = 165, y = 450)
txt.config(state=DISABLED)
chatBox.withdraw()


def filepath():  
    txt = Text(chatBox, height=27)
    txt.grid(row=1, column=0, columnspan=1)
    
    robot_mouth = pyttsx3.init()
    robot_ear = sr.Recognizer()

    filepath = filedialog.askopenfilename(title="Open File",filetypes = ((".wav", "*.wav"), ("", "")))
    print(filepath)
    
    with sr.AudioFile(filepath) as source:
        print("File is being analysed...")
        audio = robot_ear.record(source)
    
    try:
        text1 = robot_ear.recognize_google(audio)
        text1.lower()
        text1.replace('hello', 'bye')
        print('User Input: ' + text1)
        
        log.append(text1)
             
    except Exception as e:      
        print(e)     
    
    
    if 'hello' in text1:
        robot_brain = 'Hello user!'
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    
    elif "alpha" and "pull" and "50" in text1:
        robot_brain = 'Tug Alpha, pulled 50% power!'
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    
    elif "alpha" and "pull" and "10" in text1:
        robot_brain = 'Tug Alpha, pulled 10% power!'
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    
    else:
        robot_brain = 'Could not detect command'
        print('AI Recognition: Could not detect command')  
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    
    log.append(robot_brain)
    
    count = 0
    for x in log:
        if count % 2 == 1:
            txt.insert(INSERT, "User: ")
            txt.insert(INSERT,x + "\n")
        else:
            txt.insert(INSERT, "AI: ")
            txt.insert(INSERT,x + "\n")
        count += 1
    txt.config(state = DISABLED)

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
    button7.place(x=200, y=200)
    img8 = PhotoImage(file = 'Nwwindowlg.png')
    button8 = Button(top,image=img8)
    button8.pack(pady=10)
    button8.place(x=440, y=10)
    Label(top, text ="Please insert your pre-recorded audio here").pack()
    Label.place(x=100,y=100)
   
def showChatLog():
    chatBox.deiconify()
def hideChatLog():
    chatBox.withdraw()

# Avoid triggering close event when click on "X" Button
chatBox.protocol("WM_DELETE_WINDOW", hideChatLog)

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
button2 = Button(root,image = img2,border=0, command=showChatLog)
button2.place(x=100, y=10)


#FIle Browser Icon
img4 = PhotoImage(file = 'folder.png')
button4 = Button(root,image = img4,border=00,command = func)
button4.place(x=10, y=630)

#logo but used as a buttons
img5 = PhotoImage(file = 'logo111.png')
labelLogo = Label(root, image = img5)
labelLogo.place(x=680, y=10)

# create list of string
log = []


root.mainloop()