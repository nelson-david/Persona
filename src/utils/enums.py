from enum import Enum

class ZodiacSign(str, Enum):
    aries = "Aries"
    taurus = "Taurus"
    gemini = "Gemini"
    cancer = "Cancer"
    leo = "Leo"
    virgo = "Virgo"
    libra = "Libra"
    scorpio = "Scorpio"
    sagittarius = "Sagittarius"
    capricorn = "Capricorn"
    aquarius = "Aquarius"
    pisces = "Pisces"

class Gender(str, Enum):
    male = "male"
    female = "female"

class Energy(str, Enum):
    cool = "cool"
    awesome = "awesome"
    angered = "angered"
    happy = "happy"
    vibrant = "vibrant"