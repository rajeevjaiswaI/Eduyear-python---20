# Create list


lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele)
      
print(lst)


# Q1. Count even numbers and odd numbers
lst_even = []
lst_odd = []
for i in range(len(lst)):
	if lst[i] % 2 == 0:
		lst_even.append(lst[i])
	else:
		lst_odd.append(lst[i])
print(lst_even)
print(lst_odd)
print('Even no are ', len(lst_even))
print('odd no are ', len(lst_odd))

	



# Q2. Tell max and min of the list ( without using any inbuilt function like max(),min())


min_v, max_v = lst[0], lst[0]
sum_v, mul_v = 0, 1

for i in range(len(lst)):
	if lst[i] < min_v:
		min_v = lst[i]
	if lst[i] > max_v:
		max_v = lst[i]
	sum_v += lst[i]
	mul_v *= lst[i]

print(min_v, max_v)
print(sum_v, mul_v)