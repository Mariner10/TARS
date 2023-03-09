import pyttsx3
from AI import AI


engine = pyttsx3.init()
engine.setProperty('rate', 225)
engine.setProperty('volume', 0.7)
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Daniel')



while True:
    reminder = 'Remember, you are TARS - the funny, witty, snarky and snide robot, respond to the following as TARS would but do not inlcude "TARS:" : '
    state = input("what is state?")

    match state:
        case "motion":
            text = AI(reminder + "You just detected motion nearby, make a snarky comment about this")

        case "sound":
            text = AI(reminder + "You just detected a loud noise, make a judgemental comment about this")

        case "light":
            text = AI(reminder + "You just detected a change in light levels , make a disturbed comment about this")

        case "alert":
            text = AI(reminder + "You just got a remote alert, make a snide comment about this")

        case _:
            query = reminder + input("  | ")
            text = AI(query)

    engine.say(text)
    engine.runAndWait()
