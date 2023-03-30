import inflect

name_list=[]
while True:
    try:
        name_list.append(input("Name:"))
    except EOFError:
        print("")
        break
p=inflect.engine()
print("Adieu, adieu, to "+p.join(name_list))