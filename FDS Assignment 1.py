"""
Write a Python program for department library which has N books, write functions for following:
a) Delete the duplicate entries
b) Display books in ascending order based on cost of books
c) Count number of books with cost more than 500.
d) Copy books in a new list which has cost less than 500.
"""
class library:
    bookname=[]
    bookcost=[]
    bookid=[]
    newbooklist=[]

    def getdata(self):
        for i in range(n):
            self.bookname.append(input("\nEnter the name of the Book: "))
            self.bookid.append(input("\nEnter the ISBN Number: "))
            self.bookcost.append(input("\nEnter the Price of the Book: "))

    def duplicate(self):
        templist=[]
        for j in self.bookname:
            if j not in templist:
                templist.append(j)
        self.bookname=templist
        print("\nList after deleting duplicate values is: ",templist)

    def costcheck(self):
        lesscost=[]
        highcost=[]
        for k in self.bookcost:
            if k>500:
                highcost.append(k)
            elif k<500:
                lesscost.append(k)
        print("\nNumber of books with cost more than 500 is: ",len(highcost))
        print("\nNumber of books with cost less than 500 is: ",len(lesscost))

    def costvalue(self):
        costless=[]
        for l in self.bookcost:
            if l<500:
                newbooklist=costless.append(l)
        if len(costless)==0:
            print("\nNo Book is less than of cost 500.")
        else:
            print("\nCost less than 500s are: ")
            for m in self.bookcost:
                print("\n",self.bookcost)

    def sorting(self):
        self.bookcost.sort()
        print("\nList of cost after arranging in ascending order is: ",self.bookcost)

    def display(self):
        print("\nBook Name \t\t\t ISBN Number \t\t\t Price \n")
        for m in range(n):
            print(self.bookname[m],"\t\t\t",self.bookid[m],"\t\t\t",self.bookcost[m])

if __name__=="__main__":
    n=int(input("\nEnter the number of the Books: "))
    l=library()
    l.getdata()
    l.display()
    choice=int(input("\nOptions: \n1. Delete Duplicate Entries. \n2. Check cost less or more than 500. \n3. Copy Books to the new list which are less than 500. \n4. Exit \n\nEnter your choice: "))
    if choice==1:
        l.duplicate()
    elif choice==2:
        l.costvalue()
    elif choice==3:
        l.costvalue()
    elif choice==4:
        print(("\nExiting...."))
    else:
        print("\nInvalid Value Entered!")


