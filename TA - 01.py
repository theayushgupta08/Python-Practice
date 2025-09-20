filename=input("Enter the File Name (with extension): ")
fp=open(filename,"w+")
fp.write("Welcome to the World of Programming!")
fp.seek(0)
print("The contents of the file is: ",fp.read())
ch=input("Enter the character to be searched: ")
n=0
fp.seek(0,2)
l=fp.tell()
fp.seek(0)
for i in range(l):
    if ch==fp.read(1):
        n+=1
    else:
        continue
print(f"The number of times the character {ch} repeated is {n}")