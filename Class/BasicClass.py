class Product:    #defining the class
    def __init__(self):         #self constructor
        self.name='Iphone'
        self.description='It is awesome'
        self.price=700

p1=Product()        #making a object

print(p1.name)      
print(p1.description)   
print(p1.price)

-----------------------------------------------------------------------
2)Paramterized Constructor

course name and rating    shortcuts CTRL+K+C/U

class Course:

    def __init__(self,name,rating):
        self.name=name
        self.rating=rating

 
c1=Course('Daniel',[1,2,3,4,5])
print(c1.name)
print(c1.rating)

c2=Course("IFFIFHA",[7,8,9,10,11])
print(c2.name)
print(c2.rating)

c1.name='Farhan'
print(c1.name)

----------------------------------------------------------------------------------------
3)--Define a instance method.(Function for a Class)

class course:
    
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating 

    def average(self):
        numberOfRating=len(self.rating)
        average=sum(self.rating)/numberOfRating
        print("Average Rating for",self.name,"Is",average)


c1=course('Daniel',[1,2,3,4,5])

print(c1.name)
print(c1.rating)
c1.average()

-------------------------------------------------------------------------------
Create Getter and Setter method  (Accessor and mutator concept)

Programmer name salary technology

class Programmer:

    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.salary=sal

    def getSalary(self):
        return self.salary
    
    def setany(self,anyy):
        self.any=anyy

    def getany(self):
        return self.any
 

p1=Programmer()

p1.setName('Name')
p1.setSalary(100)
p1.setany(20)



print(p1.getName())
print(p1.getSalary())
print(p1.getany())


---------------------------------------------------------------------------------

5 Define instance method.


class Product:    #defining the class
    def __init__(self):         #self constructor
        self.name='Iphone'
        self.description='It is awesome'
        self.price=700

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

c1=Product()
c1.display()

-------------------------------------------------------------------------
6 Define static field    

You can access them without objects and they are constants

class students:

    major='CSE'

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

s1=students(160341,'Daniel')
s2=students(160994,'IJAZ')
print(s1.major)     #they are constant
print(s2.major)     #they are constant
print(students.major)


7 Count the number of Objects(instances)

class ObjectsCounter:

    numberOfObjects=0

    def __init__ (self):
        ObjectsCounter.numberOfObjects+=1  #classname.constantfield

theydonthaveselfastheyAreConstantField
    @staticmethod
    def displayCount():   
        print(ObjectsCounter.numberOfObjects)

o1=ObjectsCounter()
o2=ObjectsCounter()
ObjectsCounter.displayCount()  

-----------------------------------------------------------------------------

8 Create a inner CLass

Question Class called Car and it will contain engine class

class Car:    #defining the class
    def __init__(self,make,year):         #self constructor
        self.make=make
        self.year=year

    class engine:

        def __init__(self,number):
            self.number=number
        def start(self):
            print("Engine Started")

c=Car("BMW",2017)

#we need to use objetc of outer class to call inner class 
e=c.engine(123)   #calling class again
print(e.start())

#we need to use object of ourter class to invoke the instance of inner class

