from validator_collection import validators, checkers, errors

def main():

    email=input("What's your email address? ")

    if validate_email(email):
        print("Valid")
    else :
        print("Invalid")
def validate_email(s):
    b=False
    try:
        email_address = validators.email(s,allow_empty = False)
        b=True
    except errors.InvalidEmailError:
        b=False

    return(b)

if __name__ == "__main__":
    main()