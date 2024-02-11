      #Program-1
#Python program to create a child class
class Person:
 pass 
class Student(Person):
 pass

      #Program-2
#Python program to demonstrate Inheritance
class Person(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(Person):
    def isEmployee(self):
        return True
emp = Person("Ram") 
print(emp.getName(),emp.isEmployee()) 
emp = Employee("Sita") 
print(emp.getName(),emp.isEmployee())

'''Output:
Ram False
Sita True '''

          #Program-3
#Python program to demonstrate super() function in inheritance
class Person():
 def __init__(self, name, age):
     self.name = name
     self.age = age
 def display(self):
     print(self.name, self.age)
class Student(Person):
 def __init__(self, name, age):
     self.sName = name
     self.sAge = age
     super().__init__("Rahul", age)
 def displayInfo(self):
     print(self.sName, self.sAge)
obj = Student("Ram", 23)
obj.display()
obj.displayInfo()

'''Output:
Rahul 23
Ram 23'''

          #Program-4
#Python program to demonstrate adding of prperties to child class
# parent class
class Person():
 def __init__(self,name,age):
    self.name = name
    self.age = age
 def display(self):
    print(self.name,self.age)
class Student(Person):
 def __init__(self,name,age,dob):
    self.sName = name
    self.sAge = age
    self.dob = dob
#inheriting the properties of parent class
    super().__init__("Ram", age)
 def displayInfo(self):
    print(self.sName,self.sAge,self.dob)
obj=Student("sita",24,"16-03-2000")
obj.display()
obj.displayInfo()

'''Output:
Ram 24
sita 24 16-03-2000 '''
