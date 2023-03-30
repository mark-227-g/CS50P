import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    plate_pattern = re.compile('[A-Z][A-Z][A-Z]*(([1-9]?)|([1-9])([0-9])*)$')
    r=False
    if((len(s)>=1) & (len(s)<=6) ):
        if(plate_pattern.match(s)):
            r=True

    return(r)


if __name__ == "__main__":
    main()