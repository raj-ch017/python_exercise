#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Challenge 001

"""
Ask for the user's first name and display the output message:

    Hello [First Name].
"""

user_in = input("Please enter your first name: ")

print("Hello {}, welcome to the world of programming!".format(user_in))


# In[2]:


#Challenge 002

"""
Ask the user's first name and then ask for their surname, and display the output message:

    Hello [First Name] [Surname]
"""

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print("Hello {} {}, welcome to Python.".format(first_name,last_name))


# In[3]:


#Challenge 003

"""
Write code that will display the joke "What do you call a bear with no teeth?"

On the next line, display the answer: "A gummy bear!"

Try to create is using one line of code.
"""

print("What do you call a bear with no teeth?" + "\n" + "A gummy bear!")


# In[4]:


#Challenge 004

"""
Ask the user to enter two numbers.
Add them together and display the answer as:


    The total is [answer].
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("The total is {}.".format(num1+num2))


# In[8]:


#Challenge 005

"""
Ask the user to enter three numbers. Add together the first two numbers and then multiply this 
total by the third number.
Display the answer as:

    The answer is [answer].
"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("The total is {}.".format(num3*(num1+num2)))


# In[9]:


#Challenge 006

"""
Ask how many slices of pizza the user started with and ask how many slices they have eaten.
Work out how many slices they have left and display the answer in an user-friendly format.
"""

user_in = int(input("How many slices of pizza did you have initially: "))
eaten = int(input("How many slices have been eaten: "))

print("You had {} slices, you ate {} slices and now you are left with {} slices".format(user_in,eaten,user_in - eaten))


# In[11]:


#Challenge 007 

"""
Ask the user for their name and their age. Add 1 to their age and display the output:

    [Name] next birthday you will be [new age].
"""

user_name = input("Please enter your name: ")
age = int(input("What is your age? "))

print("{}, next birthday you will be {}!".format(user_name,age+1))


# In[13]:


#Challenge 008

"""
Ask the total price of the bill, then ask how many diners there are. Divide the total bill by the
number of diners and show how much each person must pay.
"""

total = float(input("What is the total price of the bill? "))
diners = int(input("How many diners? "))

print("Each diner needs to pay {} units".format(round(total/diners,2)))


# In[15]:


#Challenge 009

"""
Write a program that will ask for a number of days and then will show how many hours, minutes and
seconds are in that number of days.
"""

days = int(input("Enter a certain number of days: "))

hours = days * 24
mins = hours * 60
secs = mins * 60

print("{} days is equivalent to: {} hours | {} mins | {} secs".format(days,hours,mins,secs))


# In[17]:


#Challenge 010

"""
There are 2,204 pounds in a kilogram. Ask the user to enter a weight in kilograms and 
convert it to pounds.
"""

user_in = float(input("Enter a weight in kgs: "))

print("{} kgs = {} pounds".format(user_in, user_in * 2204))


# In[19]:


#Challenge 011

"""
Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times
the smaller number goes into the larger number in a user-friendly format.
"""

user_in = int(input("Enter a number greater than 100: "))
smaller = int(input("Enter a number less than 10: "))

print("{} is {} times bigger than {}".format(user_in,user_in // smaller,smaller))

