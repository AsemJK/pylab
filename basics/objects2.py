#The type of an object is itself an object, known as object’s class.

#example
a = {2,3,5}
print(type(a)) #<class 'set'>
#print "set" only
print(type(a).__name__) #what is  __name__  ?
# __name__ is a special attribute of a class, it returns the name of the class
