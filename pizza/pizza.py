import sys
import csv
from tabulate import tabulate

def main():

    if(len(sys.argv)==1):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv)>2):
        sys.exit("Too many command-line arguments")
    else:
        filename=sys.argv[1]
        f=filename.split('.')
        if(f[len(f)-1] != "csv"):
            sys.exit("Not a CSV file")

    menu = []

    try:
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                menu.append(row)
            csvfile.close()
    except(FileNotFoundError):
        sys.exit("File does not exist")

    print(tabulate(menu,headers="keys",tablefmt="grid"))

if __name__ == "__main__":
    main()