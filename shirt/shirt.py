import sys
import os
from PIL import Image
from PIL import ImageOps

def main():

    if(len(sys.argv)<=2):
        sys.exit("Too few command-line arguments")
    elif(len(sys.argv)>3):
        sys.exit("Too many command-line arguments")
    else:
        filename1 = sys.argv[1].lower()
        filename2 = sys.argv[2].lower()
        if not (os.path.exists(filename1)):
            sys.exit("File does not exist")
        if not (is_image_file(filename1)):
            sys.exit("Invalid input")
        if not (is_image_file(filename2)):
            sys.exit("Invalid input")
        if not (compare_ext(filename1,filename2)):
            sys.exit("Input and output have different extensions")

    try:
        shirt=Image.open("shirt.png", mode='r', formats=None)

        photo=Image.open(filename1, mode='r', formats=None)
        photo2=ImageOps.fit(photo,(shirt.width,shirt.height))
        photo2.paste(shirt, (0,0), mask = shirt)

        photo2.save(filename2, format=None)
    except(FileNotFoundError):
        sys.exit("File does not exist")



def is_image_file(filename):
    ext=os.path.splitext(filename)
    if(ext[1] in (".png",".jpg",".jpeg")):
        return(True)
    else:
        return(False)

def compare_ext(filename1,filename2):
    ext1=os.path.splitext(filename1)
    ext2=os.path.splitext(filename2)
    if(ext1[1]==ext2[1]):
        return(True)
    else:
        return(False)

if __name__ == "__main__":
    main()