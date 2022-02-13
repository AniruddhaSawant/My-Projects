#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ('Hello World')


# In[ ]:


sunny= 'Aniruddha'
print (sunny)


# In[ ]:


employees = []

employees.append (sunny)
employees.append ('aniruddha sawant')
employees.extend (['ani','anny'])
employees.insert (1,'Yo')
employees[2] = ('SunnyYO')
employees[1] = ('AniruddhaYOYO')
employees.insert (1,'Yo')
print (employees)


# In[ ]:


print (employees)


# In[ ]:


employees.pop(-1)
print (employees)


# In[ ]:


print(employees[1:])
print(employees[1:3])


# In[ ]:


employees = employees + ['anny','YOYOYOYOYOYO']


# In[ ]:


print (employees)


# In[ ]:


employees.sort()
print(employees)


# In[ ]:


len(employees)


# In[ ]:


employees.reverse()
print(employees)


# In[ ]:


employees.copy()
employees.remove('Yo')
employees


# In[ ]:


yo=[]
yo=yo+[1,2,3,4,5,6,7]
yo


# In[ ]:


yo.pop(2)
yo


# In[ ]:


yo[2]= 3
yo


# In[ ]:


yo.insert (3,4)
yo


# In[ ]:


yo.sort()
yo.reverse()
yo.sort()
yo= yo+[8,9,10]
yo.remove(2)
yo.pop(-4)
yo


# In[ ]:


yo.insert(1,2)
yo.insert(-3,7)


# In[ ]:


yo


# In[ ]:


max(yo)


# In[ ]:


min(yo)


# In[ ]:


type(yo)


# In[ ]:


yo.index(7)


# In[ ]:


yo.copy()
yo


# In[ ]:


x = 2
y = 4
z = 6
x+y+z


# In[ ]:


True and True


# In[ ]:


True or True


# In[ ]:


True and False


# In[ ]:


True or False


# In[ ]:


False and False


# In[ ]:


False or False


# In[ ]:


x= int(input())
a= 6
b= 10
if x<=a:
    print (x, 'is so small')
if x>a and x<b:
    print(x, 'is medium')
if x>=b:
    print(x, 'is so big')

    


# In[ ]:


my_dict = {'marks':[70,80,90], 'subj':['History', 'Science', 'Maths']}


# In[ ]:


print(my_dict)


# In[ ]:


my_dict.keys()


# In[ ]:




