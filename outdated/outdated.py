
months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

def print_date(m, d, y):
    d2=str(y)+"-"+f"{m:02}"+"-"+f"{d:02}"
    print(d2)
    return()

def main():
    while True:
        d = input("Date: ")
        d_mdy = d.split("/")
        d_mnamedy = d.split(" ")

        if(d_mdy[0].strip().isnumeric()):
            try:
                m=(int(d_mdy[0].strip()))
                d=(int(d_mdy[1].strip()))
                y=(int(d_mdy[2].strip()))
                if (d<=31) and (m<=12):
                    print_date(m,d,y)
                    break
            except (ValueError,IndexError) :
                pass
        else:
            try:
                m=(months.index(d_mnamedy[0].strip())+1)
                d=(int(d_mnamedy[1].strip()[:-1]))
                y=(int(d_mnamedy[2].strip()))
                if (d<=31) and (m<=12):
                    print_date(m,d,y)
                    break
            except (ValueError,IndexError) :
                pass


main()