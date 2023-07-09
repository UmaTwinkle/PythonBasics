#!/usr/bin/env python
# coding: utf-8

# In[13]:


'''
Keywords:Reserverd words 
1.if-used in conditional statements
2.else- used in conditional statement
3.elif- used in conditional statement
4.and-used in logical operator
5.or-used in logical operator
6.not-used in logical operator
7.in-membership operator
8.for-loop
9.while-loop
10.is-identity operator
11.True-boolean datatype value
12.False-boolean datatype value
13.def-used to create function
14.continue-used to skip a value based on the condition
15.break-used to exit the loop
16.import-used to import a library
17.as-alias keyword 
18.None-null




'''

num1=10
if num1<5 :
    print('The number is lesser than 5')
elif num1>=5 and num1<=9 :
    print('The number is greater than  or equal to 5 and less then or equal to  9 ')
else:
    print('number is greater than 9 ')
    
  
    


# In[15]:


#append function 
customerList=['Daniel','John','Aauri','Baxy']
premiumCustomerList=['Aauri','Baxy']
nonPremiumCustomerList=[]
for i in customerList:
    if i in premiumCustomerList:
        print ('The customer ',i,' is premium member')
    else:
        nonPremiumCustomerList.append(i)
print(nonPremiumCustomerList)        
        
    


# In[14]:


x=None
if x is True:
    print('x is true')
    
elif x is False :
    print('x is not true or false')
else:
    print('x is null')


    


# In[1]:


print('num')


# In[3]:


i = 1

while i <= 10:
    print('6 * ',(i), '=',6 * i)

    if i >= 5:
        break
    
    i = i + 1


# In[1]:


print('num')


# In[2]:


def max_num(arr,length):
    max_arr=arr[0]
    for i in range(1,length):
        if max_arr<arr[i]:
            max_arr=arr[i]
    return max_arr;        
    
arr=[12,87,70,103]
print('The max number in array is ',max_num(arr,len(arr)))
print('Max fun',max(arr))


# In[3]:


import operator

# input numbers from user
x = int(input("Enter first integer number: "))
y = int(input("Enter second integer number: "))

# Adding both input numbers  
add = operator.add(x, y)
print("Addition: ", add)

# Subtracting both input numbers
sub = operator.sub(x, y)
print("Subtraction: ", sub)

# Multiply both input numbers
mul = operator.mul(x, y)
print("Multiplication: ", mul)

# Divide both input numbers
truediv = operator.truediv(x, y)
print("True division: ", truediv)

# floor division round to minim value
fldiv = operator.floordiv(x, y)
print("Floor division: ", fldiv)

# modulus operation
mod = operator.mod(x, y)
print("Modulus: ", mod)

# power value operation
pow = operator.pow(x, y)
print("Exponentiation: ", pow)









