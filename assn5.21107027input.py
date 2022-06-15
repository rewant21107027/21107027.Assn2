#QUES1

story = input("enter the string you want to reverse: ") #taking story as my input string
print("My input string is: ", story)

rev_story = "" #taking rev_story as my reverse string and taking it empty initially

count = len(story) #determining length of story and storing it in count

while count > 0:
    rev_story += story[count-1] #saving the index of count-1 one by one in rev_story
    count = count - 1 #decrement index
print("My reverse of input string is : ", rev_story)
print('\n')

#QUES2

x = int(input("enter initial entry of range: ")) #taking x as first entry of range
y = int(input("enter one number more you want to see according to last number in range: "))#taking y last entry+1 of
# range

div_number = int(input("enter number that you would divide on items of range: ")) #taking input number that we will
# divide

for item in range(x, y):
    if item % div_number == 0: #if on diving we get 0 remainder, the item is divisible
        print(item) #printing the divisible item
    else:
        pass
print("\n")

#QUES3

i = 0
while i < 5:
    s1 = int(input("enter 1st side you want for triangle: "))  # taking 1st side of triangle
    s2 = int(input("enter 2nd side you want for triangle: "))  # taking 2nd side of triangle
    s3 = int(input("enter 3rd side you want for triangle: "))  # taking 3rd side of triangle
    s = (s1 + s2 + s3)/2 #s is the semi perimeter of the triangle
    herons_formula = (s*(s-s1)*(s-s2)*(s-s3))**0.5
    if (s1 + s2) > s3 and (s2 + s3 > s1) and (s1 + s3) > s2: #conditions to form a triangle
        print("The area of triangle is: ", herons_formula) #printing the area of triangle
    else:
        print("Triangle is not possible according to entered inputs")
    i = i + 1
print("You have only 5 opportunities to calculate area of triangle")
print("\n")

#QUES4

n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')

print("\n")

 #QUES5

no_of_rows = int(input('enter the number of rows you want to see: '))

k = 65
for i in range(1, no_of_rows+1):
    for j in range(i):
        y = chr(k)
        print(y, end="")
        k += 1
        if (k-64)%26 == 0:
            k = 65
    print("")

print("\n")

#QUES6

print("choose your lower and upper input range members")

lower_input_range = int(input('enter the lower input of range: '))
upper_input_range = int(input('enter the upper input of range: '))  # taking input from the user

print('My range is: ', (lower_input_range, upper_input_range))  #printing my range

for number in range(lower_input_range, upper_input_range + 1):  #finding number in the range
    if number > 1:
        for i in range(2, number):   #finding a number 'i' that we will be divided to number
            if (number % i) == 0:
                break                #if remainder is 0, it is not a prime number, and we break the range
        else:
            print(number)

print("\n")

#QUES7

print("following numbers are divisible by 11 and multiple of 7")

for number in range(1, 500):#taking the range
    if number % 7 == 0 and number % 11 == 0:   #applying the condition
        print(number)
else:
    pass    # applying pass in order to ignore unwanted numbers

print('\n')

#QUES8

print("you can enter 10 numbers")
num_list = []  #creating an empty list

i = 1
while i < 11:
    num = int(input('enter' + str(i) + ' integer: '))
    num_list.append(num)  #filling my list
    i = i + 1

print("my list is ", num_list)

#a
print('soln of part a, positive numbers ')
for number in num_list:
    if number > 0:     # condition for positive numbers
        print(number)
else:
    print('none')    # ignoring all other numbers
#b
print('soln of part b, negative numbers')
for number in num_list:
    if number < 0:   # condition for negative numbers
        print(number)
else:
    print('none')
#c
print('soln of part c, odd numbers')
for number in num_list:
    if number % 2 != 0:
        print(number)
    else:
        print('none')
#d
print('soln of part d, even numbers')
for number in num_list:
    if number % 2 == 0:
        print(number)
    else:
        print('none')
#e
print('soln of part e, number of times element occurs in list')
for number in num_list:
    print(number, " occurred ", num_list.count(number), " times")
'''
#QUES9
'''
print('you can enter only 10 words in the list')

userlist = []  #taking an empty list

i = 1
while i < 11:
    word = input('enter' + str(i) + ' word: ')
    userlist.append(word)  #filling my list
    i = i + 1

print("list entered by user is: ", userlist)

for word in userlist:
    print(word, 'occurred ', userlist.count(word), ' times') 
