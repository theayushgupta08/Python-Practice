def factorial(n):
    '''This is the Factorial Fuction'''    #This is the doc string
    print(factorial.__doc__)        #Printing the doc string
    f=1
    for i in range(n,0,-1):     #loop for finding factorial
        f*=i
    print(f)
    return f
n=3
factorial(n)
def add(a,b):
    c=a+b*factorial(n)
    return(c)
print(add(2,3))   #Output= 20
def f(*d):   #Variable lenght argument stores elements passed in the form of tuple if no elements passed tuple would be empty
    '''This is the doc string under variable lenght function'''
    sum=0
    for j in d:   # for i in (2,3) i.e. loop will run only 2 times for ele 2 and ele 3
        sum+=j   #first it will take 2 and then 3
    print(sum)
f(2,3)   #Output= 5
f()   #Output= 0
f(2,3,4)   #Output= 9


#Teacher's Code
# 1. Calling one function into another function
'''5 factorial
n=5
=5*4*3*2*1
=120

for i in range(n,0,-1)'''
# 2. Documentation Strings
# 3. Write a program that uses docstrings and
# variable length arguments to add the values passed
# to the function
# Syntax:f(),f(2,4),f(1,2,3)

def f(*a):  #a=(1,2,3)
    ''' This is a function to add an integer number of variable length'''
    sum=0
    for i in a:  # for i in (1,2,3) i=1  i=2 i=3
        sum=sum+i  #0+1  sum=1
    print(sum)
f(1,2)
f(1)
f(1,2,3)
def fact(n):
    '''This is factorial function.'''
    print(fact.__doc__)
    f=1
    for i in range(n,0,-1):
        f=f*i
    print(f)
def add(a,b):
    '''This is a add function'''
    print(add.__doc__)
    c=a+b
    return(c)
def multiply_and_add():
    d=5*add(6,2)
    print(d)
n=int(input('Enter any number'))
fact(n)
add(3,6)
multiply_and_add()
