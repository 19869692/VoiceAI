import speech_recognition
import pyttsx3

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

names = ["alpha", "bravo", "charlie", "1", "2", "3", "A", "B", "C"]
powerAmount = ["Aft", "Fore", "Port", "Starboard", "Port quarter", "Starboard quarter"]


while True:
    with speech_recognition.Microphone() as mic:
        print("AI Recognition: I'm listening")
        audio = robot_ear.listen(mic)
    try:
        user = robot_ear.recognize_google(audio)  
    except:
        user = ""
    ## robot_brain = "Tug Alpha, pull 5%"
    ## robot_brain = "Tug Alpha, pull 10%"
    ## robot_brain = "Tug Alpha, pull 25%"
    ## robot_brain = "Tug Alpha, pull 50%"
    ## robot_brain = "Tug Alpha, pull 75%"
    ## robot_brain = "Tug Alpha, pull 100%"
    
    print("User: " + user)

    if user == "" :
        robot_brain = "Could you please repeat that!"
    
    elif "hello" in user:
        robot_brain = "Hello user"
    elif "pull" and "50" in user :
        robot_brain = "Tug Alpha, pull 50%"
    elif "pull" and "5" in user:
        robot_brain = "Tug Alpha, pull 5%"
    elif "pull" and "10" in user:
        robot_brain = "Tug Alpha, pull 10%"
    elif "pull" and "25" in user:
        robot_brain = "Tug Alpha, pull 25%"
    elif "pull" and "75" in user:
        robot_brain = "Tug Alpha, pull 75%"
    elif "pull" and "100" in user:
        robot_brain = "Tug Alpha, pull 100%"
    elif "bye" in user:
        robot_brain = "Bye!"
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    
    print("AI Recognition: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
