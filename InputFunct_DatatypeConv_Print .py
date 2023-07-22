#!/usr/bin/env python
# coding: utf-8

# In[1]:


#datatype conversion
#datatypeConversion
#int float str bool
#int to other type
a=10
print(a)
print(type(a))
print(float(a))
b=float(a)
print(type(b))
c=str(a)
print(c)
print(type(c))
d=bool(a)
print(d)
print(type(d))
#float to other type
a=10.112
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))
c=str(a)
print(c)
print(type(c))
d=bool(a)
print(d)
print(type(d))


# In[2]:


#str to other type(float and int is not convertabile)
a='name'
print(a)
print(type(a))


# In[3]:


a='name'
#b=int(a)#value error
#print(b)
#print(type(b))
#c=float(a)#value error
#print(c)
#print(type(c))
d=bool(a)
print(d)
print(type(d))


# In[4]:


#bool to other type
a=True
print(a)
print(type(a))

b=int(a)
print(b)
print(type(b))
c=str(a)
print(c)
print(type(c))
d=float(a)
print(d)
print(type(d))


# In[10]:


#input function
num=input('enter the number')
print(num)
num=int(input('enter the number for int'))
print(num)
num=str(input('enter the number for str'))
print(num)
num=float(input('enter the number for float'))
print(num)
num=bool(input('enter the number for bool'))
print(num)


# In[11]:


#print function#end
a=10
print(a)#print(a,end='\n')
print(a,end='\t')#tab 
print(a,end=' ')
#seperator
a=10
b=30
c='Apple'
#seperator#default it is a space#shift+tab
print(a,b,c)
print(a,b,c,sep='****')


# In[12]:





# In[ ]:




