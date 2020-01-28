#intro Of Class 
'''
class abc:
    def asdf(lol):
        #self is object which you are passing
        print("i5,16gb,1TB")
qwe=abc()
abc.asdf(qwe)
qwe.asdf()
#asdf take parameter And Here asdf take argument qwe and
#it will pass self
'''
#__init__ Method 
'''
class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config IS",self.cpu,self.ram)

computer1=computer('Intel i9','16GB')
computer2=computer('Ryzen 3','8GB')

computer1.config()
computer2.config()
'''

#Constructor ,Self And Comparing Object
'''
class personal:
    def __init__(self):
        self.name="LOL"
        self.age=18

    #With Using Function Compare Both Object Properties

    def compare(self,p2): #compare(Who IS Calling,Whom To Compare)
        if self.age ==  p2.age: #Self=p1 Is Calling And And p2 Is Compare
            return True 
        else:
            return  False

#    def update(self):
#      self.age=20        

p1=personal()
p2=personal()
  
p1.name="lol"
p1.age=19
print(p1.name,p1.age)
print(p2.name,p2.age)


if p1.compare(p2):#P1 Is Calling Or Self Is Calling  To Compare Function Or Module And Compare With P2  
    print("Both Having Same Age")
else:
    print("Both Having Differnet Age")
'''

'''print("Before Updating")
print(p1.age)
print(p2.age)
p1.update()
print("After Updating")
print(p1.age)
print(p2.age)
'''
#without Function Using Comapre Both Object Propeties
'''if p1.age == p2.age:
    print(p1.name,p1.age,"=",p2.name,p2.age,"Both Having Same Age")
else:
    print(p1.name,p1.age,"=",p2.name,p2.age,"Both Having Different Age")
'''

#Type Of Varible
'''
class mobile:
    #Class Varible
    bettery="5,000Mah" #Class Namespace
    def __init__(self):
        #Instance Varible
        self.model=("Zenfone 5") #instance Namespace
        self.ram="6GB"
        self.price="20,000Rs"

m1=mobile()
m2=mobile()

mobile.bettery="5,500Mah" #Class Varible

m1.model="Zonfone 6" #Instance Varible
m1.ram="8GB"
m1.price="30,000Rs"

print(m1.model,m1.ram,m1.price,m1.bettery)
print(m2.model,m2.ram,m2.price,m2.bettery)
'''
'''
n=input("Enter No-")
sum=0
d=map(lambda x : int(x),str(n))
for ds in d:
    sum+=ds
print("Sum Is",sum)
'''
'''
n=int(input("enter Sum-"))
sum=0
rev=0
s1=0
while n!=0:
    rev=(n%10)
    n=n//10
    sum=sum+rev
s2=sum
while s2!=0:
    rev=(s2%10)
    s2=s2//10
    s1=s1+rev
print("Sum Is",s1)
'''
#Type Of Methods
'''
class Student:
    school="Hello World" #Class Varible
    #Instance Method
    def __init__(self,m1,m2,m3):
        self.m1=m1 #instance Varible m1,m2,m3
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    #Class Method
    @classmethod #Class Decorator
    def scinfo(cls): #cls Class keyword For Using Class Method
        return cls.school

    #Static Method
    @staticmethod #Static Decorator
    def info():
        print(" Use As A Normal Functions")
        
s1=Student(50,65,35)
s2=Student(65,75,55)

print(s1.avg())
print(s2.avg())

print(Student.scinfo())

        Student.info()
'''
'''
class computer:
    def __init__(self):
        self.cpu = 'i9'
        self.ram = '16Gb'

   #def config(self):
     #   print("Config IS",self.cpu,self.ram)

#computer1=computer('i9','16Gb')
computer1=computer()    
#computer1.config()
print(computer1.cpu,computer1.ram)    
'''
#Extra Not Working
'''
def questio(n):
        Question={}
        for i in range(n):
            a=input("Enter The Question-")
            option1=input("Enter The Option1-")
            option2=input("Enter The Option2-")
            option3=input("Enter The Option3-")
            option4=input("Enter The Option4-")
            answer=input("Enter The Answer-")
            Question.update(a = [option1,option2,option3,option4,[answer]])
        return Question

n=int(input("Enter The Number Of Questions Store -"))

q=questio(n)
print(q)
'''
#inner class
'''
class student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
        self.lap=self.Laptop()#Laptop Class Object Call

    def show(self):
        print(self.rollno,self.name)
        self.lap.show()#Laptop class Show Method Call

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram='16GB'


        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student(1,'Hello')
s1.show()           
'''
#inheritance
'''
#1.single level inheritance
class abc:
    def f1(self):
        print("It's Parent Class")

class xyz(abc):
    def f2(self):
        print("It's Child Class")
a=abc()
b=xyz()
b.f1()

#2.multi level inheritance
print("~~~multi level inheritance~~~")
class abc:
    def f1(self):
        print("It's Parent Class")

class xyz(abc):
    def f2(self):
        print("It's Child Class")

class mno(xyz):
    def f3(self):
        print("It's Grand Chlid Class")

q=abc()
b=xyz()
c=mno()

c.f2()


#3.multiple inheritance
print("~~~multiple inheritance~~~")
class abc:
    def f1(self):
        print("It's Parent Class")

class xyz(abc):
    def f2(self):
        print("It's Child Class")

class mno(xyz,abc):
    def f3(self):
        print("It's Grand Chlid Class")

q=abc()
b=xyz()
c=mno()

c.f2()
c.f1()
'''
'''
#Example
# A Python program to demonstrate inheritance  
   
# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is  
# equivalent to "class Person(object)" 
class Person(object): 
       
    # Constructor 
    def __init__(self, name): 
        self.name = name 
   
    # To get name 
    def getName(self): 
        return self.name 
   
    # To check if this person is employee 
    def isEmployee(self): 
        return False
   
   
# Inherited or Sub class (Note Person in bracket) 
class Employee(Person): 
   
    # Here we return true 
    def isEmployee(self): 
        return True
   
# Driver code 
emp = Person("Geek1")  # An Object of Person 
print(emp.getName(), emp.isEmployee()) 
   
emp = Employee("Geek2") # An Object of Employee 
print(emp.getName(), emp.isEmployee()) 
'''
'''
class laptop:
    
    def __init__(self): #construtor 
        print("It's Laptop Module Of Init")
    
    def gaming(self):
         print("It's Gamming Laptop Moudle")

    def basic(self):
        print("It's Basic Laptop Module")

class config(laptop):

    def __init__(self): #construtor
        super().__init__() #access method of laptop class using super() key word or super() method
        print("It's Config Module Of Init")
        
    def cpu(self):
        print("It's Cpu Module")

    def ram(self):
        print("It's Ram Module")

l=config()
'''
'''
#multiple inheritance

class laptop:
    
    def __init__(self): #construtor 
        print("It's Laptop Module Of Init")
    
    def gaming(self):
         print("It's Gamming Laptop Moudle")

    def basic(self):
        print("It's Basic Laptop Module")

class config(laptop):

    def __init__(self): #construtor
        super().__init__() #access method of laptop class using super() key word or super() method
        print("It's Config Module Of Init")
        
    def cpu(self):
        print("It's Cpu Module")

    def ram(self):
        print("It's Ram Module")

class desktop(laptop,config):

    def __init__(self):
        print("It's Desktop Init")

    def hdmonitor(self):
        print("hdmonitor")

l=desktop()
'''
'''
class A: 
    def rk(self): 
        print(" In class A") 
class B(A): 
    def rk(self): 
        print(" In class B") 
class C(A): 
    def rk(self): 
        print("In class C") 
  
# classes ordering 
class D(B, C): 
    pass
     
r = D() 
r.rk()
'''
#Polymorphism
'''
class India(): 
	def capital(self): 
		print("New Delhi is the capital of India.") 

	def language(self): 
		print("Hindi the primary language of India.") 

	def type(self): 
		print("India is a developing country.") 

class USA(): 
	def capital(self): 
		print("Washington, D.C. is the capital of USA.") 

	def language(self): 
		print("English is the primary language of USA.") 

	def type(self): 
		print("USA is a developed country.") 

obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
	country.capital() 
	country.language() 
	country.type() 


def func(obj): 
	obj.capital() 
	obj.language() 
	obj.type() 

obj_ind = India() 
obj_usa = USA() 

func(obj_ind) 
func(obj_usa) 
'''


# a=int(input("enter row"))
# b=int(input("enter col"))

# for i in range(a):
#         for j in range(b):
#                 print("*",end="")
#         print()

#polymor
# class A:
#     def explore(self):
#         print("explore() method from class A")
 
# class B(A):
#     def explore(self):
#         super().explore()  # calling the parent class explore() method
#         print("explore() method from class B")
 
 
# b_obj = B()
# a_obj = A()
 
# b_obj.explore()

# Python program to 
# demonstrate protected members 


# Creating a base class 
class Base: 
	def __init__(self): 
		
		# Protected member 
		self._a = 2

# Creating a derived class	 
class Derived(Base): 
	def __init__(self): 
		
		# Calling constructor of 
		# Base class 
		Base.__init__(self) 
		print("Calling protected member of base class: ") 
		print(self._a) 
		
obj1 = Base() 

# Calling protected member 
# Outside class will result in 
# AttributeError 
print(obj1._a) 

obj2 = Derived() 

