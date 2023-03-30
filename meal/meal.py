###################
# CS50P Python
# Mark Edwards
# Lesson 1
##################

def main():
    t = convert(input("What time is it? "))

    if(t>=(7.00) and (t<=8)):
        meal="breakfast time"
    elif(t>=(12.00) and (t<=13)):
        meal="lunch time"
    elif(t>=(18.00) and (t<=19)):
        meal="dinner time"

    if("meal" in locals()):
        print(meal)

def convert(time):
    h,m= time.split(':')
    return(int(h)+(int(m)/60))


if __name__ == "__main__":
    main()
