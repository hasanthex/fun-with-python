# Parent Class
class BaseClass():
	def __init__(self, fname, lname): #Constructor
		self.fname = fname
		self.lname = lname
	def fullname(self):
		return self.fname+' '+self.lname
# ./Parent Class

# Child Class
class ChildClass(BaseClass):
	def first_name():
		return self.fname
	def last_name():
		return self.lname
# ./Child Class


obj = BaseClass('Muhammad','Hasan')
print 'First Name: ',obj.fname,'\nLast Name: ',obj.lname,'\nFull Name: ',obj.fullname()

obj2 = ChildClass('Jahidul','Islam')
print '\n\nFirst Name: ',obj2.fname,'\nLast Name: ',obj2.lname,'\nFull Name: ',obj2.fullname()


# ********************************************************
# 		   OUTPUT WILL BE ABOVE CODE
# ********************************************************
First Name:  Muhammad 
Last Name:  Hasan 
Full Name:  Muhammad Hasan


First Name:  Jahidul 
Last Name:  Islam 
Full Name:  Jahidul Islam