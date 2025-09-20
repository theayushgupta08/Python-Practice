'''
Lambda Function(Anonymous Function):
1.Lambda function have no name.
2.It is not declared using def keyword.
3.It is created using lambda keyword.
4.Lambda function contains only a single line.
5.It can take any number of arguments.
6.It can return just one value in the form of an expression.
7.It does not have an explicit return statement,
but contains an expression which is returned.

Syntax:
lambda arguments:expression

8.They cannot access variables other than those in
their argument(parameter) list.
9.They can access Global variables.
10.We can pass lambda functions as arguments in other functions.
11.We can call a lambda function from another lambda function.
12.We can define lambda function that receives no argument.
'''
#Example 1: To add two numbers by assigning lambda function
# to a variable(add)
c=4
add=lambda a,b:a+b+c
print("Addition is with using variable", add(3,6))   #13

sub=lambda x,y,z:x-y-z
print("Subtraction of three number is ",sub(5,3,1))    #1

#Example 2:Two add two numbers without assigning lambda function
# to any variable
print("Addition is without using variable",end=' ')
print((lambda a,b:a+b) (4,5))      #9

print((lambda a,b:a-b) (7,3))    #4

#Example 3: Lambda function doesnot receive any arguments
# but simply returns an expression
x=lambda:sum(range(1,11))
print(x())    #55
print("Use of lambda function")
print((lambda:sum(range(1,11)))())   #55

#Example 4: Calling one lambda function into another lambda function
add=lambda a,b:a+b
multipy_and_add=lambda x,y,z:x*add(y,z)
print(multipy_and_add(3,4,5))    #27

#Example 5: You can pass lambda functions as arguments in
# another functions
def small(a,b):
    if(a<b):
        return a
    else:
        return b
sum=lambda x,y:x+y
diff=lambda x,y:x-y
print(small(sum(-3,-2),diff(-1,-2)))     #-5
