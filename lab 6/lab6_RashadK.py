"""
Rashad Khan
010713326
CS2520-01
Lab 6
03/10/2023
"""
import random

#task 1

split_str=input("Please enter a phrase : ").split()
for i in split_str:
    print (i)
concat_with_hash = "#"
concat_with_hash = concat_with_hash.join(split_str)
print(concat_with_hash)

"""
Please enter a phrase : hello there human
hello
there
human
hello#there#human
"""

#task 2

print("part 1")
def add_to_list(list = []):

    next = input("enter an int : ")
    while next.isdigit():
        #if number append
        list.append(int(next))
        next = input("enter the next int : ")
    else:
        #not a number, doesnt append
        return list

list1 = []
list1 = add_to_list(list1)
print(list1)


print("part 2")
list2 = [0]*20
#array length 20
for i in range(0, len(list2)):
    list2[i] = random.randint(0,50)
    #store random number from 0-50
print(list2)

print("part 3")
print(list1[len(list1)-1])
list3 = []
for i in range(len(list1)-1,0,-1):
    #reverse order 
    list3.append(list1[i])
    #store in list 3
print(list3)

print("part 4")
list4 = list1+list2
#combines list 1 and 2
list4.sort()
#sorts
list4.reverse()
#reverse order
print(list4)

"""
part 1
enter an int : 2
enter the next int : 3
enter the next int : 4
enter the next int : 5
enter the next int : 6
enter the next int : f
[2, 3, 4, 5, 6]
part 2
[50, 31, 28, 25, 22, 43, 4, 46, 34, 18, 40, 13, 32, 6, 27, 0, 27, 4, 28, 41]
part 3
6
[6, 5, 4, 3]
part 4
[50, 46, 43, 41, 40, 34, 32, 31, 28, 28, 27, 27, 25, 22, 18, 13, 6, 6, 5, 4, 4, 4, 3, 2, 0]
"""

#task 3

names = ["Winny", "Ada", "Lev", "Kay", "Jack", "Sam", "Mark"]
ages = [20, 18, 22, 16, 20, 18, 18]

zipped_tuple = tuple(zip(names, ages))

print("part 1\n", zipped_tuple)

youngest = min(zipped_tuple, key= lambda a : a[1])
youngest = youngest[0]
#name of the youngest person

ages = [x[1] for x in zipped_tuple]
sum_age = 0
for i in ages:
    sum_age = sum_age + i
len_age = len(ages)
average = sum_age/len_age
#calculate the average age

print("part 2")
print("Youngest person:", youngest)
print("Average age:", average)

sorted = sorted(zipped_tuple, key=lambda x: (-x[1], x[0]))
#sort in age going in reverse order, if tie sort based on name
print("part 3")
print(sorted)

"""
part 1
 (('Winny', 20), ('Ada', 18), ('Lev', 22), ('Kay', 16), ('Jack', 20), ('Sam', 18), ('Mark', 18))
part 2
Youngest person: Kay
Average age: 18.857142857142858
part 3
[('Lev', 22), ('Jack', 20), ('Winny', 20), ('Ada', 18), ('Mark', 18), ('Sam', 18), ('Kay', 16)]
"""


