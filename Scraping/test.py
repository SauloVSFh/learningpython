class myfirstclass():
    attribute = 0
    def method(object):
        object.attribute = object.attribute + 1
        return object.attribute

myobject = myfirstclass()

print(myobject.method()) #it stands for myfirstclass.method()
print(myobject.method())
print(myobject.method())
print(myobject.method())
print(myobject.method())
