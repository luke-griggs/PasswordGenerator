import random

def randnum():
    min = 1
    max = 10
    randnum = random.randint(min, max)
    return randnum

def randUpperChar():
    randchar = chr(random.randint(65, 90))
    return randUpperChar

def randLowerChar():
    randLowerChar = chr(random.randint(97, 122))
    return randLowerChar

def randSymbol():
    Symbols = "!@#$%?"
    randSymbol = random.choice(Symbols)
    return randSymbol



    