from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic  import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class Movie(BaseModel):
    title:str
    release_year:Optional[int]
    genre:List[str]
    director:Optional[str]
    cast:List[str]
    rating:List[float]
    summary:str

parser=PydanticOutputParser(pydantic_object=Movie) # this is use for check the movie all value are fill properly 
model = ChatMistralAI(model = "mistral-small-2506")

prompt_template = ChatPromptTemplate.from_messages([
     ('system',"""
Extract movie information from the paragraph
     {format_instructions}
"""),
("human","{paragraph}")
])

while True:
    user_input = input("You: ")

    if user_input == "0":
        break

    # 🔥 format prompt
    prompt = prompt_template.invoke({"paragraph": user_input,"format_instructions":parser.get_format_instructions()})

    # 🔥 call model
    result = model.invoke(prompt)

    print("Bot:", result.content)
print(result)