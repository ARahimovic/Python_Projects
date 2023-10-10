import sys
import math

#set are unordered, mutable(can add, remove), unique dont allow duplicate, not indexable

mySet = {1,5,-2,4,3}
print(mySet)
print(len(mySet))

print()
mySet.add(5)
print(mySet)
print(len(mySet))

mySet.update({1000})
print(mySet)
print(len(mySet))


mySet2 = set((70,50,30,10,5))
print(mySet2)

#create a new set with only the intersection elements
interSet = mySet.intersection(mySet2)
print(interSet)
#modify the calling set to include only the intersection elements
mySet.intersection_update(mySet2)
print(mySet)


unionSet = mySet2.union(mySet)
print(unionSet)




