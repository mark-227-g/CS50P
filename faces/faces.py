###################
# CS50P Python
# Mark Edwards
# Lesson 0
##################

def convert(s):
    s = s.replace(":)","🙂")
    s = s.replace(":(","🙁")
    return s

def main():
    sName = input()
    sName = convert(sName)
    print(sName)

if __name__ == "__main__":
    main()