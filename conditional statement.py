#!/usr/bin/env python
# coding: utf-8

# In[3]:


x=int(input("type your value"))

if x>50:
    print("your toller")


# In[6]:


x="abcdefghi"

if x.isalpha():
    print("yes is alphabits")


# # 1. Write a program to accept percentage from the user and display the grade according to the following criteria:
# 
#          Marks                                    Grade
#          > 90                                        A
#          > 80 and <= 90                              B
#          >= 60 and <= 80                             C
#          below 60                                    D
# 

# In[11]:


x=int(input("enter your marks"))

if x>90:
    print("your grade :A")
elif x>80 and x<90:
    print("your grade :b")
elif x>60 and x<80:
    print("your grade :c")
else:
    print("your grade :d")
    print("your wast fellow")
    


# In[9]:


x=int(input("enter your marks"))

if x>90:
    print("your grade :A")
elif x>80 and x<=90:
    print("your grade :b")
elif x>=60 and x<=80:
    print("your grade :c")
elif x>60:
    print("your grade :d")
else:
    print("your wast fellow")
    


# # Q4. Write a program to check whether a person is eligible for voting or not. (accept age from user)
# 

# In[12]:


z=int(input("enter you age"))

if z>18:
    print("your are eligible")
else:
    print("your not eligible")
    


# # 5. Write a program to check whether a number entered by user is even or odd.
# 

# In[16]:


v=int(input("enter the number :"))

if (v%2==0):
    print("the given number is even")
else:
    print("the given number is odd")


# # Write a program to check whether a number is divisible by 7 or not.
# 
# 

# In[26]:


v=int(input("enter the number :"))

if v%7==0:
    print("divisible by 7")
else:
    print("not divisible ")


# # Write a program to display "Hello" if a number entered by user is a multiple of five , 
# otherwise print "Bye

# In[31]:


v=float(input("enter the number :"))

if v%5==0:
    print("hello")
else:
    print("bye")


# # Q9. Write a program to display the last digit of a number.
# (hint : any number % 10 will return the last digit)
# 

# In[51]:


a=int(input())
b=a%10
print(b)


# In[52]:


x=int(input("enter the number: "))
print("last digit is : ",(x%10))


# In[56]:


x=int(input("enter the number: "))

if (x%10):
    print("last digit is :")


# # 10. Write a program to check whether the last digit of a number( entered by user ) is 
# divisible by 3 or not.

# In[18]:


x=int(input("enter the number: "))
v=x%10
if v%3==0:
    print("divisible by 3")
else:
    print("not divisible")


# In[ ]:


x=int(input("enter the number: "))

if x%10 x%3==0:
    print("divisible by 3")
else:
    print("not divisible")


# # 8. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)
# 

# In[24]:


units=int(input("enter electricity bill units: "))

if units<=100:
    print("no charges")
elif not(units>100 and units>200):
    print("your current bill",units*5)
else:
    b=100*5
    x=(units-200)*10
    print("bill",b+x)


# In[19]:


unit=int(input("electricity bill units"))

if unit<=100:
    print("no charge")
elif not(unit>100 or unit<200):
    print("bill",unit*5)
else:
    b=100*5
    x=(unit-200)*10
    print("bill",b+x)


# # 2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
#     
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                                     10%
#         <= 50000             
#                                                                  5%

# In[44]:


x=int(input("enter bike price: "))

if x>100000:
    t=x*15//100
    print("your tax is :",t)
elif (x>50000 and x<=100000):
    y=x*10//100
    print ("your tax is :",y)
else:
    z=x*5//100
    print("your tax is :",z)


# In[41]:


x=int(input("enter the value"))

if x>100000:
    y=x*15/100
    print("type your tax %",y)
elif x>50000 and x<100000:
    z=x*10/100
    print("type your tax %",z)
else:
    a=x*5/100
    print("type your tax %",a)
    


# In[ ]:




