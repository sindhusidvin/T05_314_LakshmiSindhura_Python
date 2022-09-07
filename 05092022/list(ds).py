''''''
'''
Data or information used in our program need to store in our system. Various ways to store data in our system that is
using file or folder but if amount of data is large  we cannot use file or folder to store the data for that we can go to the database.
Before storing this data to the database,we need to organise this data or we need the store this data in a particular format 
and this format is called as data structures.
Data Structures is of 2 types
1.Linear Data Structure
2.Associated Data Structure
we know about linear data structures like list and tuples  where the data is stored in the linear order and
# we can access the data using the location or index of the data  and there is an another data structure called as associated data structure.
# In the associated data structure, we can access the data using the associated key values,dictionaries are one of the associated data structure.


List: 
List holds a collection of elements.
List is a linear type of data structure.
It is represented in Square brackets.
Elements in the list will be in ordered format.
One of the important feature of list is mutable.Mutable means if we change any element in the list the address of the list wont be changed.
'''
# How to reverse a list:
# There are 2 ways to reverse a list one way is to use reverse function
# list1 = [200,500,300,100,400]
# list1.reverse()     # It is a list method it will change the original.list1.reverse() don't have any return type.
# print(list1)

# list1 = [200,500,300,100,400]
# x = list1[::-1]  # This is the sequence operation in slicing.Slicing will create a copy of that object or variable it will not affect the original one.
# print(x)

# How to concatenante two lists:
# list2 = ['M','na','i','si']
# list3 = ['y','me','s','ndhu']
# list5 = []
# for i in range(len(list2)):
#     for j in range(len(list3)):
#         if i == j:
#             list5.append(list2[i] + list3[j])
# print(list5)
'''
List comprehension:
l1 = [expression for e in sequence] #here for loop runs in sequence, here sequence means string,list,tuple.
The for loop iterates between each elements and that many times loop will be execute the expression for how many elements present in the sequence.
The result of the expression is the element of the list.

'''
# li1 = [54,76,23,65,98,23,67,54,87,65,34]
# l2 = [i for i in li1 if i%2==0]
# print(l2)



# here we can use list comprehension,we can use list comprehension with the Zip()
# list4 = [i + j for i, j in zip(list2,list3)] #here zip is used to map the similar index and helped to concatenate the list 2 & list 3
# print(list4)

# Turn every item of a list into its square
# list6 = [1,2,3,4,5,6,7]
# result = []
# for i in list6:
#     result.append(i * i)
# print(result)




