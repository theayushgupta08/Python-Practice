l1=[1,2,3,4,5]
print(type(l1))
l1.append((12))   #Adding Element at the ending of the list
print(l1)
l1.insert(2,22)    #Inserting 22 in the list at index to 2. Remaining will shift to right
print(l1)
l1.remove(22)    #Removing known element 22 from the list  & #Removing element that is not present gives value error
print(l1)
f1=12.34567
print(format(f1,'.2f'))   #to format float number upto 2 decimal places
#Removing element at particular index
print(l1.pop(2))
print(l1)
print(l1.pop(2))   #Removing element at particular index
print(l1)
del l1[1]   #To Delete element at specified index or whole list
print(l1)
#del l1    #To delete the complete list
#print(l1)   # Must show name error becoz no list is present with  the name l1
l1.clear() #It will delete all the content
print(l1)  #Only Square Brackets will be the output
