from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import names
from googletrans import Translator
from pprint import pprint
from nickname_gen.generator import Generator
from nickname_gen.wtypes import WordList, WordType, Lang
from utils.enums import ZodiacSign, Gender, Energy
from algorithm.personality import PersonalityProfile

MONGO_DB = "fastapiapp"
client = MongoClient("mongodb://127.0.0.1:27017")

translator = Translator()
db = client[MONGO_DB]
app = FastAPI()

# my_adjectives = WordList("My Adjectives", Lang.EN, ["cool", "awesome"], WordType.ADJECTIVE)
# my_nouns = WordList("My Nouns", Lang.EN, ["python", "developer"], WordType.NOUN)
# nickname = Generator.get_random_en_nickname(combos=[my_adjectives, my_nouns])
# print("NICKNAME: ", nickname)

# @app.get("/")
# def read_root(gender: Union[str, None] = None):
#     new_name = names.get_full_name()
#     if gender != None:
#         new_name = names.get_full_name(gender=gender)

#         #translation = translator.translate(new_name, src="en", dest="de")
#     #print("TRLT:", translation)
#     return {"name": new_name, "german":"Hello"}


class Persona(BaseModel):
    name: str
    favourite_color: str
    zodiac_sign: ZodiacSign
    age: int
    gender: Gender
    energy: Energy

@app.get("/")
def home():
    return {"message":"Hello World Application"}

@app.post("/")
def  home(request: Persona):
    print("PERSONA: ", request)
    user_profile = PersonalityProfile(name='Alice', zodiac_sign='Leo', favorite_color='Red', age=25, gender='Female', energy='Vibrant')
    return user_profile.profile