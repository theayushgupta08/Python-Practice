fp=open("Count.txt","w+")
fp.write("My fav number is 8")
fp.seek(0)
print(fp.read())
fp.seek(0,2)
u,w,d=0,0,0
l=fp.tell()
fp.seek(0)
for i in range(l):
    ch=fp.read(1)
    if ch.isupper()==True:
        u+=1
    elif ch.islower()==True:
        w+=1
    elif ch.isdigit()==True:
        d+=1
    else:
        continue
print("The no. of Uppercase Characters are: ",u)
print("The no. of Lowercase Characters are: ",w)
print("The no. of Digits are: ",d)