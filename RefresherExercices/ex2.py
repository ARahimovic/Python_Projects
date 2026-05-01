'''

# Exercise 2: String Manipulation
# Task: Ask the user to enter a sentence. Then:
# 1. Print the sentence in all uppercase
# 2. Print the sentence in all lowercase
# 3. Print the number of characters in the sentence
# 4. Print the number of words in the sentence
# 5. Print the sentence with all occurrences of the letter 'a' replaced with '@'
# 6. Print the sentence with each word capitalized
# 7. Print the sentence in reverse order



NOTE : all string methods return a new string. They don't modify the original string.
'''

user_input = input("enter a full sentence :")

print("upper case : " + user_input.upper())
print("lowerc case: "  + user_input.lower())

print(f"lenght of string : {len(user_input)}")

words = user_input.split()
print(f"number of words in the sentence {len(words)}")

newStr = user_input.replace("a","@")
print(newStr)

# this wil captialize only the fist letter of the sentence
print("capitalize only the first letter")
print(user_input.capitalize())
# this will captialize the first letter of each word in the sentence
print("capitalize each word")
print(user_input.title())
#reverse string using slicing
reverse_str = user_input[::-1]
print(f"reverse string : {reverse_str}")
