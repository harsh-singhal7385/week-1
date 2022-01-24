color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print("\n Result differenct of color_list_1 and color_list_2 are :")

li = []

for i in color_list_1:
    if i in color_list_2:
        pass
    else:
        li.append(i) 

print(li)