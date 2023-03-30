
while(True):
    input_fraction= input("Fraction: ")
    f = input_fraction.split('/')



    if (f[0].isnumeric()) and (f[1].isnumeric()):
        try:
            x=int(f[0])
            y=int(f[1])
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if (y!=0) and (y>=x):
                amt_full = int(x)/int(y)
                if(amt_full <= .01):
                    print("E")
                elif(amt_full>=.99):
                    print("F")
                else:
                    print(f"{amt_full:.0%}")
                break
