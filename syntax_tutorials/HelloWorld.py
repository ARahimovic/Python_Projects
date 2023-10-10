import math 


title = '''
    This is a title text that we are going to modify using 
string functions    
'''
# print(title)
# print(len(title))
# x = title.strip()
# print(len(x))
# print(x)

# upper = title.upper()
# lower = title.lower()
# inTitle = title.title()

# print(lower)
# print(upper)
# print(inTitle)

# title = "menu".upper()
# print(title.center(20, "*"))
# print("Coffe ".ljust(16,".") + "$1".rjust(4))
# print("Cappucino ".ljust(16,".") + "$2".rjust(4))
# print("Machiatto ".ljust(16,".") + "$1.80".rjust(4))


### string index value 
title = "This is a title text that we are going to modify" 

print(title[0])
print(title[-1])
print(title[5:])
print(title[0::3])

print(title.startswith("T"))
print(title.endswith("f"))


f = 3.28
print(round(f))


print(math.floor(f))
print(math.ceil(f))
print(math.pi)

