dic= {'a':1, 'b':[2,3,4], 'c':'ccc'}

#dictinary related functions

#1. keys - get key lists of dictionary.
print(dic.keys())
for key in dic.keys() :
    print(key)


#2. values - get value lists of dictionary.
for val in dic.values():
    print(val)

#3. items - key & value set
for item in dic.items() :
    print(item)

#4. clear - delete all item? of dictionary
dic.clear()
print(dic)

#5. get value by key
dic= {'a':1, 'b':[2,3,4], 'c':'ccc'}

# it is same as dic['a']
gotVal = (dic.get('a'))
print(gotVal)

#6. in - check if key is in dic
result = 'a' in dic
print(result)


#practice
dic = {'name':'a','birth':1128, 'age':30}


a = {'A':90, 'B':80, 'C':70}
print(a.get('B'))

items = a.items()
print(items)

a = {'A':90, 'B':80}
print(a.get('C', 'nope'))