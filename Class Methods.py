class student:
    name="Ayush Gupta"    #Public Variable
    __rollno=11145       #Private Variable
    _div="A"   #Protected Variable
    def student1(self):   #Class Method 01
        print("Name of the student: ",self.name)
        print("Roll No. of the student: ",self.__rollno)
        print("Division of the student: ",self._div)
    def student2(self,name,__rollno,div):    #Class Method 02
        print("Name of the student: ",name)
        print("Roll No. of the student: ",__rollno)
        print("Division of the student: ", _div)
s=student()     #Class Oblect
s.student1()   #Class Function without argument
s.student2("Sahil",11146,"B")    #Class Function with argument
h=student.stud()
h.haramistud()