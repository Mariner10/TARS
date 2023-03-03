import openai
from constants import openAI_ORG,openAI_privKey

openai.organization = openAI_ORG
openai.api_key = openAI_privKey



def TARS(userInput):
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.8,

    messages=[
        {"role": "user", "content": userInput}
    ] 
    )

    return completion.choices[-1].message.content


    