# Simple Calculator

#Taking input of the two number from the user

firstnum=int(input("Enter the First Number: "))
secondnum=int(input("Enter the Second Number: "))

#Displaying list of options to choose from

print("Choose the operation from the list to perform: "
      "\n 1. Addition "
      "\n 2. Subtraction (From 1st Number to 2nd Number) "
      "\n 3. Subtraction (From 2nd Number to 1st Number) "
      "\n 4. Multiplication "
      "\n 5. Division (1st Number by 2nd Number) "
      "\n 6. Division (2nd Number by 1st Number) "
      "\n 7. Exponent (1st Number of 2nd Number) "
      "\n 8. Exponent (2nd Number of 1st Number)")

#Taking input from the user to choose any option

option=int(input("Enter your option (1-8): "))

#Performing operations based on the user's input

if option==1:
    print("Addition of the two Number is: ",firstnum+secondnum)
elif option == 2:
    print("Subtraction (From 1st Number to 2nd Number) of the two Number is: ", firstnum - secondnum)
elif option == 3:
    print("Subtraction (From 2nd Number to 1st Number) of the two Number is: ", secondnum-firstnum)
elif option == 4:
    print("Multiplication of the two Number is: ", secondnum*firstnum)
elif option == 5:
    print("Division (1st Number by 2nd Number) of the two Number is: ", firstnum / secondnum)
elif option == 6:
    print("Division (2nd Number by 1st Number) of the two Number is: ", secondnum/firstnum)
elif option == 7:
    print("Exponent (1st Number of 2nd Number) of the two Number is: ", firstnum ** secondnum)
elif option == 8:
    print("Exponent (2nd Number of 1st Number) of the two Number is: ", secondnum**firstnum)
else:
    print("Invalid option chose!")