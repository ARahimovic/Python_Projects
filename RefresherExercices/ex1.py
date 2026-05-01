'''

# Exercise 1: Basic Input and Output
# Task: Write a program that asks for the user's name, age, and favorite color.
# Then print a personalized message using three different string formatting methods:
# 1. f-strings
# 2. .format() method
# 3. % operator formatting

'''
name = input("enter name : ")

age = int(input("enter Age : "))

color = input("enter color : ")


#using f-string
print(f"my name is {name}, I am {age} old, my favorite color is {color}")
#using string format
print("my name is {}, I am {} old, my favorite color is {}".format(name,age,color))

print("my name is %s, I am %d old, my favorite color is %s"%(name,age,color))


