with_vowels = input("Input: ")

without_vowels = ""
for c in with_vowels:
    if(c.upper() not in ["A","E","I","O","U"]):
        without_vowels += c
print("output: ", without_vowels)

