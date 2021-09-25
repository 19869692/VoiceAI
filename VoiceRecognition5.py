import speech_recognition
import pyttsx3
import PyAudio

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

tugName = ["alpha", "bravo", "charlie", "1", "2", "3", "A", "B", "C","Aft tug", "Fore tug", "Port tug", "Starboard tug", "Port quarter tug", "Starboard quarter tug"]
tugPower = ["5%", "10%", "25%", "50%", "75%", "100%","minimum", "minimum weight", "bare weight", "quarter Power", "Half Power", "Three Quarters Power", "Full Power"]
#tugCommand = ["pull","push", "pull directly astern", "all stop", "move to pull", "move to push", "be ready to pull", "be ready to push", "move to", "square up"]
#tugPosition = ["Aft", "Fore, Port", "Starboard", "Port Quarter", "Starboard Quarter"]

while True:
    with speech_recognition.Microphone() as mic:
        print("AI Recognition: I'm listening")
        audio = robot_ear.listen(mic)
    try:
        user = robot_ear.recognize_google(audio)  
    except:
        user = ""
    
    print("User: " + user)

#    if names in user:
#        robot_brain = "This is " + names + ", could you repeat that?"
    if "hello" in user:
        robot_brain = "Hello user"
    elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power" and "Three Quarters Power" and "Full Power" in user:
        robot_brain = user
#    elif tugName and tugCommand and tugPower in user:
#        robot_brain = user
#    elif tugName and tugCommand and tugName and tugCommand in user:
#        robot_brain = user
#    elif tugName and tugCommand and tugPosition in user:
#        robot_brain = user
#    elif tugName and tugCommand and " and " and tugCommand and tugPosition in user:
#        robot_brain = user
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
