#Question1

print("Solution 1")
i = 1
while i <= 6:
    marks = int(input("Enter your marks: ")) #entering the marks
#marking grades according to question
    if marks < 25:
        print("Grade : F")
    if 25 <= marks < 45:
        print("Grade : E")
    if 45 <= marks < 50:
        print("Grade : D")
    if 50 <= marks < 60:
        print("Grade : C")
    if 60 <= marks < 80:
        print("Grade : B")
    if marks >= 80:
        print("Grade : A")
    i = i + 1
print("Your choice for choosing marks and getting corresponding grade is over ")
print("\n")

#Question2

print("Solution 2")
year_number = int(input("Enter year number: "))
if year_number % 100 == 0 and year_number % 400 != 0:
    print("it is not a leap year")
elif year_number % 4 == 0:
    print('it is a leap year')
else:
    print("it is not a leap year")
print("\n")

#Question3

print("Solution 3")
from random import randint

print("Welcome to multiplication game program")
i = 1
while i <= 10:
    x = randint(0, 20)
    y = randint(0, 20)
    expression = x*y
    print("Question number", str(i), ", ", str(x), "X", str(y), "is")
    z = int(input("Type your answer: "))
    if z == x*y:
        print("Right Answer!")
    else:
        print("Oops! The answer is incorrect, try again")
    i = i + 1
print("Number of questions are over, great learning!")
print("\n")

#Question4

print("Solution 4")
for i in range(200):
    if i % 5 == 2:
        if i % 6 == 3:
            if i % 7 == 2:
                print("There are " + str(i) + " Candies in total")
print("\n")
