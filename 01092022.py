'''
What is python?
Python is an interpreted,high level,dynamically typed,general purpose programming language.
* Interpreted: Here translation of code is done line by line.
* High level:It is the language which humans can understand.
* Dynamically typed: It means the type of variable and expression is decided during run time.
* General purpose programming language: It means it is designed to be used in a range of applications including
data science,software and  web development,automation etc.
==================================================================================================================================================================
Features of python?
* Python Is a Case-Sensitive Language
   It's the differentiation between lower- and uppercase letters.
* It is an object oriented language as everything in python is an object.
* In python the programmer need to follow PEP 8 standards,these are standards which are to be followed while writing the code.
===============================================================================================================================================================
Advantages of python?
* It is free and open source.
* It is easy to code compared to other programming languages like Java,C++.
* Python supports to develop graphical user interfaces.
* Python language is also a portable language.
For example, if we have Python code for windows and if we want to run this code on
other platforms such as Linux, Unix, and Mac then we do not need to change it,
we can run this code on any platform.
=====================================================================================================================================================================
Disadvantages of python
* We can consider python programming language as slow because of two reasons
----as code is executed line by line and
----here datatype is decided during the runtime.
*Not suitable for Mobile and Game Development
Python is mostly used in desktop and web server-side development.
It is not considered ideal for mobile app development and game development due to the consumption of more memory and
its slow processing speed while compared to other programming languages.
* we can see runtime errors in python.
=============================================================================================================================================================
Why Python is so popular now a days?
Python has been used in web development, data analytics, machine learning, data science, data engineering,
and even machine learning and artificial intelligence. Many top businesses and software companies depend on Python
including Facebook, Google, Netflix, Instagram, and others.
==========================================================================================================================================================================
Variables:
What is meant by variable?
It is a reference name or pointer to an object.
Ex: x = 4
===============================================================================================================================================================================
x = 10. Explain in detail for CRUD operations
CRUD full form is Create,Retrieve,Update,Delete
If 10 i.e.value is assigned to it is create
if we want to print x we get the output as 10 that is retrieve
if we update the value of x as 5 it is update
if we use del x then variable is deleted.
====================================================================================================================================================================================
VARIABLE SCOPES OF LEGB RULE
The LEGB rule names the possible scopes of a variable in Python: Local, Enclosing, Global, Built-in.
Scopes are created with functions, classes, and modules.
Python searches namespaces in this order to determine the value of an object given its name.
Here we should know what is namespace,namespace ensures the names we use should be unique and should not lead to conflict.
Python contains multiple namespace.
* Local    : It contains names defined inside the current function.
* Enclosed : It contains names defined inside any and all enclosed function. we can find enclosed scope in the nested function.
* Global   : It contains names defined at the top level of the script or module.
* Builtin  : It contains built-in names,we can access wherever we want, no need to define anything, we can directly use their names.
========================================================================================================================================================================================

'''
# Swapping of 2 variables:
x = 5
y = 6
x,y = y,x
print(x)
print(y)

# =================================================================================================================================================================
'''
Memory Management in Python ?
Reference variables gets memory in stack.Objects will get memory in private heap space.
In private heap space we cannot get access directly.
we can access through reference id only.
This id or memory given to object is done by python memory manager.
Python memory manager is one type of program and its responsibility is to allocate memory from private heap space.
Any object which is not referred by any name i.e the garbage block and it is eligible to release through garbage collector.
When it runs we can't say,but when necessary python calls garbage collector.Garbage collector releases the garbage blocks.
So that if we need any memory in future, we can reuse it.
=====================================================================================================================================================================
Assigning value to multiple variables?
Python assigns values from right to left. When assigning multiple variables in a single line, 
different variable names are provided to the left of the assignment operator separated by a comma.
===========================================================================================================================================================================
Tokens in Python. Explain all types
Smallest individual unit in python program where all statements and instuctions in program are built with tokens.
1.Identifiers : Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore.
                An identifier cannot start with a digit. 
                Keywords cannot be used as identifiers. 
                We cannot use special symbols like !, @, #, $, % etc. 
                An identifier can be of any length.
2.Literals : literals are constants used in python or in other words this is the data which is stored in a variable
3.Keywords : Python keywords are special reserved words that have specific meanings and purposes and
             can't be used for anything but those specific purposes.
4.Punctuators : These are the symbols that used in Python to organize the structures, statements, and expressions.
                Some of the punctuators are: [ ] { } ( ) @ -= += *= //= **== = , etc.
5.Operators : These are used to do operations on variables and values.
=============================================================================================================================================================
IDE Shortcuts
Shortcut                                                 Action
Double Shift                           Search Everywhere
                                       Quickly find any file, action, class, symbol, tool window, or setting in PyCharm, in your project, and in the current Git repository.

Ctrl+Shift+A                           Find Action
                                       Find a command and execute it, open a tool window, or search for a setting.

Alt+Enter                              Show Context Actions
                                       Quick-fixes for highlighted errors and warnings, intention actions for improving and optimizing your code.

F2                                     Navigate between code issues

Shift+F2                               Jump to the next or previous highlighted error.

Ctrl+E                                 View recent files
                                       Select a recently opened file from the list.

Ctrl+W                                 Extend or shrink selection

Ctrl+Shift+W                           Increase or decrease the scope of selection according to specific code constructs.

Ctrl+/                                 Add/remove line or block comment

Ctrl+Shift+/                           Comment out a line or block of code.

Alt+F7                                 Find Usages
                                       Show all places where a code element is used across your project.
                                       
===============================================================================================================================================================
Explain in detail about all operators?
Operators are used to do various operations on variables.
There are different types of operators
1.Arithmetic Operator:Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.'''
                      # There are 7 arithmetic operators in Python :
