n=int(input("Enter the length of the series: "))
def fibonnaci(a,b,n):
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c
a=0
b=1
print(a)
print(b)
fibonnaci(a,b,n)