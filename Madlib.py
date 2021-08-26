import random as r

def madlib():
    noun = input("Give me a Name:")
    age = input("Give me a Age:")
    city = input("Give me a City:")
    emo = input("Give me a Emotion:")
    name = input("Give me a name:")

    madlib1 = (f"There once was a man called {noun} he was {age} years old andd lived in {city} he was {emo} about living there but knew as long as {name} stayed wth ")
    madlib2 = (f"A girl named {noun} lived in {city} she was very {emo} about having to move but being {age} and having moeny problems she had no choice but she still had her mom {name}.")
    madlib3 = (f"Once ther was a man that was {age} his name was {noun} and he lived in {city} he was {emo} because {name} just passed")

    randomNumber = r.randint(1,3)

    print(randomNumber)

    if randomNumber <=1:
        print(madlib1)
    elif randomNumber <=2:
        print(madlib2)
    else:
        print(madlib3)
    
madlib()