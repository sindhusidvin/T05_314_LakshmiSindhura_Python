''''''
'''
What are control statements?
Control statements in python are used to control the order of execution of the program based on the values and logic.
There are three types of control statements
Break 
Continue 
Pass
Break: It is used to control the sequence of the loop. If we want to terminate a loop and skip to the next code after the loop break will help.
Continue: It is used to end the current iteration in a for loop(or a while loop) and continues to the next iteration.
Pass: It is used as a placeholder for future code. When the pass statement is executed,nothing happens,but you avoid getting an error
    when empty code is not allowed.Empty code is not allowed in loops, function definitions,class definitions or in if statements.


'''
# write a program to stop numbers greater than 100
numbers = [10,40,120,230]
for i in numbers:
    if i > 100:
        break
    print(i)

# write a program to skip number 40
numbers = [10,40,120,230]
for i in numbers:
    if i == 40:
        continue
    print(i)

# write a syntax for pass statement
months = ['January', 'June', 'March', 'April']
for monday in months:
    pass
print(months)


