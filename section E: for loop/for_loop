#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Challenge 035

"""
Ask the user to enter their name and then display their name three times.
"""

user_in = input("Enter your name: ")
times = 3

for k in range(times):
    print(user_in)


# In[2]:


#Challenge 036

"""
Alter program 035 so that it will ask the user to enter
their name and a number and then display their name that
number of times.
"""

user_name = input("Enter your name: ")
times = int(input("Enter an integer: "))

for j in range(times):
    print(user_name)


# In[4]:


#Challenge 037

"""
Ask the user to enter their name and display each letter
in their name on a seperate line.
"""

user_name = input("Enter your name: ")

for letter in user_name:
    if letter != " ":
        print(letter)


# In[6]:


#Challenge 038

"""
Change program 037 to also ask for a number. Display
their name (one letter at a time on each line) and 
repeat this for the number of times they entered.
"""

user_name = input("Enter your name: ")
times = int(input("Enter an integer: "))

for i in range(times):
    for letter in user_name:
        if letter != " ":
            print(letter)
    print()


# In[21]:


#Challenge 039

"""
Ask the user to enter a number between 1 and 12 and 
then display the times' table for that number.
"""

user_in = int(input("Enter a number between 1 and 12: "))

for val in range(1,13):
    print("{} * {} = {}".format(user_in,val,user_in*val))


# In[11]:


#Challenge 040

"""
Ask for a number below 50 and then count down from 50
to that number, making sure you show the number they
entired in the output.
"""

user_num = int(input("Enter a number less than 50: "))

for val in range(50,user_num-1,-1):
    print(val)
    if val == user_num:
        print("The number you entered is {}.".format(user_num))


# In[13]:


#Challenge 041

"""
Ask the user to enter their name and a number. If the
number is less than 10, then display their name that
number of times; otherwise display the message "Too high"
three times.
"""

user_name = input("Enter your name: ")
user_num = int(input("Enter a number: "))

if user_num < 10:
    for k in range(user_num):
        print(user_name)
else:
    print("Too high " * 3)


# In[14]:


#Challenge 042

"""
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. 
If they do, then add the number to the total. 
If they do not want it included, don't add it to the 
total. After they have entered all the five numbers,
display the total.
"""

total = 0
count = 0

for i in range(5):
    user_num = int(input("Enter a number: "))
    user_choice = input("Do you want to include the number in total? (Y/N): ")
    
    if user_choice == "Y":
        total += user_num
        count += 1

        
print("The total of {} numbers included is {}.".format(count,total))        


# In[18]:


#Challenge 043

"""
Ask which direction the user wants to count (up or down).
If they select up, then ask them for the top number and
then count from 1 to that number. 
If they select down, ask them to enter a number below
20 and then count down from 20 to that number.
If they entered something other than up or down,
display the message "I don't understand".
"""

possible_answers = ["up","down"]

direction = input("In which direction would to like to count? (up/down): ").lower()

if direction in possible_answers:
    if direction == "up":
        user_num = int(input("Enter a number greater than 1: "))
        
        for val in range(1,user_num+1):
            print(val)
    elif direction == "down":
        user_num = int(input("Enter a number below 20: "))
        
        for val in range(20,user_num - 1,-1):
            print(val)
            
else:
    print("I don't understand!")


# In[20]:


#Challenge 044

"""
Ask how many people the user wants to invite to a 
party. If they entered a number below 10, ask for the
names and after each name display:
    
    "[name] has been invited"
    
If they enter a number which is 10 or higher, display
the message "Too many people".
"""

user_num = int(input("How many people will you invite? "))

if user_num >= 10:
    print("Too many people!")

else:
    for k in range(user_num):
        user_name = input("Enter the name of the person: ")
        
        print("{} has been invited".format(user_name))

