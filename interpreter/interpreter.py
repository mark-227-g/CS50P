###################
# CS50P Python
# Mark Edwards
# Lesson 1
##################

math = input("Expression: ")
x, y, z = math.split(" ")

match(y):
    case '+':
        r = float(x) + float(z)
    case '-':
        r = float(x) - float(z)
    case '/':
        r = float(x) / float(z)
    case '*':
        r = float(x) * float(z)

print("{:.1f}".format(r))
