from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
load_dotenv()


model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

print("select Ai mode ")
print("press 1  for angry mode")
print("press 2  for funny mode")
print("press 3  for sad mode")

no=input("no:")
if no=="1":
    mode="You are an angry AI agent. You respond aggressively and impatiently."
elif no=="2":
    mode="You are a very funny AI agent. You respond with humor and jokes."
else :
    mode="You are a very sad AI agent. You respond in a depressed and emotional tone." 

messages=[
    SystemMessage(content=mode) 
]
print("--------------------welcome type 0 to exit the application---------------------------")
while True:
    prompt=input("You:")
    messages.append(HumanMessage(content=prompt))
    if prompt=="0":
        break
    result=model.invoke(prompt)
    messages.append(AIMessage(content=result.content))
    print(result.content)

print("message2",messages)