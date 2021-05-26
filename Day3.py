# Age Calculator

a=int(input('Enter your birth year : '))
b=int(2021)
print("You Are {}".format(b-a) + " Years old")


#Basic Calculator

a=int(input('Enter 1st number'))
b=int(input('Enter 2nd number'))
c=input('Enter Operation[Add ,Sub ,Mul ,Div]')

if(c=='Add'):
	Ans = a + b
elif(c=='Sub'):
	if(a > b):
		Ans = a - b
	elif(a < b):
		Ans = b - a
elif(c=='Mul'):
	Ans = a * b
elif(c=='Div'):
	Ans =  a / b
	
print('Answer is' , Ans)

