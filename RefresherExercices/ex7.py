# Exercise 7: Dictionaries and List Comprehension
# Task: Create a program that:
# 1. Asks the user to input 5 words
# 2. Creates a dictionary where the keys are the words and the values are their lengths
# 3. Creates a dictionary where the keys are the words and the values are the words reversed
# 4. Creates a dictionary where the keys are the words and the values are lists of the characters in each word

'''
NOTE: dictionaries also can be defined using list comprehension 

{key_expression: value_expression for item in iterable if condition}

'''

words = input("enter 5 words seperated by a space").split()

dictLength = {}
dictReversed = {}
dictList = {}
for word in words:
    dictLength[word] = len(word)
    dictReversed[word] = word[::-1]
    dictList[word] = [x for x in word]

print(f"dict length {dictLength}")
print(f"dict reversed {dictReversed}")
print(f"dict list {dictList}")


#solving using dict comprehension 
dictLength = {word:len(word) for word in words}
dictReversed = {word:word[::-1] for word in words}
dictList = {word:list(word) for word in words} 
## or 
#dictList = {word:[for x in word] for word in words} 

print(f"dict length {dictLength}")
print(f"dict reversed {dictReversed}")
print(f"dict list {dictList}")


