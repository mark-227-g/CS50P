import random

def main():
    score=0
    level=get_level()

    problems={}

    while True:
        x=generate_integer(level)
        y=generate_integer(level)
        problem_key=str(x)+" + "+str(y)+" ="
        if(problem_key not in problems):
            problems[problem_key]=create_list(x,y)
        if len(problems)==10:
            break

    for p,n in problems.items():
        if solve_problem(p,n[0],n[1]):
            score+=1
    print("Score:",str(score))

def create_list(x,y):
    l=list()
    l.append(x)
    l.append(y)
    return(l)

def solve_problem(problem,x,y):
    correct=False
    answer=x+y
    for i in range(3):
        try:
            guess=int(input(problem))
            if guess == answer:
                correct=True
                break
            else:
                if i==2 :
                    print(problem+str(answer))
                    break
                else:
                    print("EEE")
        except ValueError:
            print("EEE")
    return(correct)

def get_level():
   while True:
    try:
        level=int(input("Level: "))
        if(level in (1,2,3)):
            return(level)
    except:
        pass

def generate_integer(level):
    match int(level):
        case 1:
            r=int(random.randint(0,9))
        case 2:
            r=int(random.randint(10,99))
        case 3:
            r=int(random.randint(100,999))
    return(r)

if __name__ == "__main__":
    main()

