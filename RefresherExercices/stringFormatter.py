def clean_data(stringList):
    if not stringList :
        return []
    newList = []
    for string in stringList :
        string = string.strip()
        if (len(string) < 3) or (not string.isalpha()):
            continue

        newList.append(string.title())
    return newList


if __name__ == "__main__":
    
    list1 = ["  apple ", "b1", "cat", "  dog", "elephant4", "  "]
    print(clean_data(list1))
        
