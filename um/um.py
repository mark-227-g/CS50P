import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    match = re.findall(r'\b(um)\b',s,re.IGNORECASE)
    if(match) :
        c=len(match)
    else:
        c=0

    return(c)




if __name__ == "__main__":
    main()