foods = ['ham', 'toast', 'spam', 'bacon', 'spinach']

#for food in foods:
#    print(food, "and eggs")


def before_and_after(list, before, after):
    full_list = []
    for i in list:
        string = before, i, after
        full_list.append(string)

    return full_list


menu = before_and_after(foods, "Would you like ", " and eggs?")
for item in menu:
    print(item)
