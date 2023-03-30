###################
# CS50P Python
# Mark Edwards
# Lesson 2
##################

camel_case = input("camelCase: ")

snake_case = ""
for c in camel_case:
    if(c == c.upper()):
        snake_case += "_"
    snake_case += c.lower()




print("snake_case: ", snake_case)
