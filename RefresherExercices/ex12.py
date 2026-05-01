# Exercise 12: File Handling with Data Processing
# Task: Create a program that:
# 1. Generates a file with 100 random numbers (1-1000)
# 2. Reads the file and calculates the average, minimum, and maximum values
# 3. Creates a new file with only the numbers above the average
# 4. Creates a dictionary with the frequency of each number
# 5. Prints the 5 most common numbers and their frequencies

import random 

if __name__=="__main__":


    with open("numbers.txt", "w") as myfile:
        for _ in range(100):
            number = random.randint(1, 1000)
            myfile.write(str(number) + "\n")
    
    # Step 2: Read the file and calculate statistics
    with open("numbers.txt", "r") as myfile:
        content = myfile.read().strip()
        values = list(map(int, content.split('\n')))

    
    maximum = max(values)
    minimum = min(values)
    average = sum(values) / len(values)

    print(f"average = {average}")
    print(f"max = {maximum}")
    print(f"min = {minimum}")


    with open("average_numbers.txt", "a") as averageFile:
        average_values = [str(val) for val in values if val >average]
        txt = "\n".join(average_values)
        averageFile.write(txt) 

        

    number_frequency = {}
    for val in values:
        number_frequency[val] = number_frequency.get(val, 0) + 1
    
    print(f"frequency count : \n{number_frequency}")

    most_common_numbers = sorted(number_frequency.items(), key=lambda x:x[1], reverse=True)[:5]
    print(f"most_common_numbers as a list of tuples: \n{most_common_numbers}")

    most_common_keys = sorted(number_frequency, key=number_frequency.get, reverse=True)[:5]
    most_common_dict = {key: number_frequency[key] for key in most_common_keys}
    print(f"\n5 most common numbers (as dictionary):")
    print(most_common_dict)


    
    
