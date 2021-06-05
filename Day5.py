# 1. From range n to m, print all the numbers divisible by 5 and 7 both

a = int(input('Enter the 1st number\n'))
b = int(input('Enter the 2nd number\n'))
print("Your Number ranges from ", a , "to" , b)
for i in range(a , b):
	if i % 5 == 0 and i % 7 == 0:
		print(i)

print()
print()
print()
print()
print()
# 2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# Given:
# number_of_terms = 5
# So series will become 2 + 22 + 222 + 2222 + 22222
# Expected output:
# 24690
# Hint: 'a'*2 = 'aa'

# number_of_terms = int(input("Enter the number of terms"))


num = input('Enter the number')
terms=int(input('Enter the no of terms'))
sum_v = 0
for i in range(1,terms+1):
	a = int(num * i)
	sum_v+=a
print(sum_v)
	
	
print()
print()
print()
print()
print()
# 3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the sum of all numbers. (Use while loop)

add = 0
while True:
	num = input("Enter a number ")
	if num == 'q':
		break
	add = add + int(num)
print(add) 	

print()
print()
print()
print()
print()

# 4.  Write a loop to find the factorial of any number
# The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.

# For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:
# 120

num = int(input('Enter the no to find the factorial of '))
mul = 1
while num>=1:
	mul*=num
	num-=1
print(mul)

print()
print()
print()
print()
print()

# 5. input: python language is best programming language
# output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e

a = 'python language is best programming language'
for i in range(len(a)):
	end_value = '-'
	if a[i] == ' ':
		end_value = ''
	if i == len(a)-1:
		end_value = ''
	elif a[i+1] == ' ':
		end_value = ''
	if i % 2 == 0:
		print(a[i].upper() , end = end_value)
	else:
		print(a[i].lower() , end = end_value)
	


	