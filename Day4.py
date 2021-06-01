# use string function to count the occurrence of 'y' in a word given by user

string = str(input("Enter the word \n"))
a = string.count("y")
print(' Y occurs ', a , ' times')

#2) take input of a string and print it's even indexed characters

string = input("Enter a string\n")
for i in range (0 , len(string) , 2):
	print(string[i])
	

# 3)create a program to swap case. Using string functions

string = input("Enter the String\n")
Swaped_string = string.swapcase()
print("Swapped string is" , Swaped_string)











# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
# 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
# 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace'
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip','split', 'splitlines', 'startswith', 'strip', 'swapcase', 
# 'title', 'translate', 'upper', 'zfill']
