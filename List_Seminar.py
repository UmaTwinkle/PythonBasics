#!/usr/bin/env python
# coding: utf-8

# In[8]:


#list
#LIST ;ordered, changeable, and allow duplicate values(index 0,1,2,3)
list1=[0,1,'A','B','A']
print(list1)
print(list1[1])
print(list1[-1])

print(list1[1:3])
#repetition
print(list1*2)
#concat
list2=[2,3,4]
list3=list1+list2
print(list3)
#iteration
print('iteration')
for i in list1:   
    print(i) 

#change the list items
list1[1]='Apple'
print(list1)
list1[3:5]=['Python','Java']
list1[-1]=100
print('New list',list1)

#insert list items 
#append append(value)
list1.append(200)
print('after appending:',list1)
#insert insert(index,value)
list1.insert(1,100)
print('after inserting',list1)



#removing list items
list1.pop(1)
list1.remove('Apple')
del list1[3]
print(list1)

#nested lists
list1=[0,1,(2,3)]
print(list1)
print(list1[0])
print(list1[2][0])
print(list1[2][1])




# In[7]:


vegetables=["potato","carrot","spinach"]
fruits=["apple","mango","grapes"]
vegetables.reverse()
print(vegetables+fruits)
nutritiousfood=vegetables+fruits
nutritiousfood.reverse()
print(nutritiousfood)
nutritiousfood.sort()
print(nutritiousfood)
nutritiousfood.sort(reverse=True)
print(nutritiousfood)


# In[ ]:




