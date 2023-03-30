import sys

def main():

    if(len(sys.argv)==1):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv)>2):
        sys.exit("Too many command-line arguments")
    else:
        filename=sys.argv[1]
        f=filename.split('.')
        if(f[len(f)-1].lower() != "py"):
            sys.exit("Not a Python file")
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except(FileNotFoundError):
        sys.exit("File does not exist")

    count=0
    for line in lines:
        if(line.lstrip()==""):
            pass
        elif(line.lstrip().startswith("#")):
            pass
        else:
            count += 1

    print(count)

    file.close()





if __name__ == "__main__":
    main()