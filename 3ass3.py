#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
a=int(input("enter no "))
if(a>0):
    print("positive")
elif(a<0):
    print("negative")
else:
    print("zero")


# In[1]:


#2
a=int(input("enter no "))
if(a%2==0):
    print("even")
else:
    print("odd")


# In[2]:


#3
a=int(input("enter year "))
if(a%4==0 and a%100!=0):
    print("leap year")
elif(a%100!=0 ):
    print("not leap year")
elif(a%400==0):
    print("leap year")
else:
    print("not leap year")
    


# In[44]:


#4
a=int(input("enter no "))
count=0
if(a>1):
    for i in range(2,a):
        if(a%1==0):
            print("Not prime")
            break
        else:
            print("prime")

else:
    print("Not prime")

    


# In[ ]:


#5
for i in range(1,10001):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
                   


# # 81

# In[ ]:




