import speech_recognition
import pyttsx3


robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

#tugName = ["alpha", "bravo", "charlie", "1", "2", "3", "A", "B", "C","Aft tug", "Fore tug", "Port tug", "Starboard tug", "Port quarter tug", "Starboard quarter tug"]
#tugPower = ["5%", "10%", "25%", "50%", "75%", "100%","minimum", "minimum weight", "bare weight", "quarter Power", "Half Power", "Three Quarters Power", "Full Power"]
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

    if "hello" in user:
        robot_brain = "Hello user"
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" in user:
        robot_brain = user
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power"and "Three Quarters Power" and "Full Power" in user:
        robot_brain = user
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power"and "Three Quarters Power" and "Full Power" + "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power"and "Three Quarters Power" and "Full Power" in user:
        robot_brain = user
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "5%" and "10%" and "25%" and "50%" and "75%" and "100%" and "minimum" and "minimum weight" and "bare weight" and "quarter Power" and "Half Power"and "Three Quarters Power" and "Full Power" + "Aft" and "Fore, Port" and "Starboard" and "Port Quarter"and "Starboard Quarter" in user:
        robot_brain = user
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "alpha" and "bravo" and "charlie" and "1" and "2" and "3" and "A" and "B" and "C" and "Aft tug" and "Fore tug" and "Port tug" and "Starboard tug" and "Port quarter tug" and "Starboard quarter tug" + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + " and " + "pull" and "push" and "pull directly astern" and "all stop" and "move to pull" and "move to push" and "be ready to pull" and "be ready to push" and "move to" and "square up" + "Aft" and "Fore, Port" and "Starboard" and "Port Quarter"and "Starboard Quarter" in user:
        robot_brain = user
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    elif "bye" in user:
        robot_brain = "Bye!"
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
    else:
        robot_brain = "Could you please repeat that?"
        print("AI Recognition: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    
    print("AI Recognition: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
