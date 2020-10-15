class myfirstclass():
    attribute = 0
    def __init__ (object):
        print("This is a message to state the object is constructed!")
    def method(object):
        object.attribute = object.attribute + 1
        return object.attribute
    def __del__ (object):
        print("This is a message to state that the object was destructed!")
        #It prints at the end of the program or when I destroy the variable


myobject = myfirstclass() #it will build myobject and the state within the init method.
print(myobject.method()) #it stands for myfirstclass.method(). it Returns 1
print(myobject.method()) #it returns 1+1= 2
print(myobject.method()) #it returns 3
#By doing that I'm destructing the object which before belonged to the class myfirstclass and now it's an integer
myobject = 50
print('Myobject is now: ', myobject, 'and the object was destructed before the end of the program.')
