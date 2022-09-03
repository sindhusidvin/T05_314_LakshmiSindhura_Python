''''''

'''
Importance of Loops
Loops are important in Python or in any other programming language as they help you to execute a block of code repeatedly.
===============================================================================================================================================================
Explain while loop. 
It is used to iterate over a block of code as long as the text expression (condition) is satisfied.
We generally use the while loop when we don't know the number of times to iterate beforehand.
==============================================================================================================================================================
Explain for loop. 
It is used for iterating over a sequence(i.e.either a list, a tuple, a string,range)
=============================================================================================================================================================

'''
#  Write while loop statement to print the following series:
# 10, 20, 30 … … 300
i=10
while i<=300:
    print(i)
    i=i+10

#  Write a while loop statement to print the following series
105, 98, 91 ………7
i=105
while i>=7:
    print(i)
    i=i-7

# write a for loop statement to print range of 10 numbers
for i in range(10):
    print(i)

# write a for loop statement to print range between 11 to 21 with a gap of 2 numbers
for i in range(11,21,2):
    print(i)

# write a for loop statement to print range of first 20 numbers where to print the numbers other than divisible by 5.
for i in range(1,21):
    if i % 5 != 0:
        print(i)

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 22
# Output: [1,3]
# Explanation: Because nums[1] + nums[3] == 22, we return [1, 3].
nums = [2,7,11,15]
def two_sums(nums,tar):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == tar:
                return [i,j]

print(two_sums([2,7,11,15],22))


