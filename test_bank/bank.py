def main():
    v = value(input("Greeting: "))
    print(v)

def value(greeting):
    if greeting.lower().strip()[0:5]=="hello":
        return(0)
    elif greeting[0:1].lower().strip()=='h':
        return(20)
    else :
        return(100)

if __name__ == "__main__":
    main()