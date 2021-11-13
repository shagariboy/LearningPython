#reverses the elements in list
my_list = [] #creates an empty list
for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)    



#sums the elements in list

new_list = [10, 2, 4, 6, 8]
total = 0

for i in new_list:
    total += i

print(total)
        

#reverses the order of list elements

old_list = [1, 2, 3, 4, 5]
old_list[0], old_list[4] = old_list[4], old_list[0]
old_list[1], old_list[3] = old_list[3], old_list[1]

print(old_list)


#reverses the order of list elements(using for loop)
anoti_list = [1, 2, 3, 4, 5]
length = len(anoti_list)

for i in range(length // 2):
    anoti_list[i], anoti_list[length - i - 1] = anoti_list[length - i -1], anoti_list[i]

print(anoti_list)    


