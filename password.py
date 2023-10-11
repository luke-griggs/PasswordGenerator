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

ten_char_password = " "

e = 0
while e < 10:
    ten_char_password += rand_char()
    e += 1

user_selection = input("would you like an 8 or 10 character password?")
temp = int(user_selection)
if temp == 8:
    print(f"your generated password is{eight_char_password}")
elif temp == 10:
    print(f"your generated password is{ten_char_password}")


    

    