''''''
'''
Dictionary is an associated type of data structure.
# In the associated data structure, we can access the data using the associated key values,dictionaries are one of the associated data structure.
When we have a huge amount of data or when we want to fetch data in an efficient way or fast way then we can assign a key to every value.
we can assign a key to every value.
Dictionary will be represented in curly brackets  as keys should not repeated, as sets values does not repeat.
In Dictionary the data is distinguished between two things
One is key and the other one is value,here values are denoted by keys.
In Dictionary keys are immutable and values are mutable.
As keys cannot be changed and values can be changed. 

# Different ways of creating dictionaries in python.It is the unordered collections of items and it contains keys and value pair.
# 1.Using curly bracket syntax
# 2.Creating empty dictionary and fill in the entries one by one.


dictionary get method purpose

	-get() method is used in Python to retrieve a value from a dictionary. dict. get() returns None by default if the key you specify cannot be found. 
	-With this method, you can specify a second parameter that will return a custom default value if a key is not found.dictionary get method purpose


'''
mail_address = {'amul' : 'amul@gmail.com','john' : 'john@gmail.com','anny' : 'anny@gmail.com'}
print(mail_address)
# if we want only dictionary keys
print(mail_address.keys())
# if we want only dictionary values
print(mail_address.values())
# how to access values using keys in dictionaries
print(mail_address['amul'])

# creating dictionary in dict way
dict()
print(dict)
# copying dictionary
num = {1:'one',2:'two',3:'three'}
# if i want to copy this num dictionary to another i.e.numbers
numbers = dict(num)
print(numbers)
# to find out the length of the dictionary
print(len(num))
# Delete a key value pair from the dictionary
del num[2]
print(num)
# if we want to check whether a key is present in the dictionary or not
print(1 in num)
print(3 in num)
print(2 in num)


# if we want to check the value of key is correct or not?
dict1 = {'a':2,'b':2,'c':3}
for k,v in dict1.items():
    if k == 'b' and v == 2:
        print('True')
    else:
        print('False')

# It can be done in other way also
dict1 = {'a':2,'b':3,'c':3}
for i in dict1:
    if i == 'b' and dict1.get(i) == 3:
        print(True)
    else:
        print(False)

# Dictionery way
str = 'sindhu'
dict={}
for i in str:
    keys=dict.keys()
    if i in keys:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)

# here we can get the same result while using" from collection import Counter "
