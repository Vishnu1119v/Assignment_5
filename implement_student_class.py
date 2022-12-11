class Student:
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,rollno):
        self.__rollno=rollno
    def getRollNumber(self):
        return self.__rollno
student1=Student()
student2=Student()

#student1
student1.setName('vishnu')
student1.setRollNumber('100')

print(student1.getName())
print(student1.getRollNumber())

#student2
student2.setName('arya')
student2.setRollNumber('101')

print(student2.getName())
print(student2.getRollNumber())

