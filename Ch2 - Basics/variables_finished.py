# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print (myint)

# to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])
# use slices to get parts of a sequence
print(mylist[1:4:2])
# you can use slices to reverse a sequence
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict["one"]) 

# ERROR: variables of different types cannot be combined
#print ("string type " + 123)
print ("string type " + str(123))

# Global vs. local variables in functions
def someFunction():
    #global mystr
    mystr = "def"
    print (mystr)

someFunction()
print (mystr) 

del mystr
print (mystr)
