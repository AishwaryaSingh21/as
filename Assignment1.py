#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task1


# In[1]:


#2
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=",")


# In[3]:


#3
fname = input("Enter first name")
lname = input("Enter last name")
print(lname+" "+fname)


# In[5]:


#4
d = 12
r = d/2
volume = 4/3*3.14*r*r*r
print("Volume of the sphere is",volume)
 


# In[6]:


#Task2


# In[7]:


#1
liste = input("Enter comma seperatable input").split(",")
print("List entered is",liste)


# In[18]:


#2
n = int(input("Enter number of lines..must be a odd integer"))
l = ["*"]
for i in range(n):
    print(*l)
    if i<n//2:
        l.append("*")
    else:
        l.pop(0)


# In[9]:


#3
word = input("Enter word")
word = list(word)
word.reverse()
word = "".join(word)
print("Reversed word is "+word)


# In[16]:


#4
print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN\, !\n\t\tSOCIALIST\, SECULAR\, DEMOCRATIC REPUBLIC\n\t\t\tand to secure to all its citizens")

