fp=open("Counting.txt","w+")
fp.write("Hi I am Ayush Gupta. \t \n FE Computer Department")
fp.seek(0)
print(fp.read())
fp.seek(0,2)
l=fp.tell()
s,t,n=0,0,0
fp.seek(0)
for i in range(l):
    ch=fp.read(1)
    if ch==' ':
        s+=1
    elif ch=='\t':
        t+=1
    elif ch=='\n':
        n+=1
    else:
        continue
print("The no. of spaces are: ",s)
print("The no. of tabs are: ",t)
print("The no. of new line are: ",n)

