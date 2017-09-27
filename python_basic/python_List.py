# Python List Define Types
# 1. Define an Empty List
my_list_1 = []
# 2. Numbers  List
my_list_2 = [1,2,3] 
# 3. Various Types of List Value
my_list_3 = [10,'String',10.25]

my_list_4 = ['String One', 10]
my_list_5 = [10,11,12,13,14,15]
my_list_6 = [16,17,18,19,20]
my_list_7 = [22,21,20,19,18]

# Add Data into the List using append() method
my_list_1.append(100)
my_list_4.append('New String added')
# Add Data into the List Using insert() method
my_list_4.insert(3,'Insert By Insert Method')

# Replace The List value
my_list_3[2] = 'New String'

# Types Of Print List Values
print('===================================')
print(my_list_2[0:1])
print(my_list_2[0:]) 
print my_list_4[:]   
print(my_list_3[2])
print('===================================')
# Join 2 List values
new_list = my_list_5 + my_list_6
print new_list
print('===================================')
# List Length
print '(my_list_6) List have : ',len(my_list_6),'List Item'
print('===================================')
# Print All List Items Index and Value 
for items in my_list_6:
	print 'Item No[%d]' %my_list_6.index(items),' Item Value Is:',items
print('===================================')

# **********************************************
# 		   OUTPUT WILL BE ABOVE CODE
# **********************************************

===================================
[1]
[1, 2, 3]
['String One', 10, 'New String added', 'Insert By Insert Method']
New String
===================================
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
===================================
(my_list_6) List have :  5 List Item
===================================
Item No[0]  Item Value Is: 16
Item No[1]  Item Value Is: 17
Item No[2]  Item Value Is: 18
Item No[3]  Item Value Is: 19
Item No[4]  Item Value Is: 20
===================================
[Finished in 0.0s]