myDict = dict(love="wife", child="Kratos")

print(myDict)

print(f"{myDict.keys()}")
print(f"{myDict.values()}")
print(myDict.items())

print()

myDict2 = {
    'jack' : 'bodybuilder',
    'baki' : 'Warrior',
    'Yujiro' : 'Mass destruction'

}

print(myDict2)
print(myDict2.keys())
print(myDict2.values())
print(myDict2.items())

t = myDict2.items()
print(type(t))

#add items to a dictionary 
myDict["goal"] = "hereAfter"
print(len(myDict))
print(myDict)

val = myDict.get("goal")
print(val)
val = myDict.get("dontKnow")
print(val)

#update the dictionary 
myDict.update({"newKey" : "newValue"})
print(myDict)

#remove a key and return its value 
a = myDict.pop("newKey")
print(myDict)
#remove last key:pair item
myDict.popitem()
print(myDict)

