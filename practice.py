name = "ian" #comment
print(name)
#comment
print(type(name) == str) #true
print(isinstance(name, str)) #true
age = 30
print(isinstance(age,int)) #true
age = 30.5
print(isinstance(age,float)) #true
age = float(30)
print(isinstance(age, float)) #true
age = "30"
print(isinstance(age, int)) #false
age = int("30")
print(isinstance(age, int)) #true
number = "30"
age = int(number)
print(isinstance(age, int)) #true 
#casting
number = "test"
age = int(number)
print(isinstance(age, int)) #ValueError: invalid literal for int() with base 10: 'test'

# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets
