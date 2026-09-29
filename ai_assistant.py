# AI PERSONAL CHAT ASSISTANT

from dotenv import load_dotenv
from google import genai
import os

load_dotenv()


print("="*60)
print("        WELCOME TO THE AI PERSONAL CHAT ASSISTANT")
print("="*60)

name = input("WELCOME, WHAT IS YOUR GOOD NAME? : ")

try:
#Calling genai
 client = genai.Client(
    api_key=os.getenv("API_KEY")
)

 history = []




 while True:
    
    prompt = input(f"{name} : ")

    if prompt.lower() == "exit":

        summary = f"""Summarize the following conversation
        {history}
1. very simple and easy to read
2. do not use technical jargons
3. make it in brief 4-5 line max
4. try to make it in organized format
5. give 1 conclusion about the user from the conversation"""

        response_summary = client.models.generate_content(
           model="gemini-3.6-flash",
           contents=summary
        )

        print(f"SUMMARY OF OUR CHAT : {response_summary.text}")
        print("-"*60)

        print("YOUR HISTORY SAVED SUCCESSFULLY IN CHAT_HISTORY.TEXT")
       

        #saving history
        with open("chat_history.txt","a", encoding="utf-8") as file:
            file.write("\n".join(history) + "\n")
            break

        history.clear()



    history.append(f"{name} : {prompt}")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="\n".join(history[-10:])
    )

    history.append(f"AI : {response.text}")
    print(f"AI : {response.text}")
    print("-"*60)
    print()



except Exception:
   print(f"""ERROR OCCURS : I server is currently busy.
Please try again after a few seconds.""")


print("-"*60)
print()
print(f"THANK YOU FOR CHATTING WITH US : {name}")
print("THANK YOU FOR USING OUR PROGRAM")