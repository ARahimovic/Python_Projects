'''
# Exercise 5: Dictionary Operations
# Task: Create a program that:
# 1. Creates an empty dictionary to store student information
# 2. Asks the user to input the names and scores of 3 students
# 3. Prints the dictionary
# 4. Prints the name of the student with the highest score
# 5. Calculates and prints the average score of all students
# 6. Asks the user for a student name and prints their score if the student exists


NOTE: Dictionaries are ordered in Python 3.7 and later. If you are using an earlier version of Python, the order of the dictionary may not be the same as the order in which you entered the elements.

to define a dictionary we use the following syntax
myDict = {
    key1: value1,
    key2: value2,
    key3: value3
}

or we can use the dict() constructor
myDict = dict(key1=value1, key2=value2, key3=value3)

to add a new element to the dictionary we use the following syntax
myDict[newKey] = newValue
or
myDict.update({newKey: newValue})

to remove an element from the dictionary we use the following syntax
del myDict[key]


to get the value of a key we use the following syntax
value = myDict.get(key)
or 
value = myDict[key]

to get the keys of a dictionary we use the following syntax
keys = myDict.keys()
these keys are returned as a dict_keys object which is a view object that displays a list of all the keys in the dictionary
and automatically updates when the dictionary changes


to get the values of a dictionary we use the following syntax
values = myDict.values()
these values are returned as a dict_values object which is a view object that displays a list of all the values in the dictionary
'''

if __name__ == "__main__":
    myDict = {}
    for _ in range(0,3):
        name = input("enter student name")
        score = int(input('enter score'))
        myDict[name] = score
    
    print(myDict)
    print(max(myDict, key=myDict.get))
    
    total_sum = sum(myDict.values())
    average = total_sum / len(myDict)
    print(f"average = {average:.2f}")
    
    student_name = input("enter student name to search : ")
    if student_name in myDict.keys():
        print(f"student {student_name} score = {myDict.get(student_name)}")
    else:
        print("student name is not in dict")
        
    
    
    