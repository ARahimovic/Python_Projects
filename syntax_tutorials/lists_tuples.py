users = ['rahimovic', 'assleha', 'youcef']

print(len(users))

for item in users :
    print(item)

users += ['addded']
for item in users :
    print(item)

print("with this we can append multiple items")
users += ['another addded', "another two"]
for item in users :
    print(item)



#this will add each letter as a item to the list
#users +='added'
# for item in users :
#     print(item)

users.append("dhiaa")
print(len(users))

for item in users :
    print(item)


# want to add another list 
users.extend(["another list", "hello", "awsome"])
print("extended list")
print(len(users))
for item in users :
    print(item)


print("rahimovic" in users) ##return true

users.remove("rahimovic")
print("after removing element")
for item in users :
    print(item)

obj = users.pop(2)
print(f"object popped {obj}")
print("after poping element")
for item in users :
    print(item)

print()
users.insert(2,"inserted at 2")
for item in users :
    print(item)


#slicing list



#copying a list : 3 ways
copyList = users[:]
print(f"\n{copyList}")
list2 = copyList.copy()
print(f"\n{list2}")
list3 = list(copyList)
print(f"\n{list3}")

# to append
# users += ["rara", "fafa"]

print(len(list2))
# add an element at postion 2
list2[2:2] = ["addedElement", "this is useful"]
print(list2)
#replace element in position 2
list2[2:3] = ["replaceElemet"]
print(list2)

list2[2] = "replacing it Again"
print(list2)

#get index of an element
print(f"index = {users.index('dhiaa')}")


numbers = list([1, 75, 86, 60, 40, 25])

numbers.sort(reverse=True)
print(numbers)

#to clear a list , it become empty
users.clear()
print(users) #empty list

################# tuples #########
#tuples are like lists but they are immutable once created, you cannot add, append change order of a tuple


myTuple = ('rahimovic', 26, 'mirka')
print(myTuple)
myTuple2 = tuple(('another tuple', 2050, 'human potentiel is amazing'))
print(myTuple2)
print(myTuple2.count(22))
print(myTuple2.index(2050))

print(myTuple[2])
#creating a tuple from a list

numberTuple = tuple(numbers)
print(numberTuple)

(one, *two, three)= numberTuple
print(one)
print(two)
print(three)

