import sys
import csv

def main():

    if(len(sys.argv)<=2):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv)>3):
        sys.exit("Too many command-line arguments")
    else:
        filename_before=sys.argv[1]
        f=filename_before.split('.')
        if(f[len(f)-1] != "csv"):
            sys.exit("Not a CSV file")
        filename_after=sys.argv[2]
        f=filename_after.split('.')
        if(f[len(f)-1] != "csv"):
            sys.exit("Not a CSV file")

    students = []

    try:
        with open(filename_before) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(row)
            csvfile.close()
    except(FileNotFoundError):
        sys.exit("Could not read "+filename_before)

    with open(filename_after, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last", "house"])
        writer.writeheader()
        for student in students:
            name=student["name"].split(',')
            first=name[1].strip()
            last=name[0].strip()
            writer.writerow({"first":first,"last":last, "house":student["house"]})
        file.close()
if __name__ == "__main__":
    main()