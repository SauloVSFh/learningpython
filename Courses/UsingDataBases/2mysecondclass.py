#In this class I'm going to create a class and two instances/ objects in the same class

class mysecondclass():
    x = 0
    name = ''
    def __init__ (self, passin): #self stands for what is inside the function. It could be anything (ex = saidghbapfig)
        self.name = passin
        print(self.name, ", constructed")
    def method(self):   #thats my method to create other type of object
        self.x += 1
        print("Now you have other instance, and the first was destructed: ",self.x)
    def __del__ (self):
        print("===================destructed====================")


#When creating a new class you can inherit all the capabilities of an existing class
#subclasses - there might be a hirearchy of classes

class mythirdclass(mysecondclass): #that creates a new class and pass in the capabilities of the existing class
    money = 200
    def yourichmethod(self): #other method but within mythirdclass only
        self.money += 1000
        self.method () #it calls line 9 and changes self.x
        print(self.name, ' has ', self.money, ' euros.' )

anything = mysecondclass("Saulo") #it will be passed in the init function automatically
print(type(anything))
anything.method() #it does NOT destruct the object. Two instances of the same class.
print(type(anything))
something = mysecondclass("Tiago")
something.method()
something.method()
anybody = mythirdclass("Luciana")
 #Now I can call methods within mysecondclass because mythirdclass inherits the capabilities
anybody.method() #self.x = 1
anybody.yourichmethod() #self.x = 2, self.name = Luciana and self.money = 1200. All of them are stored within anybody.
print(dir(anybody))
print(anybody.money)


# REVIEW:
# Class - template
#atribute - data
#method - function of the class
#object - what we construct from the class
#constructor - code to create the object
#inheritance new class with additional capabilities

# REVIEW:
#anything, something, and anybody are objects
#What is inside this objects are instances -> self.name, self.x, self.money
#money, x and name are attributes
