###################
# CS50P Python
# Mark Edwards
# Lesson 1
##################

answer = input("What is the Question of Life, the Universe and Everything? ")

match answer.strip().lower():
    case "42":
        reply = "yes"
    case "forty-two":
        reply = "yes"
    case "forty two":
        reply = "yes"
    case _:
        reply = "No"

print(reply)