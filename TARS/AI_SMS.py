from AI import AI
from smsGmail import send_message
from fetchGmail import thisWholdThingIsAFunction
from constants import SMS_number,mobile_carrier,debug_mode,AI_Name,your_name,reminder,query,restart_mood,wake_up_mood
import os
import sys


if debug_mode == True: print("| Debug mode is set to TRUE ~ you can change this by setting `debug_mode` to FALSE |")


# AI setup.
if debug_mode == True: print("Querying " + AI_Name + "...")
starting_remarks = AI(query)
if debug_mode == True: print(AI_Name + " says: " + starting_remarks)
if debug_mode == True: print("\n" + AI_Name + " text and personality calibrated...")


# Arg handling.
if len(sys.argv) > 1:
    arg1 = sys.argv[1]
else:
    arg1 = ''

def sendSMS(string):
    string = string.strip()
    print(AI_Name + "- " + string)
    send_message(SMS_number,mobile_carrier,string)

sendSMS("[System Online]")
if arg1 == "-w":
    sendSMS(AI(reminder + wake_up_mood))


if debug_mode == True: print("Getting Mail details...")
item = thisWholdThingIsAFunction()
if debug_mode == True: print("\nDone!\n")

try:
    splitedItem = item.split("/|/")
    InitialnumMail = splitedItem[0]
except AttributeError:
    InitialnumMail = 0
    if debug_mode == True: print("     |Mail count set to zero.")


if debug_mode == True: print("Setup complete & ready for SMS requests")
while True:

    item = thisWholdThingIsAFunction()
    try:
        splitedItem = item.split("/|/")
        numMail = splitedItem[0]
    except AttributeError:
        numMail = 0
        if debug_mode == True: print("     |No new mail found.")
    
    FinalnumMail = numMail
    
    if int(InitialnumMail) < int(FinalnumMail):
        query = splitedItem[1]
        if "Override:" in query:
            if debug_mode == True: print("|Override Request|")
            if "restart" in query:
                sendSMS(AI(restart_mood))
                sendSMS("SYSTEM_SHUTDOWN")
                if debug_mode == True: print("Restarting")
                if debug_mode == True: print(sys.executable, ['python3'] + sys.argv)
                os.execv(sys.executable, ['python3'] + sys.argv + ['-w'])

            elif "Other action" in query:
                sendSMS("configurable action!")
                
            
        else:
            print(your_name + "- " + query)
            text = AI(reminder + query)
            sendSMS(text)
        
    InitialnumMail = FinalnumMail