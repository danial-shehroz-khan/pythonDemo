ABSTRACTION

Function is defined in abstract class with defination and pass keyword
Inherit class has to use those fucntion at all cost
In Parent class has to be inherited by abc
From abc import abstact method

from abc import abstractmethod,ABC

class BMW(ABC):

    def __init__(self,make,model,year):
        self.make=make 
        self.model=model
        self.year=year
    
    def start(self):                   #This function will also be inherited by the child class
        print("Starting the Car")
    
    def stop(self):                    #same as above comment
        print("Stopping the Car")
    
    @abstractmethod
    def drive(self):
        pass



class ThreeSeries(BMW):
    
    def __init__(self,cruiseControlEnabled,make,model,year):
        #BMW.__init__(self,make,model,year)  1)))))))we have to add super instead of BMW
        super().__init__(make,model,year)  #we wont be needing "self" any more
        self.cruiseControlEnabled=cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)  

    def drive(self):
        print ("Three series is Driven")

class FiveSeries(BMW):
    
    def __init__(self,parkingAssistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)   #InvokeTheClassYouWantToInherItFeaturesFrom
        self.parkingAssistEnabled=parkingAssistEnabled
    
    def display(self):
        print(self.parkingAssistEnabled)

    def stop(self):                    #same as above comment
        super().start()              #concept 2 using function of parent class form child class
        print("Button Start")

    def drive(self):
        print("Five Series is driven")

threeSeries=ThreeSeries(True,"BMW","328i","2018")

print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()

         
fiveSeries=FiveSeries(True,"BMW","528i","2020")

print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)
fiveSeries.start()
fiveSeries.stop()
fiveSeries.display()

------------------------------------------------------------------------------

#2)Assignement 
from abc import abstractmethod,ABC

class TouchScreenLaptop(ABC):
   
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass



class HP(TouchScreenLaptop):
    
    def scroll(self):
        print("You have scrolled")

    @abstractmethod
    def click(self):
        pass

class HPNotebook(HP):
    
    def scroll(self):
        print("You have scrolled")

    
    def click(self):
        print("You have clicked")



HP=HPNotebook()
print(HP.scroll())
print(HP.click())
         
