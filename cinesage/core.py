from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
model = ChatMistralAI(model = "mistral-small-2506")

prompt_template = ChatPromptTemplate.from_messages([
     ("system", """
You are an AI that extracts structured information from movie descriptions.

Extract the following:
- Movie Name
- Director
- Release Year
- Main Cast
- Plot Summary (short)
- Key Highlights (rating, music, achievements)

Only use the given text. Do not guess.
Return answer in clean readable format (not JSON).
"""),
    ("human", "{input}")
])

while True:
    user_input = input("You: ")

    if user_input == "0":
        break

    # 🔥 format prompt
    prompt = prompt_template.invoke({"input": user_input})

    # 🔥 call model
    result = model.invoke(prompt)

    print("Bot:", result.content)
print(result)