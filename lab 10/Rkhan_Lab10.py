"""
Rashad Khan
010713326
CS2520-01
Project 3
04/26/2023
"""
#Lab10_bike.py
class Bike:
    def __init__(sf, gr, sp):
        sf.gr = gr
        sf.sp = sp
    def applyBrake(sf, decrement):
        sf.sp -= decrement
    def spUp(sf, increment):
        sf.sp += increment
    def __str__(sf):
        return f"No. of grs are {sf.gr}\n" \
               f"speed of Bike is {sf.sp}"

class MtnBike(Bike):
    def __init__(sf, gr, sp, startHeight):
        super().__init__(gr, sp)
        sf.seatHeight = startHeight
    def setHeight(sf, newValue):
        sf.seatHeight = newValue
    def __str__(sf):
        return f"{super().__str__()}\nseat height is {sf.seatHeight}"

def main():
    mb = MtnBike(3, 100, 25)
    print(mb)

main()

"""
No. of grs are 3
speed of Bike is 100
seat height is 25
"""

#Lab10_Fraction.py

class Fraction:
  def __init__(sf, n=0, d=1):
    sf.num = n
    sf.den = d
  
  def __add__(sf, f):
    return Fraction(sf.num * f.den + sf.den * f.num, sf.den * f.den)

  def __mul__(sf, f):
    return Fraction(sf.num * f.num, sf.den * f.den)

  def __eq__(sf, f):
    return sf.num * f.den == sf.den * f.num

  def __str__(sf):
    return str(sf.num) + "/" + str(sf.den)

f1 = Fraction(3, 7)
f2 = Fraction(2, 5)
f3 = Fraction(1, 3)
f4 = Fraction(2, 6)
result = f1 + f2 * f3
print(result)
if f1 == f3:
  print("f1 = f3")
else:
  print("f1 != f3")
if f3 == f4:
  print("f3 = f4")
else:
  print("f3 != f4")

"""
59/105
f1 != f3
f3 = f4
"""