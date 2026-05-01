'''

# Exercise 3: List Creation and Basic Operations
# Task: Create a program that:
# 1. Creates an empty list
# 2. Asks the user to input 5 numbers one by one and adds them to the list
# 3. Prints the original list
# 4. Prints the list sorted in ascending order
# 5. Prints the list sorted in descending order
# 6. Prints the sum and average of all numbers in the list
# 7. Asks the user for a number and checks if it exists in the list

NOTE:
we can define a list using the following syntax
myList = [element1, element2, element3]
or we can use the list() constructor
myList = list((element1, element2, element3))
or 
myList = list([element1, element2, element3])
'''

if __name__ == "__main__":

myList = []

for _ in range(0,5):
    temp = int(input("enter a number : "))
    myList.append(temp)


print(myList)

sorted_list = myList.copy()
sorted_list.sort()
print(f"sorted list : {sorted_list}")
reverse_sorted_list = myList.copy()
reverse_sorted_list.sort(reverse=True)
print(f"sorted list : {reverse_sorted_list}")

sum = 0
average = 0
for i in myList:
    sum += i

average = sum / len(myList)
print(f"sum : {sum}")
print(f"average : {average}")

number = int(input("enter a number to search : "))
if number in myList:
    print(f"{number} is in the list") 
    print(f"index of number is : {myList.index(number)}")
else:
    print(f"{number} is not in the list")       