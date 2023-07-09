#!/usr/bin/env python
# coding: utf-8

# In[1]:


#arithmetic operators
a=10+3
b=10-3
c=2*3
d1=6/3
d2=6//3#floor division return the minimum rounded value
d3=6%3#return the remainder
f=5**2#power
print(a,b,c,d1,d2,d3,f)


# In[2]:


#Assignment Operatord
num1=10
num1+=2
print(num1)
num1-=2
print(num1)
#ternary operator
a,b=10,20
minimum=a if a<b else b
print(minimum)


# In[9]:


#Comparision Operator(>,<,>=,<=,!=)
num1=10
num2=20
print(num1>num2)
print(num1<num2)
print(num1==num2)
print(num1>=num2)
print(num1<=num2)
if(num1>num2):
 isOutput=True
else:
 isOutput=False
print(isOutput)


# In[5]:


#Logical Operator(or,and,not)
num1=10
num2=20

if(num1>num2 or num1==num2):
 isOutput=True
else:
 isOutput=False
print(isOutput)

x = 5
print(x>3 and x<10)
print(not(x > 3 and x < 10))


# In[6]:


#Identity Operator (is,isnot)
x=['orange','apple']
y=x
z=[1,2]
print(x is y)
print(x is not y)
print(z is y)


# In[7]:


#Membership Operator(in,not in)
x = ["apple", "banana"]
string='July'
print('ly' in string)
print("banana" in x)
print("banana" not in x)


# In[8]:


#bitwise operator
#Bitwise Operator 
'''8421
1- 0001
2- 0010
3- 0011
4- 0100
5- 0101
6- 0110
7- 0111
8- 1000
9- 1001
10-1010
AND
&-if two elements are 1 then put 1 
6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010

OR
| - if any one elemt is 1 then 1
6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111


XOR
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101

NOT
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100






The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100


print(8 >> 2)




The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010
'''

print(3 & 2)
print(3 | 2)
print(~3)
print(3 << 2)
print(12 >> 2)


# In[ ]:




