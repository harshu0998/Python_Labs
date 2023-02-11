'''
Rashad Khan 
LAB 2 
Completed: 02/05/2023
ID:010713326
'''

#Task 1

previous_value, interval, years= input("Please enter a Previous value, Interval, and Year value to recieve your Future value: \n").split()
# takes 3 inputs in specific order all at once.
previous_value= float(previous_value)
interval= float(interval)
years=int(years)
#converts data input from a string to float/int.
temp= interval/100
temp= temp+1
temp= temp**years
future_value= temp*previous_value
future_value= round(future_value, 2)
#Does equation fv=pv((1+(int/100))**yrs) then rounds to the second digit.
print("Your future value is: ",future_value , "\n")
#Outputs future value.

'''
Please enter a Previous value, Interval, and Year value to recieve your Future value: 
23.4 5.6 20  
Your future value is:  69.58
''' 


#task 2 a
v1 = 5
v2 = 2
v3 = 1
#initialize values
v1+=1
v2-=1
v3+=(v1*(v2))
#makes changes to values
print('v1:',v1,'\nv2:',v2,'\nv3:',v3)
#prints new numbers

'''
v1: 6 
v2: 1 
v3: 7

'''

#task 2 b
first, second, third= input('\nPlease enter three values\n').split()
#takes three inputs at once
int(first), int(second), int(third)
#converts to int
(first,second,third)=(second,third,first)
#tuples values
print('first:',first,'\nsecond:',second,'\nthird:',third,'\n')
#prints new values

'''
Please enter three values
12 45 78
first: 45 
second: 78
third: 12
'''
#Wrote code base off of example and not text
#text seemed to have typo claiming first=second second=first third=origional_first
#I wrote it as first=second second=third and third=origional_first (Based of off example)


#task 3
num1,num2=input('Enter the value of num1 and num2: ').split()
#takes two values at once
num1=int(num1)
num2=int(num2)
#converts into integers (unsure why I couldnt just do int(num1), int(num2))
quotient=num1//num2
remainder= num1%num2
#Gets quotient and remainder
print('Quotient when', num1, '/',num2,'is:',quotient)
#prints quotient
print('Remainder when', num1, 'is divided by',num2,'is:',remainder)
#prints remainder

'''
Enter the value of num1 and num2: 12 5
Quotient when 12 / 5 is: 2
Remainder when 12 is divided by 5 is: 2
'''
