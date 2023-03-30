def main():

    without_vowels = shorten(input("Input: "))
    print("output: ", without_vowels)

def shorten(word):
    without_vowels=""
    for c in word:
        if(c.upper() not in ["A","E","I","O","U"]):
            without_vowels += c
    return(without_vowels)





if __name__ == "__main__":
    main()