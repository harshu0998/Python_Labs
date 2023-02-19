'''
Rashad Khan 
Project 1
Completed: 02/19/2023
ID:010713326
'''
#task 1
"""

def notNegativeNotZero(a):
    a=float(a)
    if a <= 0:
        print("Invalid input")
        a=0
        return a
    else:
        return a

def bmiSelectionAndInput ():
    test =True
    while test == True:
        systemCheck = input("Write 1 for USA/English system (Lb,Inches) \nWrite 2 for Metric system (KG,Meters)\n")   
        if systemCheck == '1' or systemCheck == '2':
            test = False
        else:
            print("Invalid input")
    b = 0
    while b == 0:
        weight = notNegativeNotZero(input("Please enter Weight: "))
        b = weight
    if systemCheck == '1':
        weight = weight*703
    b = 0
    while b == 0:
        height = notNegativeNotZero(input("Please enter Height: "))
        b = height
    height = height**2
    return(weight/height)


def main():
    answer = round(bmiSelectionAndInput(),3)
    print("Your BMI is equals to",answer)
    if answer < 18:
        print("You are under weight")
    elif answer>25:
        print("You are overweight")
    else:
        print("You are average weight")

main()

"""
"""
1.)
Write 1 for USA/English system (Lb,Inches) 
Write 2 for Metric system (KG,Meters)
1
Please enter Weight: 155
Please enter Height: 70
Your BMI is equals to 22.238
You are average weight

2.)
Write 1 for USA/English system (Lb,Inches) 
Write 2 for Metric system (KG,Meters)
1
Please enter Weight: 172
Please enter Height: 68
Your BMI is equals to 26.15
You are overweight

3.)
Write 1 for USA/English system (Lb,Inches) 
Write 2 for Metric system (KG,Meters)
2
Please enter Weight: 75
Please enter Height: 1.83
Your BMI is equals to 22.395
You are average weight

4.)
Write 1 for USA/English system (Lb,Inches) 
Write 2 for Metric system (KG,Meters)
2
Please enter Weight: 51.5
Please enter Height: 1.68
Your BMI is equals to 18.247
You are average weight

5.)
Write 1 for USA/English system (Lb,Inches)
Write 2 for Metric system (KG,Meters)
1
Please enter Weight: 150
Please enter Height: 69
Your BMI is equals to 22.149
You are average weight

6.)
Write 1 for USA/English system (Lb,Inches) 
Write 2 for Metric system (KG,Meters)
2
Please enter Weight: 80
Please enter Height: 2.3
Your BMI is equals to 15.123
You are under weight

7&8.)
#I mixed 7 and 8 because I designed the program to keep asking for inputs untill a proper numerical input is given
Write 1 for USA/English system (Lb,Inches) 
Write 2 for Metric system (KG,Meters)
123
Invalid Input
Write 1 for USA/English system (Lb,Inches)
Write 2 for Metric system (KG,Meters)
2
Please enter Weight: 0
Invalid input
Please enter Weight: -1
Invalid input
Please enter Weight: 70
Please enter Height: 0
Invalid input
Please enter Height: -1
Invalid input
Please enter Height: 2.1 
Your BMI is equals to 15.873
You are under weight
"""


#task2