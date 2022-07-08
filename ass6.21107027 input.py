#QUES1

print('a perfect number is a number that is half the sum of all of its positive divisors (including itself).')
choose_num = int(input('enter the number you want to check is perfect or not: ')) #Enter a positive number only

if choose_num > 0:   #checking if number entered by user is positive or not
    num_taken = choose_num
else:
    num_taken = int(input('enter a positive number: '))

div_list = []   #creating an empty list to add divisors

for i in range(1, num_taken):   #finding divisors of number taken and adding it in list
    if num_taken % i == 0:
        div_list.append(i)
    else:
        pass

print('list of proper divisors is: ', div_list)  #it excludes number itself

if (sum(div_list) + num_taken)/2 == num_taken:  #checking condition for a perfect number
    print('number taken is perfect')
else:
    print('number taken is not perfect')
print('\n')

#QUES2

print("This is a program to check whether a passed string is palindrome or not. ")

enter_str = input('Enter the string you want to check is a palindrome or not: ')
enter_str = enter_str.replace(' ', '')  #replace space without space
rev_str = enter_str[::-1]
rev_str = rev_str.replace(' ', '')

if rev_str == enter_str:  #entering condition for equality
    print('entered string is a palindrome')
else:
    print('entered string is not a palindrome')

print('\n')

#QUES3

n = int(input('enter the number of rows: '))

from math import factorial  #importing math for using factorial

for i in range(n):   #applying mathematical concept behind pascals triangle
    for j in range(n-i+1):
        print(end=" ")

    for j in range(i+1):
        print(factorial(i)/(factorial(j)*factorial(i-j)), end=" ")

    print()
print('\n')

#QUES4

print('This is a python function to check whether a string is pangram or not ')
print('Pangram are words or sentences containing every letter of the alphabet at least once')

write_str = input('Enter the input string you want to check for pangram: ')  #Taking input string from user

def ispangram(write_str):   #creating a function for checking pangram
    alphabet = 'abcdefghijklmnopqrstuvwxyz'   #listing all the alphabets
    for char in alphabet:   #applying the condition for pangram
        if char not in write_str.lower():
            return False
    return True

if (ispangram(write_str) == True):
    print('YES, this is a pangram')
else:
    print('NO, this is not a pangram')

print('\n')

#QUES5

word = input("Enter hyphen-separated sequence of words : ")
items = [n for n in word.split('-')]
items.sort()
print('-'.join(items))
print('\n')

#QUES6

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: {kwargs['student_name']}")
            print(f"Student Class: {kwargs['student_class']}")


student_data(student_id='21107027', student_name='Rewant Pahuja')

student_data(student_id='21107027', student_name='Rewant Pahuja', student_class ='2nd Semester')
print('\n')

#QUES7

class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print('\n')

#QUES8

list=[]
def findTriplets(arr, n):

    found = False
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    list.append([arr[i],arr[j],arr[k]])
                    print(list)
                    found = True

    if (found == False):
        print(" not exist ")

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)
print('\n')

#QUES9

class validity:

    def f(str):

        a= ['()', '{}', '[]']

        while any(i in str for i in a):

            for j in a:

                str = str.replace(j, '')

        return not str

s = input("enter : ")

print(s, "-", "is balanced"

      if validity.f(s) else "is Unbalanced")
