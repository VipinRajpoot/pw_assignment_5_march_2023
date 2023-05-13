#!/usr/bin/env python
# coding: utf-8
Q1. Create one variable containing following type of data:

(i) string

(ii) list

(iii) float

(iv) tuple

Ans:-

(i) string:-
str = 'vipin'
print(str)


(ii) list:-

l = [1,2,3,4,'vipin']
print(l)

(iii) float:-

var_flot = 5.6
print(var_flot)


(iv) tuple:-

var_tuple = (1,2,3,4)
print(var_tuple)


Q2. Given are some following variables containing data:

(i) var1 = ' '

(ii) var2 = '[ DS , ML , Python]'

(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]

What will be the data type of the above given variable.



Ans:-

(i) String
(ii) String
(iii) List
(iv) float

Q3. Explain the use of the following operators using an example:

(i) /
(ii) %
(iii) //
(iv) **


(i) /
Ans:- Division Operators allow you to divide two numbers and return a quotient, i.e., the first number or number at the left is divided by the second number or number at the right and returns the quotient. 
for example

a = 10
b = 5
c = a/b
print(c)

output : 2.0

(ii) %
Ans:- % modulus operator is used to find the remainder for any value. 

For example 
a = 7
b = 2
c = a%b
print(c)

output : 1

(iii) //
Ans:- (//) Division (floor): divides the first operand by the second, it return always integer value not float 

For example  i have two values a and b 
 a = 9 
 b = 4
 c = a//b
 print(c)
 
 output : 2
 

(iv) **
Ans:- In Python, ** is the exponentiation operator. It is used to raise the first operand to the power of the second.
For example 
 a =2 
 b = 3
 c = a**b
 print(c)
 
 output : 8
# In[16]:


#  Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print theelement and its data type.
#  Ans: -

l = [1,2,3,4.0,'vipin',6,7.0,8,9,'hello']
for i in l:
    print(type(i)," ==",i)

Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.


# In[8]:


n = int(input("Enter the number n:- "))
b = int(input("Enter the number b:- "))
c=0
while n>0:
    if n%b==0:
        c=c+1
    n-=1
print("How many times it can be divisible ?","\n", c)


# In[23]:


# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is divisible by 3 or not.
l = []
l1 =[]
for i in range(26):
    if i%3==0:
        l.append(i)
    else:
        l1.append(i)
print("  Which number is divisiable by 3  ","\n",l)
print()
print("  Which number is not divisiable by 3  ","\n",l1)

Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.

Ans:- 

Mutable :-A mutable object can be changed after it's created, and an immutable object can't be change after creation.
Example:-
# In[21]:


l= [1,2,3,4,5,6]
l[2]='vipin'
print(l)


# In[22]:


str = ' welcome to india'
print(str)
str[2]='a'
# So we can not change immutable data type


# In[ ]:





# In[ ]:




