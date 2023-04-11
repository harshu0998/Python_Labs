"""
Rashad Khan
010713326
CS2520-01
Lab 8
04/10/2023
"""


print("Q1")
q1 = open("Q1.txt", "r")
page_lines_q1_1 = q1.readlines()
print("part 1")
print(page_lines_q1_1[0], end = "")
print(page_lines_q1_1[2], end = "")
q1.close()

print("part 2")
q1 = open("Q1.txt", "r")
page_lines_q1_2 = list([])
for newline in q1:
   page_lines_q1_2.append(newline)
print(page_lines_q1_2[1], end = "")
print(page_lines_q1_2[3], end = "")

q1.close()

"""
Q1
part 1
We can't touch
We hunker down
part 2
But we still reach out
But we still rise up
"""




print("\n\nQ2")
fp=open('data1.txt', 'w')
fp.write("hello\t")
fp.write("how are you")
fp.write("\n")
fp.write("thank you ")
fp.write("bye\n")
fp.close()

print("data1.txt context")
q2= open("data1.txt","r")
q2_list1 = q2.readlines()
print(q2_list1)
q2.close()

fp=open('data2.txt', 'w')
fp.writelines(["hello\t", "how are you", "\n", "thank you ", "bye\n"])
fp.close()

print("data2.txt context")
q2= open("data2.txt","r")
q2_list2 = q2.readlines()
print(q2_list2)
q2.close()
print("Are the two files the same? ",q2_list1 == q2_list2)

"""
Q2
data1.txt context
['hello\thow are you\n', 'thank you bye\n']
data2.txt context
['hello\thow are you\n', 'thank you bye\n']
Are the two files the same?  True
"""


print("\nQ3")
while True:
    userInput= input("Please enter a file name (i.e. Q3.txt):  ")

    try:
        q3= open(userInput, "r")
    except FileNotFoundError:
        print("File not found")
        continue
    q3_list = []
    for newline in q3:
        try:
            q3_list.append((format((float(newline)),'.1f')))
        except ValueError:
            q3_list.append(0.0)
    print(q3_list)
    break

"""
Q3
Please enter a file name (i.e. Q3.txt):  Q3.txt
['102.0', '20.5', 0.0, 0.0, '30.2', '12.0', '23.4',
 '45.5', '34.0', '78.0', '67.0', '58.0', 0.0, '34.2',
 '345.0', '987.0', '76.0', '54.0', '18.6', '25.4']
"""

