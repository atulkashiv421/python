import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',150)

def speak(text):
    engine.say(text)
    
    engine.runAndWait()

name = int(input("Enter your age: "))

if(name%2==0):
    message = "this is even"
    print(message)
    

if(name==0):
    message = "no it is not possible"
    print(message)
    speak(message)
elif(name<0):
    message ="thisa is not valid"
    print(message)
    speak(message)
elif(name>18):
    message = "you are not teenager"
    print(message)
    speak(message)
else:
    message = "you are not teenager"
    print("End of the program")
    speak(message)

