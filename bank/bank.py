###################
# CS50P Python
# Mark Edwards
# Lesson 1
##################

h = input("Greeting: ")
if h.strip()[0:5]=="Hello":
    print("$0")
elif h[0:1].strip()=='H':
    print("$20")
else :
    print("$100")