# AI SMS

AI chatbot based on OpenAI GPT model that can communicate with you over SMS messaging. I created my personal AI SMS into a robot known as TARS.

TARS is a brash and snarky AI who will converse with you over SMS or even chat with text-to-speech!

> _"Oh, just me, a highly advanced and incredibly charming robot. Who were you expecting, Siri?"_

Believe it or not, TARS has the tendency to associate himself with the character TARS from the movie *Interstellar*, while this robot was never chosen as a role-model or personality, our TARS ***decided*** to associate himself with it anyway.

Plug and play functionality for actions your AI can do and various methods of communication are planned.

## Setup

You will have to go into the ```constants.py``` file and add all of your imformation for it to work correctly, then run either ```AI_SMS.py``` or ```AI_speak.py``` (depreciated) depending on how you want to communicate with the AI.

Then go into your device and start by sending a text to the email you used in setup.

## AI Personalities

You can look at [info.md](TARS/personalities/info.md) for the steps on how to create a custom personality to use with your AI.




## How?

There are 3 main parts to the whole program:

### 1. Receiving SMS as input.

In order to receive SMS to use as input to feed to the AI, I chose to use a IMAP client for mail, because as it turns out - SMS numbers can work as a "email" address by appending a @<insert mail server>.com to it *("@mms.att.net")* for example. So for any given number you can append that address at the end and then send messages as emails to any gmail address.

Go ahead and create a burner gmail address and genereate an app specific password and enable IMAP clients so that the python program is able to communicate with any text messages that come in.

### 2. Detecting new messages and feeding them to the AI:

The program counts your messages *(email)* at all times, whenever a change is detected *(a new message from the provided number appears)*, it feeds the data through a filter to determine if there are any keywords in the text that match specific actions you want the program to do instead of contacting the AI. If the data doesn't catch any filters then it will be passed strait to the AI, who will respond according to your personality customisation, and issue a response.

### 3. Response:

Using the phone number provided, by appending the aforementioned carrier adresses to the end of the number, we are able to send an email, *(SMS)* back to the number, which shows up in whatever SMS device origianlly contacted the AI. Oddly enough the timing of when this message actually makes it back to the device is ***EXTREMELY*** variable which makes no sense and thus makes this the bottleneck of the program.
