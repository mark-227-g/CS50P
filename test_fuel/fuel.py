
def main():

    f = convert(input("Fraction: "))
    print(gauge(f))

def convert(fraction):
    f = fraction.split('/')
    try:
        x=int(f[0])
        y=int(f[1])
    except (ValueError):
        raise ValueError("Value Error")

    if(y==0):
        raise ZeroDivisionError("ZeroDivisionError")
    if(x>y):
        raise ValueError("Value Error")
    return(round((x/y)*100))

def gauge(percentage):
    r=""
    if(percentage <= 1):
        r="E"
    elif(percentage>=99):
        r="F"
    else:
        r=(f"{percentage}%")
    return(r)

if __name__ == "__main__":
    main()