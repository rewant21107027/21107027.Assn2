#Python Assignment 2

#Question1

string_a = "python is a case sensitive language" # string_1
print("<A> the length of the string_1 is:", len(string_a)) # function to find the length of the string
print("<B> the reverse of order of string_1 is:", string_a[-1::-1]) # reversing the order or string_a
string_c = string_a[10:27] # stored a case sensitive in a new string
string_c.replace("a case sensitive", "object oriented") # replaced "a case sensitive" with "object oriented"
print("<E> the index of substring a in string_a is:", string_a.find("a")) # calculating the index of string
# now removing white spaces from the string
print("<F> the input string string_a after removing white spaces is:", string_a.replace(" ", ""))
print("\n")

#Question2

name = input("enter your name:") #entering my name
SID = int(input("enter your SID:")) #entering my sid
department = input("enter your department:") #entering my department
CGPA = float(input("enter your CGPA:")) #entering my cgpa
print("hey, %s "%name, "here!")
print("my SID is %d"%SID)
print("i am from %s"%department, "and my CGPA is %f"%CGPA)
print("\n")

#Question3

a = 56 #given
b = 10 #given
#solving the given questions using bitwise operators
print("<a> ", a&b)
print("<b>", a|b)
print("<c>", a^b)
print("<d> left shift both a and b with 2 bits respectively are:", a<<2, b<<2)
print("<e> right shift a with 2 bits and b with 4 bits respectively are:", a>>2, b>>4)
print("\n")

#Question4

#taking inputs
i = str(input("Enter a string:"))
#using string slice method to find the word in line
checked = i.find("name")
#making a loop for printing yes or no according to the output
#here '==' is a comparison operator
if checked == -1: #'-1' is the value as the output of find function indicating absence of particular str in  it
    print("No")
else:
    print("Yes")
print("\n")

#Question5

print("This program determines whether 3 sides entered by the user can form triangle or not?")
side_1 = int(input("Enter length of first side of the triangle:"))
side_2 = int(input("Enter length of second side of the triangle:"))
side_3 = int(input("Enter length of third side of the triangle:"))

A = side_1 < side_2+side_3
B = side_2 < side_1+side_3
C = side_3 < side_1+side_2

Result = str(A&B&C)
print("Can  the sides entered by user form a triangle?")
Result = Result.replace("True", "Yes")
Result = Result.replace("False", "No")
print("The answer is:", Result)
print("\n")

#Question6

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = (a^b)
d = bin(c)
count = 0
for i in d[2:]:
    if i == "1":
        count += 1
        print(count)





