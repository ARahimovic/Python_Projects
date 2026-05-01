# Exercise 8: Using map() and filter()
# Task: Write a program that:
# 1. Asks the user to input 10 numbers separated by spaces
# 2. Uses map() to convert the input to integers
# 3. Uses map() to find the square of each number
# 4. Uses filter() to keep only the even numbers
# 5. Uses filter() to keep only the numbers greater than the average of all numbers
# 6. Combines map() and filter() to find the sum of the squares of all even numbers


#input will give a string of words separated by spaces
#split will split the words in a list
#we use map to map a function to every item on an iterable, this returns a map object, need to map it back to list
numbers = list(map(int, (input("enter 10 numbers separated by a space").split())))
print(f"numbers = {numbers}")

#squared_members = [x**2 for x in numbers]
squared_members = list(map(lambda x : x**2, numbers))
print(f"squared_members = {squared_members}")

#keep only even numbers
even_numbers = list(filter(lambda x: x %2 == 0, numbers))
print(f"even_numbers = {even_numbers}")

#keep only numbers greater than average
average = sum(numbers) / len(numbers)
greaterThen = list(filter(lambda x:x>average, numbers))
print(f"greater the the average {average} = {greaterThen}")

# Combines map() and filter() to find the sum of the squares of all even numbers 
#like from scratch and not used already calculated lists
even_squares = list(map(lambda x:x**2, filter(lambda x:x%2 ==0, numbers)))
print(f"even_squares = {even_squares}")
print(f"sum = {sum(even_squares)}")

