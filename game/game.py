import random

while True:
    try:
        level=int(input("Level:"))
        if(level>0):
            break
    except:
        pass

correct_number=int(random.randint(1,level))

while True:
    try:
        guess=int(input("Guess:"))
        if(correct_number<guess):
            print("Too large!")
        elif(correct_number>guess):
            print("Too small!")
        else:
            print("Just right!")
            break
    except:
        pass
