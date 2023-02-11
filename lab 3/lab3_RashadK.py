'''
Rashad Khan
02/10/2023
Lab 3
ID: 010713326
'''



#Task 1.1, 1.2, 1.3
print("Please enter three values:")
inputValue1 = input("Value 1:")
inputValue2 = input("Value 2:")
inputValue3 = input("Value 3:")
if (("-" or ".") in (inputValue1 or inputValue2 or inputValue3)):
     inputValue1 = float(inputValue1)
     inputValue2 = float(inputValue2)
     inputValue3 = float(inputValue3)
largest= max(inputValue1, inputValue2,inputValue3)
print(largest)

'''
Please enter three values:
Value 1:hello
Value 2:how're you
Value 3:hoho
how're you

Please enter three values:
Value 1:420
Value 2:351
Value 3:530
530

Please enter three values:
Value 1:-35.8
Value 2:-28
Value 3:-36.5
-28.0
'''


#task 2
count = int(input("Please enter the number of items purchased: " ))
total = int(input("Please enter the total cost: "))
print("No negative items" if (count<0 or total<0) else "average = 0" if  count==0 else  "avarage = "+ str(total/count))


'''

Please enter the number of items purchased: -12
Please enter the total cost: -12
No negative items

Please enter the number of items purchased: -12
Please enter the total cost: 12
No negative items

Please enter the number of items purchased: -12
Please enter the total cost: 0
No negative items

Please enter the number of items purchased: 0
Please enter the total cost: -12
No negative items

Please enter the number of items purchased: 0
Please enter the total cost: 0
average = 0

Please enter the number of items purchased: 0
Please enter the total cost: 12
average = 0

Please enter the number of items purchased: 12
Please enter the total cost: -12
No negative items

Please enter the number of items purchased: 12
Please enter the total cost: 0
avarage = 0.0

Please enter the number of items purchased: 12
Please enter the total cost: 13
avarage = 1.0833333333333333
'''


    
     
  


#task 3
"""
 My guess for these codes are
 a.)Nothing gets printed
 b.)3 5 7 9 11 13 15

"""
#a
j=1 
while j < 10 : 
      j += 2 
      if j == 5 : 
          continue 
          print(j, end =  " ")

#b
for j in range (50) : 
     j += 2 
     print(j, end =  " ") 
     if j == 15 : 
               break 
"""

What Got Printed
a.) Nothing Printed
b.) 2 3 4 5 6 7 8 9 10 11 12 13 14 15 

For part a
The program worked the way I thought it would

For part b
the program printed every number rather then every other number.
This shows me that the j in the for loop is not altered by the j+=2 meaning it is  not within the same scope.
"""



#task 4
for x in range(5):
#initial for loop is for the 5 teset cases
     number= int(input("Enter a number to check if it is prime or not: "))
     for i in range(2,(number//2)+1):
          if number%i==0:
               print(number," is not a prime number")
               break
     else:
          print(number, " is a prime number")


'''
Enter a number to check if it is prime or not: 71
71  is a prime number
Enter a number to check if it is prime or not: 119
119  is not a prime number
Enter a number to check if it is prime or not: 30000001
30000001  is a prime number
Enter a number to check if it is prime or not: 34567
34567  is not a prime number
Enter a number to check if it is prime or not: 400000003
400000003  is not a prime number
'''