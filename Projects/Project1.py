'''
Rashad Khan 
Project 1
Completed: 02/19/2023
ID:010713326
'''
#task 1


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

import math
import re


def calc_sin(valueInput):
    accuracy = .000001
    mySin = 0
    testSin = math.sin(valueInput)
    for i in range(0, 10000):
        
        term = (((-1)**(i)) * (valueInput**(2*i+1)) / math.factorial(2*i+1))
        mySin += term
    
        print("\nn:", i+1 , "\nEstimated:",mySin ,"\nTrue:" ,testSin, "\nDifference:",abs(mySin-testSin))
        if abs(mySin-testSin) < accuracy:
            break
    else:
        print("Accuracy not reached.")

def askForPiOrRadian():
    while True:
        inputType= input("Would you like to input x in (pi format) or (radians)? : ")
        if inputType=='radians':
            initialInput = input("Please enter value in radians : ")
            initialInput = float(initialInput)
            return initialInput
        elif inputType== 'pi format':
            initialInput = input("Please input value in pi format : ")
            pattern=  r"(-?\d*\.?\d+)pi"
            initialInput = re.sub(pattern, lambda match: str(float(match.group(1)) * math.pi), initialInput)
            initialInput = initialInput.replace('pi', f'{math.pi}')
            return eval(initialInput)
        else:
            print("Wrong format for input")

 

calc_sin(askForPiOrRadian())

"""
Would you like to input x in (pi format) or (radians)? : pi format
Please input value in pi format : pi/3

n: 1 
Estimated: 1.0471975511965976 
True: 0.8660254037844386 
Difference: 0.18117214741215903

n: 2 
Estimated: 0.8558007815651173 
True: 0.8660254037844386
Difference: 0.0102246222193213

n: 3
Estimated: 0.8662952837868347
True: 0.8660254037844386
Difference: 0.00026988000239613896

n: 4
Estimated: 0.8660212716563725
True: 0.8660254037844386
Difference: 4.132128066047791e-06

n: 5
Estimated: 0.8660254450997811
True: 0.8660254037844386
Difference: 4.131534248053015e-08

-----------------------------------------------------------------------------

Would you like to input x in (pi format) or (radians)? : pi format
Please input value in pi format : -pi/6

n: 1
Estimated: -0.5235987755982988
True: -0.49999999999999994
Difference: 0.02359877559829887

n: 2
Estimated: -0.49967417939436376
True: -0.49999999999999994
Difference: 0.00032582060563618453

n: 3
Estimated: -0.5000021325887924
True: -0.49999999999999994
Difference: 2.1325887925027764e-06

n: 4
Estimated: -0.4999999918690232
True: -0.49999999999999994
Difference: 8.130976725251315e-09

-----------------------------------------------------------------------------

Would you like to input x in (pi format) or (radians)? : pi format
Please input value in pi format : 0.112

n: 1
Estimated: 0.112
True: 0.11176599215128519
Difference: 0.00023400784871481506

n: 2
Estimated: 0.11176584533333334
True: 0.11176599215128519
Difference: 1.4681795185156332e-07

-----------------------------------------------------------------------------

Would you like to input x in (pi format) or (radians)? : pi format
Please input value in pi format : pi

n: 1
Estimated: 3.141592653589793
True: 1.2246467991473532e-16
Difference: 3.141592653589793

n: 2
Estimated: -2.0261201264601763
True: 1.2246467991473532e-16
Difference: 2.0261201264601763

n: 3
Estimated: 0.5240439134171688
True: 1.2246467991473532e-16
Difference: 0.5240439134171687

n: 4
Estimated: -0.07522061590362306
True: 1.2246467991473532e-16
Difference: 0.07522061590362318

n: 5
Estimated: 0.006925270707505135
True: 1.2246467991473532e-16
Difference: 0.006925270707505013

n: 6
Estimated: -0.00044516023820921277
True: 1.2246467991473532e-16
Difference: 0.00044516023820933523

n: 7
Estimated: 2.1142567558399565e-05
True: 1.2246467991473532e-16
Difference: 2.11425675582771e-05

n: 8
Estimated: -7.727858894306387e-07
True: 1.2246467991473532e-16
Difference: 7.727858895531034e-07

-------------------------------------------------------------------------

Would you like to input x in (pi format) or (radians)? : pi format
Please input value in pi format : pi/2

n: 1
Estimated: 1.5707963267948966
True: 1.0
Difference: 0.5707963267948966

n: 2
Estimated: 0.9248322292886504
True: 1.0
Difference: 0.07516777071134961

n: 3
Estimated: 1.0045248555348174
True: 1.0
Difference: 0.004524855534817407

n: 4
Estimated: 0.9998431013994987
True: 1.0
Difference: 0.00015689860050127624

n: 5
Estimated: 1.0000035425842861
True: 1.0
Difference: 3.542584286142514e-06

n: 6
Estimated: 0.999999943741051
True: 1.0
Difference: 5.625894905492146e-08

-------------------------------------------------------

Would you like to input x in (pi format) or (radians)? : radians
Please enter value in radians : .45

n: 1
Estimated: 0.45
True: 0.43496553411123023
Difference: 0.015034465888769777

n: 2
Estimated: 0.4348125
True: 0.43496553411123023
Difference: 0.00015303411123024357

n: 3
Estimated: 0.4349662734375
True: 0.43496553411123023
Difference: 7.393262697608094e-07

--------------------------------------------------------------------------

Would you like to input x in (pi format) or (radians)? : radians
Please enter value in radians : .56

n: 1
Estimated: 0.56
True: 0.5311861979208834
Difference: 0.028813802079116657

n: 2
Estimated: 0.5307306666666667
True: 0.5311861979208834
Difference: 0.00045553125421671226

n: 3
Estimated: 0.5311896098133333
True: 0.5311861979208834
Difference: 3.4118924499004777e-06

n: 4
Estimated: 0.5311861830378382
True: 0.5311861979208834
Difference: 1.4883045240665638e-08
"""