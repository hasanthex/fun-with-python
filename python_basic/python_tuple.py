# -------------------------------------------
# Python- Tuple Definition
# -------------------------------------------
# Empty Tuple
my_tuple = ()
# Tuple With Int Datatype
my_tuple_1 = (1,2,3,4,5)
# Tuple With String Datatype
my_tuple_2 = ('String 1','String 2')
# Tuple With Mixed Datatype
my_tuple_3 = (1,2,3,'String',1.5)
# Nested Tuple
my_tuple_4 = ('Sting', [11,12,13], (10,9,8,7)) 
# tuple can be created without parentheses
my_tuple_5 = 20,'Tuple String', 11.50
# tuple unpacking
a, b, c, = my_tuple_5;
print(a)
print(b)
print(c)
print('========================================')
# Declare One Element is a bit tricky.
# my_tuple_6 Treat Like a String Declare. And my_tuple_7 Treat Like a Tuple Declare
my_tuple_6 = ('One Element')
my_tuple_7 = ('One Element',)
print(type(my_tuple_6))
print(type(my_tuple_7))
my_tuple_8 = 'Single Element',
print(type(my_tuple_8))
print('========================================')
# -----------------------------------------------
# Access Tuple Elements  
# -----------------------------------------------
print(my_tuple_1)
print'Third Element Of This Tuple Is:',my_tuple_1[2]
print('========================================')
# Accessing Nesting Tuple Element
print(my_tuple_4)
print(my_tuple_4[0][2])
print(my_tuple_4[1][1])
print(my_tuple_4[2][3])
print('========================================')
# The index of -1 refers to the last item
print(my_tuple_3[-1])
print('========================================')
# Tuple Slicing
my_tuple_9 =  (1,2,3,4,5,6,7,8,9,10)
print my_tuple_9[:]
print my_tuple_9[0:3]
print my_tuple_9[3:]
print my_tuple_9[:-7]
print('========================================')
# concatenation multiple tuple element
my_new_tuple = my_tuple_3 + my_tuple_9
print my_new_tuple
# Repeat Multiple Times
print (my_tuple_3*3)
print('========================================')
# Delete Tuple
my_tuple_10 = ('a','b','c')
print my_tuple_10
del my_tuple_10
print('========================================')
# Tuple Method
print('Tuple Method count(), index(), max(), min(), sorted(),  and in -->')
my_tupe_11 = ('x','y','z')
print 'Postion of x is: ',my_tupe_11.count('x')
print 'Postion of a is: ',my_tupe_11.count('a')
print 'Postion of z is: ',my_tupe_11.index('z')
print 'Character M is exist\'s in tuple: ', 'M' in my_tupe_11
print 'Character x is exist\'s in tuple: ', 'M' in my_tupe_11
print 'Max value Of The Tuple is: ', max(my_tuple_9)
print 'Min value Of The Tuple is: ', min(my_tuple_9)
print 'Sort Element Of The Tuple is: ', sorted(my_tuple_9)
print 'Sum of Total Elements: ', sum(my_tuple_9)
print('========================================')
# Tuple with For loop
my_tuple_12 = ('Fox','Tiger','Deer', 'Monkey')
for name in my_tuple_12:
	print'Animal Name is: ',name
print('========================================')
# While Loop
size  = len(my_tuple_12)
count = 0
while (count<size):
	print'Animal Name is: ',my_tuple_12[count]
	count +=1
print('========================================')
# ---------------------------------------------------
#        OUTPUT WILL BE ABOVE CODE
# ---------------------------------------------------
20
Tuple String
11.5
========================================
<type 'str'>
<type 'tuple'>
<type 'tuple'>
========================================
(1, 2, 3, 4, 5)
Third Element Of This Tuple Is: 3
========================================
('Sting', [11, 12, 13], (10, 9, 8, 7))
i
12
7
========================================
1.5
========================================
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(1, 2, 3)
(4, 5, 6, 7, 8, 9, 10)
(1, 2, 3)
========================================
(1, 2, 3, 'String', 1.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(1, 2, 3, 'String', 1.5, 1, 2, 3, 'String', 1.5, 1, 2, 3, 'String', 1.5)
========================================
('a', 'b', 'c')
========================================
Tuple Method count(), index(), max(), min(), sorted(),  and in -->
Postion of x is:  1
Postion of a is:  0
Postion of z is:  2
Character M is exist's in tuple:  False
Character x is exist's in tuple:  False
Max value Of The Tuple is:  10
Min value Of The Tuple is:  1
Sort Element Of The Tuple is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Sum of Total Elements:  55
========================================
Animal Name is:  Fox
Animal Name is:  Tiger
Animal Name is:  Deer
Animal Name is:  Monkey
========================================
Animal Name is:  Fox
Animal Name is:  Tiger
Animal Name is:  Deer
Animal Name is:  Monkey
========================================