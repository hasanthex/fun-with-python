# --------------------------------------------------
# 		Function or Method 
# --------------------------------------------------
# General Function Definition
def fun():
	print 'Hello'
fun()
# Function With Return type
def fun2():
	return 'This Text Return From fun2() Function'
print fun2()

# Function With Argument
def fun3(fname, lname):
	print fname, lname
fun3('Muhammad','Hasan')

def fun4(num1, num2):
	return num1+num2
print(fun4(10,15))

print('===============================================')
# Arbitrary Argument Lists
def concate(*args):
	var =' '
	return var.join(args)
print 'Name :',concate('Muhammad','Hasan','Ahmed')

args = ['Lalbagh','Dhaka','Bangladesh']
print 'Address: ',concate(*args)
print('===============================================')
# Example 1
def plus(num1, num2):
	return num1*num2
def minus(num1, num2):
	if num1>num2:
		return num1-num2
	else:
		return num2-num1
print(plus(4,5)*minus(2,5))
print('===============================================')
def feb(n):
	result = []
	a, b = 0, 1
	while a<n:
		result.append(a) 
		a, b = b, a+b
	print result
print 'Fibonacci Series ',feb(6)
print('===============================================')
# ------------------------------------------------------
#  		  OUTPUT WILL BE ABOVE CODE
# ------------------------------------------------------
Hello
This Text Return From fun2() Function
Muhammad Hasan
25
===============================================
Name : Muhammad Hasan Ahmed
Address:  Lalbagh Dhaka Bangladesh
===============================================
60
===============================================
Fibonacci Series  [0, 1, 1, 2, 3, 5]
None
===============================================