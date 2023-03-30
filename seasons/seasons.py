from datetime import datetime
from datetime import date
import inflect
import sys

def main():
    try:
        birthday = datetime.fromisoformat(input ("Date of Birth: "))
    except:
        sys.exit("Invalid Date")

    minutes = number_minutes_from_today(birthday)
    print(format_number_words(minutes),"minutes")

def number_minutes_from_today(dt):
    t =  datetime.combine(date.today(), datetime.min.time())
    diff = t - dt
    return(round(diff.total_seconds()/60))

def format_number_words(minutes):
    p=inflect.engine()
    return ((p.number_to_words(minutes,andword="")).capitalize())

if __name__ == "__main__":
    main()