# ******************************************************
# 					ITERATOR IN PYTHON
# ******************************************************
# Iterators are everywhere in Python. 
# They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.
# Iterator in Python is simply an object that can be iterated upon. 
# An object which will return data, one element at a time.
# Python iterator object must implement two special methods: __iter__() and __next__(), collectively called the iterator protocol.
# An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.
# The iter() function (which in turn calls the __iter__() method) returns an iterator from them.
print('=============================================')
# Python For Loop
result_1, result_2 = '',''
input  = "ABCDEFG"
for char in input:
	result_1 = result_1+' '+char
print'Result By For Loop: ',result_1
print('=============================================')
# Python Iterator
list = iter(input)
print'Type is: ',type(list)
while True:
	try:
		result_2 = result_2+' '+next(list)
	except StopIteration:
		break
print'Result By Iterator Object:',result_2
print('=============================================')
# Create Own Iterator
class PowerOfTwo:
	def __init__(self,limit=0):
		self.limit = limit
	def __iter__(self):
		self.start = 0
		return self
	def __next__(self):
		if self.start <= self.limit:
			result = 2 ** self.start
			self.start += 1
			return result
		else:
			raise StopIteration
obj = PowerOfTwo(3)
it  = iter(obj)
print it.__next__()
print it.__next__()
print it.__next__()
print it.__next__()
# We just have to implement the methods __iter__() and __next__().
# The __iter__() method returns the iterator object itself. If required, some initialization can be performed.
# The __next__() method must return the next item in the sequence. 
# On reaching the end, and in subsequent calls, it must raise StopIteration.
print('=============================================')
# **********************************************
# 		   OUTPUT WILL BE ABOVE CODE
# **********************************************
=============================================
Result By For Loop:   A B C D E F G
=============================================
Type is:  <type 'iterator'>
Result By Iterator Object:  A B C D E F G
=============================================
1
2
4
8
=============================================