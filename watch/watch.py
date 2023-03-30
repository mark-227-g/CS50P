import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    match=re.search(r'<iframe (?:.)*(?:src="(?:(?:http|https)://(?:www.)*youtube.com/embed/)([a-z_A-Z__0-9]+))"(?:.)*></iframe>',s,re.IGNORECASE)
    if match :
        return("s"+match.group(1))
    else:
        return(None)

if __name__ == "__main__":
    main()