# General Class Define
class MyClass:
	txt = 'Hello World! From Class variable'
	def print_txt(self):
		return 'Hello World! From Class Function'
myClassObj = MyClass()
# Access Class Variable
print myClassObj.txt
# Access Class Function
print myClassObj.print_txt()
print('========================================================')

# Class With Constructors 
class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))
# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)
c1.getData()
c2 = ComplexNumber(15)
# Create New Varible Name new_var
c2.new_var = 25
print(c2.real, c2.imag, c2.new_var)
# **********************************************
# 		   OUTPUT WILL BE ABOVE CODE
# **********************************************
Hello World! From Class variable
Hello World! From Class Function
========================================================
2+3j
(15, 0, 25)
