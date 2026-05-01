# Exercise 6: Advanced List Comprehension
# Task: Use list comprehension to:
# 1. Create a list of tuples containing numbers from 1-10 and their squares
# 2. Create a list of numbers from 1-20 that are divisible by either 2 or 3
# 3. Create a list of all possible combinations of two letters from 'abcd'
# 4. Create a flat list from a list of lists [[1,2,3], [4,5,6], [7,8,9]]

'''
NOTE: list comprehension follow this general syntax 
[expression for item in iterable if condition]
'''


if __name__ == "__main__":

    
    squared_list = [(x,pow(x,2)) for x in range(1,11)]
    print(f"squared_list : {squared_list}")

    myList = [x for x in range(1,21) if (x%3 == 0) or (x%2 == 0)]
    print(f"list of elements divisable by 2 or 3 : {myList}")

    myStr = 'abcd'
    combinations = [x+y for x in myStr for y in myStr if x!=y]
    print(combinations)

    listofLists = [[1,2,3], [4,5,6], [7,8,9]]
    flatList = [x for lists in listofLists for x in lists] 
    print(flatList)
