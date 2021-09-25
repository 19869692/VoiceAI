import speech_recognition
import pyttsx3

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

tugName = ["alpha", "bravo", "charlie", "1", "2", "3", "A", "B", "C","Aft tug", "Fore tug", "Port tug", "Starboard tug", "Port quarter tug", "Starboard quarter tug"]
tugPower = ["5%", "10%", "25%", "50%", "75%", "100%","minimum", "minimum weight", "bare weight", "quarter Power", "Half Power", "Three Quarters Power", "Full Power"]
tugCommand = ["pull","push", "pull directly astern", "all stop", "move to pull", "move to push", "be ready to pull", "be ready to push", "move to", "square up"]
tugPosition = ["Aft", "Fore, Port", "Starboard", "Port Quarter", "Starboard Quarter"]

while True:
    with speech_recognition.Microphone() as mic:
        print("AI Recognition: I'm listening")
        audio = robot_ear.listen(mic)
    try:
        user = robot_ear.recognize_google(audio)  
    except:
        user = ""
    
    print("User: " + user)

    if tugName in user:
        robot_brain = "This is " + tugName + ", could you repeat that?"
    elif "hello" in user:
        robot_brain = "Hello user"
    elif tugName and tugCommand in user:
        robot_brain = user
    elif tugName and tugCommand and tugPower in user:
        robot_brain = user
    elif tugName and tugCommand and tugName and tugCommand in user:
        robot_brain = user
    elif tugName and tugCommand and tugPosition in user:
        robot_brain = user
    elif tugName and tugCommand and " and " and tugCommand and tugPosition in user:
        robot_brain = user
    elif "bye" in user:
        robot_brain = "Bye!"
    else:
        robot_brain = "Could you please repeat that?"
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    
    print("AI Recognition: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
