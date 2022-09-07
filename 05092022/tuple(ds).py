''''''
'''
Tuple is also a linear type of data structure which contains collection of elements.
It contains elements in ordered way.
Tuple is immutable,here we cannot change the values,as if we change even one value the memory address of tuple is changed.
Tuple is represented in paranthesis.
Tuple does not support the item assignment.
For example 


So here we can discuss the thing like list vs. tuple
we can say like when we have a list, list of elements or items we know that there is no possibility of modifying the values.
Since we dont change the values in tuple,the iteration in tuples is faster than list.
Memory allocation in list is more than the tuple.
In list functions like append,clear,add,insert,delete,edit,change,index,pop,count etc.,
But in tuple only two functions like count and index.
  
'''
tup1 = (21,36,14,25)
print(tup1[1]) #indexing
print(tup1.count(21)) #count i.e count of element present in tuple
# here print function executes the tuple count as count has no in place modification that's why it return the output.

# if we want any value from the tuple
tuple1 = ('a','b','c','d','e','f','g','h','i')
x1 =(tuple1[3])
x2 =(tuple1[-4])
print(x1,x2)
