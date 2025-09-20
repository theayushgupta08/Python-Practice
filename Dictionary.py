#Dictionary is ordered, Changeable, allows duplicate values, stores element in pairs such as key:value Pairs
d1={1:"Ayush Gupta",2:"Asmita Singh",3:"Ashutosh Madheshiya",4:"Nilesh Yadav"}
print(type(d1))
print(d1)
print(d1.items())  #To display each values seperately
print(d1.keys())   #To Display only keys
print(d1.values())  #To display only values in the keys
d1.pop(1)  #To remove the element & If used index which is not there then it will show key error
print(d1)
print(d1.get(2))  #To display value stored in key 2
d1.clear()  #To clear the dictionary
print(d1)
del d1   #To delete complete dictionary