''''''
'''What is decision making? and its different scenarios
It is anticipation of conditions occurring while execution of the program and specifying actions taken according to the conditions.
To handle those programs we use conditionals like if,else,elif,nested if.
* if condition:It is the most simple decision-making statement. It is used to decide whether a certain statement or block of statements
will be executed or not i.e if a certain condition is true then a block of statement is executed otherwise not.
* else condition: The if statement alone tells us that if a condition is true it will execute a block of statements and
 if the condition is false it won’t. But what if we want to do something else if the condition is false. Here comes the else statement.
  We can use the else statement with if statement to execute a block of code when the condition is false.
* elif condition:The elif is short for else if. It allows us to check for multiple expressions. If the condition for if is False ,
 it checks the condition of the next elif block and so on. If all the conditions are False , the body of else is executed.
* nested if condition: A nested if statement is an if statement placed inside another if statement.
  Nested if statements are often used when you must test a combination of conditions before deciding on the proper action.

'''
# Write a program to check whether the last digit of a number (entered by user) is divisible by 3 or not
user=input("Enter the Number: ")
last_digit=int(user[-1])
print(last_digit)
if last_digit % 3 == 0:
    print("Last digit is divisible by 3")
else:
    print("Last digit is not divisible by 3")


# Write a program to find the sum of all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
if num1<num2:
    while (num1<num2):
        if num1 > (num1 + 1):
            if num1%2==0:
                print(num1)
        num1=num1+1
else:
    if num1>num2:
        while (num1>num2):
            if num2%2==0:
                print(num2)
            num2=num2+1



