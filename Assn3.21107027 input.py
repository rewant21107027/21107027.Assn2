#Question1

print("Enter your input as decimal number and get its binary equivalent")
decimal_number = int(input("enter your decimal number: "))
number_bin = []
while decimal_number > 0:
    bin_digit = decimal_number%2
    number_bin.append(bin_digit)
    decimal_number = decimal_number//2
number_bin.reverse()
print("The binary equivalent is:")
for i in number_bin:
    print(i, end=" ")
print("\n")

#Question2

print("Welcome to this interactive python calculator")
enter_your_expression = input("Enter the expressions by using only these operators (+,-,*,/,**,%,//):")
print("The result is ", end=" ")
print(eval(enter_your_expression))
print("\n")

#Question3

import math as M

#part(a)

a_1 = 3
a_2 = 4
a_3 = 5
answer_a = (a_1+a_2)*a_3
print("Result of part (a) is: ", answer_a)
print("\n")
#part(b)

print("Choose the value of n")
n = float(input("The value of n taken is: "))
expression_b = (n*(n-1))/2
print("The result of part (b) is: ", expression_b)
print("\n")

#part(c)
print("Choose the value of r")
r1 = float(input("The value of r1 taken in: "))
expression_c = (4 * M.pi * (r1**2))
print("The result of part (c) is: ", expression_c)

#part(d)

r = float(input("enter the value of r: "))
a = float(input("enter the value of angle a: "))
b = float(input("enter the value of angle b: "))
print("The result of part (d) is: ", end=" ")
print(((r*((M.cos(a))**2)) + (r*((M.sin(b))**2)))**0.5)
print("\n")

#part(e)

x1 = float(input("enter the value of x1:"))
x2 = float(input("enter the value of x2:"))
y1 = float(input("enter the value of y1:"))
y2 = float(input("enter the value of y2:"))
print("The result of part (e) is: ", end=" ")
if x2 == x1:
    print("NOT DEFINED")
else:
    print("(y2-y1)/(x2-x1)", (y2-y1/(x2-x1)))
print("\n")

#Question4

print("In the range(5): ")
for i in range(5):
    print(i)

print("In the range(3, 10): ")
for i in range(3, 10):
    print(i)
print('\n')

print("In the range(4, 13, 3): ")
for i in range(4, 13, 3):
    print(i)
print('\n')

print("In the range(15 ,5, -2): ")
for i in range(15, 5, -2):
    print(i)
print("\n")

print("In the range(5, 3): ")
for i in range(5, 3):
    print(i)
print("\n")

#Question5

print("This program computes molecular weight of carbohydrates")
print(", for this we need to enter number of atoms of hydrogen, carbon and oxygen.")
no_of_hydrogen_atoms = int(input("enter the number of hydrogen atoms: ")) #number of atoms cannot be negative
no_of_carbon_atoms = int(input("enter the number of carbon atoms:")) #number of atoms cannot be negative
no_of_oxygen_atoms = int(input("enter the number of oxygen atoms:")) #number of atoms cannot be negative
#now calculating the weight of elements by multiplying their number of atoms and atomic mass
weight_of_hydrogen = no_of_hydrogen_atoms*1.00794
weight_of_carbon = no_of_carbon_atoms*12.0107
weight_of_oxygen = no_of_oxygen_atoms*15.9994
#weight of carbohydrate would be sum of weight of hydrogen , oxygen and carbon
weight_of_carbohydrate = weight_of_hydrogen + weight_of_carbon + weight_of_oxygen
print("The weight of carbohydrate: ", weight_of_carbohydrate)






