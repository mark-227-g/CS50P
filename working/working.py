import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r'^(\d|10|11|12)?(?::)*([0-5][0-9])* (AM|PM) to (\d|10|11|12)?(?::)*([0-5][0-9])* (AM|PM)',s)
    if (match) :

        start_ampm_idx=3
        end_hour_idx=4
        end_min_idx=5
        end_ampm_idx=6

        if((match.group(start_ampm_idx) == "PM") and (int(match.group(1))<12)) :
            start_hour=int(match.group(1))+12
        elif((match.group(start_ampm_idx) == "AM") and (int(match.group(1)) == 12)) :
            start_hour =0
        else :
            start_hour=int(match.group(1))

        if match.group(2) == None :
            start_min=0
        else :
            start_min=int(match.group(2))

        start_time=f"{start_hour:02}"+":"+f"{start_min:02}"

        if((match.group(end_ampm_idx) == "PM") and (int(match.group(end_hour_idx))<12)) :
            end_hour=int(match.group(end_hour_idx))+12
        elif((match.group(end_ampm_idx) == "AM") and (int(match.group(end_hour_idx)) == 12)) :
            end_hour =0
        else :
            end_hour=int(match.group(end_hour_idx))

        if (match.group(end_min_idx)) == None :
            end_min=0
        else :
            end_min=int(match.group(end_min_idx))

        end_time=f"{end_hour:02}"+":"+f"{end_min:02}"

        new_time=start_time+" to "+end_time
        return(new_time)
    else:
        print("here")
        raise ValueError("ValueError")

if __name__ == "__main__":
    main()