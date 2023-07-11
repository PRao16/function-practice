# Write your code here :-)  Functions practice.
#Functions are named blocks of code, designed to do one specific job. Information passed to a function is called argument.  and information received by
#a function is called parameter.

# def is a reserved keyword in Python

def robo():
    print('Welcome to my program')
    print('Hope you are having a great day!')

robo()
#Blank line to seperate block of code

print('Another example of function')
print()

def add():
    a=100
    b=200
    sum= a+b
    print(sum)
add()

print()
#print('Or you can also write the same program this way:')

def add(a,b):
    sum = a+b
    print(sum)

add(500,560)

print()#blank line

# A simple function

def greet_user():
    """Display a simple greeting"""
    print('Hello!')
greet_user()

# passing an argument to the function
def greet_user(username):
    """display a personaized greeting"""
    print('Hello! ' + username + "!")
greet_user('jesse')

print()#blank line

#Default values to parameter

def make_pizza(topping='bacon'):
    """ make a single topping pizza"""
    print('Hello! have a ' + topping + ' pizza')
make_pizza()
make_pizza('Cheese')
make_pizza('Onion')

print()#blank line
#Return statement in function

def square(number):
    return(number*number)

print(square(4))

#another example addition
print()# extra line for space

def add(number):
    return(number+number)
print(add(100))

print() #adding a blank line.
#anoter practice code for function
def dallas_trip(a,b):
    distance_to_dallas = '30 Miles'
    gas= a
    parking= b
    total_cost = a+b
    print('your trip to Dalas today is ' + distance_to_dallas + ' away ' + 'and it is going to cost you ' + str(total_cost) + ' Dollars')
    print('Thank you!')
    print('parking is cheap!')


dallas_trip(20,3)

