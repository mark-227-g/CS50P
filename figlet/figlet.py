import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if(len(sys.argv)==1):
    fontname = random.choice(figlet.getFonts())
    try:
        figlet.setFont(font=fontname)
    except :
        sys.exit("Invalid usage")
elif(len(sys.argv)==3):
    if((sys.argv[1] != "-f") and (sys.argv[1] != "--font")):
        sys.exit("Invalid usage")
    else:
        try:
            figlet.setFont(font=sys.argv[2])
        except :
            sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

input_text = input("Input:")
print(figlet.renderText(input_text))
