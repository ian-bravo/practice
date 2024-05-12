name = "ian" #comment
print(name)
#comment
print(type(name) == str) #true
# print(isinstance(name, str)) #true
# age = 30
# print(isinstance(age,int)) #true
# age = 30.5
# print(isinstance(age,float)) #true
# age = float(30)
# print(isinstance(age, float)) #true
# age = "30"
# print(isinstance(age, int)) #false
# age = int("30")
# print(isinstance(age, int)) #true
# number = "30"
# age = int(number)
# print(isinstance(age, int)) #true 
#casting
# number = "test"
# age = int(number)
# print(isinstance(age, int)) #ValueError: invalid literal for int() with base 10: 'test'

# # complex for complex numbers
# # bool for booleans
# # list for lists
# # tuple for tuples
# # range for ranges
# # dict for dictionaries
# # set for sets

# 4 % 3 #1
# 4 ** 2 #16
# 5 // 2 #2 (rounds down - floor division)
# 1 + -1 #0

# # age = 8
# # age += 8
# # print(age) #16
# # age *= 8     # age = age * 8
# # print(age) #64

# # cond1 = True
# # cond2 = False

# # not cond1 #false
# # cond1 and cond2 #false
# # cond1 or cond2 #true

# or returns the first operand that is not a falsy value, otherwise it return the last operand
# print(0 or 1) #1
# print(False or 'hey') #'hey'
# print('hi' or 'hey') #'hi'
# print([] or False) #False
# print(False or []) # []

# and only evaluate the second argument if the first one is true. 
# print(0 and 1) #0
# print(1 and 0) #0
# print(False and 'hey') #False
# print('hi' and 'hey') #'hey'
# print([] and False) #[]
# print(False and []) #False

# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation

# is, identity operator. compares objects. returns true if both are the same object.

# in, membership operator, if a value is contained in another sequence/list

# def is_adult(age):
#   if age > 18:
#     return True
#   else:
#     return False
  
# ternary operator:
# def is_adult2(age):
#   return True if age > 18 else False

# name = "ian"
# name+= " is my name"
# print(name) # ian is my name

# print('''Ian is

# 30

# years old
# ''')

# Ian is

# 30

# years old

# print("ian".upper()) #IAN
# print('iaN'.lower()) #ian
# print("ian person".title()) #Ian Person , caps first letter
# print("ian person".islower()) #true
# print("iaN person".islower()) #false

# isalpha() to check if string contains only characters and is not empty
# isalnum() to check if a string contains char or digits and is not empty
# isdecimal() to check if string contains digits and is not empty
# startswith() to check if the string starts with a specific substring
# endswith() to check if string ends with a specific substring
# replace() to replace a part of a string
# split() to split a string on a specific char separator
# strip() to trim the whitespace from a string
# join() to append new letters to a string
# find() to find the new position of a substring

# # all return a new modified string
# name = 'Ian'
# print(name.lower()) #ian
# print(name) #Ian
# print(len(name)) #3
# print('n' in name) #true

# escaping (\) is a way to add special char into a string
# \ means the next character is going to mean what it normally means, will act as a string 
# name = "Ian"
# name = "I\"an"
# name = "I\nan" # \n means new line
# name = 'Ia\n' # Ia
# name = 'Ia\\n' #Ia\n
# name = 'ian'
# print(name[1]) #a
# name = 'ian'
# print(name[-1]) #n (last char in string)
#range
# name = 'person'
# print(name[1:3]) #er starts at index 1, end before index 3
# print(name[1:2]) #e
# name1 = 'ian is cool'
# print(name1[1:7]) #an is
# print(name1[:7]) #ian is  returns UP TO index 7
# print(name1[5:]) #s cool end of the string

# done = False
# if done:
#   print("yes")
# else:
#   print("no")  #prints no

# done = True
# if done:
#   print("yes") #prints yes
# else:
#   print("no")  

#numbers are always true except 0. zero is false
#strings are false only when empty
# #list, tuples, sets, and dict are false only †

#any returns true if any of the values are iterable, if any of them are true, will return true.
# book_1_read = True
# book_2_read = False
# read_any_book = any([book_1_read, book_2_read])

#all returns true if all of the values are true
# ingred_purchased = True
# meal_cooked = False
# ready_to_serve = all([ingred_purchased, meal_cooked])

# complex numbers are expressed as part of a real part, and an imagine part
# written with 'j'
# num0 = 2+3j
# num = complex(2, 3) #2 is the real, 3 is imagine
# print(num.real, num.imag) #2.0, 3.0