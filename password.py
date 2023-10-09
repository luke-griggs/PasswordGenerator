import random

def randnum():
    min = 1
    max = 10
    randnum = random.randint(min, max)
    return str(randnum)

def randUpperChar():
    randUpperChar = chr(random.randint(65, 90))
    return str(randUpperChar)

def randLowerChar():
    randLowerChar = chr(random.randint(97, 122))
    return str(randLowerChar)

def randSymbol():
    Symbols = "!@#$%?"
    randSymbol = random.choice(Symbols)
    return str(randSymbol)

def rand_char():
    num = random.randint(1, 4)
    if num == 1:
        return randnum()
    elif num == 2:
        return randUpperChar()
    elif num == 3:
        return randLowerChar()
    else:
        return randSymbol()
       
eight_char_password = " "

i = 1
while i < 9:
    eight_char_password += rand_char() 
    i += 1  

test = eight_char_password
print(test)


    

    