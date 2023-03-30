grocery_list = {}

while True:
    try:
        item = (input()).upper()
        try:
            grocery_list[item] = int(grocery_list[item])+1
        except KeyError:
            grocery_list[item] = 1
    except EOFError:
        grocery_list_sorted = sorted(grocery_list)
        for i in grocery_list_sorted:
            print(grocery_list.get(i),i)
        break