# Addition
x = 3
y = 6
print(x+y)

# Subtraction
x = 5
y = 2
print(x-y)

# Multiplication
x = 5
y = 7
print(x*y)

# Division
x = 65
y = 5
print(x/y)

# Modulus
# If we want remainder part we use modulus
x = 6
y = 3
print(x%y)

# Exponentiation
# if we want 2 to the power of 3 like 2*2*2
print(2**3)

# Floor division
# If the answer comes in decimal we can convert it into integer.
x = 5
y = 2
print(x//y)
'''
Operators precedence:It guides the order in which these operations are carried out,
                     when there are multiple operators written in single line of code.
                     The correct order of precedence is given by PEMDAS 
                     which means Parenthesis (), Exponential **, Multiplication *, Division /, Addition +, Subtraction -.
                     '''
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print(e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print(e)

e = (a + b) * (c / d)   # (30) * (15/5)
print(e)

e = a + (b * c) / d      #  20 + (150/5)
print(e)

'''2.Logical Operator:
In Python, Logical operators are used on conditional statements (either True or False). They perform Logical AND, Logical OR and Logical NOT operations.

OPERATOR	                  DESCRIPTION	                                SYNTAX
and	Logical AND:            True if both the operands are true	            x and y
or	Logical OR:             True if either of the operands is true	        x or y
not	Logical NOT:             True if operand is false	                     not x
'''



'''
3.Comparision/Relational Operator:Relational operators are used for comparing the values. 
It either returns True or False according to the condition. Ex:=,<,>,<=,>=
4.Assignment Operator:It assigns the value of its right-hand operand to a variable, a property, or an indexer element given by its left-hand operand
5.Membership Operator:We use membership operators to check whether a value or variable exists in a sequence (string, list, tuples, sets, dictionary) or not
In Python, there are two membership operators. (in, not in).
6.Identity Operator:Identity operators are used to comparing the objects 
if both the objects are actually of the same data type and share the same memory location.

=======================================================================================================================================================
Keywords : Python keywords are special reserved words that have specific meanings and purposes and
             can't be used for anything but those specific purposes.
                                       
==============================================================================================================================================
DATA TYPES
===============================================================================================================================================
1. DATA TYPES IN PYTHON
    1.NUMBERS ---> python supports four different data types .they are int,long,float,comolex

    2.STRING ---> strings are amongst the most popular type in python.we can create them simply enclosing charecters in quotes
                  python threats single quotes the same as double quotes.

===============================================================================================================================================----------------------------------------------------------------------------------------------------------------------------
2.DATA STRUCTURES IN PYTHON
    list,tuple,dictionary and set

    list ----> list is a mutable data structure
               the list is a most versatile data type available in python which can be 
               written as a list of comma separated values b/w square brackets

    tuple ----> tuple is immutable data structure 
                tuples are sequences , just like lists

    dictionary ----> dictionary is a mutable data structure 
                    dictionary in python is an unorderd collection of data values

    set ----> a set is an unodered and mutable collection of unique elements

============================================================================================================================================================
list vs tuple?

    list
        list is mutable
        implication of iterations is time- consuming
        list consume more memory
        list have several bulit in methods like append,count,extend,index,insert,reverse etc

    tuple
        tuples are immutable
        The implication of iterations is comparatively faster
        tuple consume less memory as compared to the list
        tuple does not have many bulit in methods
          tuple functions like min,max,len etc
====================================================================================================================================================          

Typecasting:
It is a method to convert the variable data type into a certain data type for the operation required to be performed by users.
There are two types of type casting in python:
1.Implicit typecasting:
 It converts data type into another data type automatically.No need of user intervention in this.
2.Explicit typecasting:
 It converts the variable datatype into certain datatype in order of the operation required.Here user invovement will be there.'''