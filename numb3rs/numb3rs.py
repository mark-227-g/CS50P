import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if (re.search(r"^((1?\d?\d|2[0-4]\d|25[0-5])\.){3}(1?\d?\d|2[0-4]\d|25[0-5])$",ip)):
        return True
    else :
        return False

if __name__ == "__main__":
    main()