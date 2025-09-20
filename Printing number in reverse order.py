n1=input("Enter any digit Number: ")
print(n1[::-1])

#OR

n=int(input("Enter any digit Number: "))
l=len(str(n))
for i in range(l):
    r=n%(10**(i+1))//(10**i)
    print(r)
