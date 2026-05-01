'''
# Exercise 4: List Comprehension Basics
# Task: Use list comprehension to:
# 1. Create a list of squares of numbers from 1 to 10
# 2. Create a list of only the even numbers from 1 to 20
# 3. Create a list of numbers from 1 to 30 that are divisible by 3
# 4. Create a list where each element is "Number X" where X is a number from 1 to 5

NOTE: in order to copy a list, we cannot use
list2 = list1 because list1 will be a reference to list2, and changing list1 is equivalent ot changing list2 and vice versa

instead we use either:

list2 = list1.copy() 
list2 = list(list1)  
list2 = list1[:]


to join two lists together  we can use the + operator
list3 = list1 + list2

or we can use the extend() method
list1.extend(list2)


###### append is not recommanded ##

or we can use the append() method
list1.append(list2)

using append will not append each element of list2 to list1, but will append the list2 as a single element to list1

instead we would have to do 
for x in list2:
    list1.append(x)
'''

square_list = [pow(x,2) for x in range(1,10)]
print(square_list)

even_list= [x for x in range(1,20) if x%2 == 0]
print(even_list)

divideBythree = [x for x in range(1,30) if x%3 == 0]
print(divideBythree)

numberX= ['Number X' for i in range(1,5)]
print(numberX)
