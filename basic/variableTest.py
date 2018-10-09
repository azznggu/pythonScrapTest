
# assign -> identical

a =[1,2,3]

b = a

#check id, it points same list.
print(id(a))
print(id(b))

b.append(4)

print(b)
print(a)


#copy
##1. [:]
b = a[:]
b[1] = "a"

print(b)
print(a)


##2. use copy module
from copy import copy
a = copy(b)

print(b)
print(a)


#way to make var
##tuple example

a,b = ("a","b")

#same as below
(a,b) ='a','b'
print(a,b)

##list example
[a,b] = ['a','b']

print(a)
print(b)

## exchange value
a = 3
b = 5
a,b = b,a
print(a)
print(b)


