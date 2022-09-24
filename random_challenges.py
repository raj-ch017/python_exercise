#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

#Challenge 052

"""
Display a random integer between 1 and 100 inclusive
"""

num1 = random.randint(1,100)
print(num1)


# In[7]:


#Challenge 053

"""
Display a random fruit from a list of five fruits.
"""

fruit_list = ["Watermelon","Apple","Pineapple","Orange","Banana"]

choice = random.choice(fruit_list)
print(choice)


# In[12]:


#Challenge 054

"""
Randomly choose either heads or tails ('h' or 't').

Ask the user to make their choice. If their choice is
the same as the randomly selected value, display the
message 'You win', otherwise display 'Bad luck'.

At the end, tell the user if the computer selected 
heads or tails.
"""

choice_options = ['h','t']
comp_choice = random.choice(choice_options)

user_in = input("Choose between heads and tails (h/t): ").lower()

if user_in == comp_choice:
    print("You win!")
    
else:
    print("Bad luck!")
    
print("Your choice: {} | Computer's choice: {}".format(user_in,comp_choice))


# In[25]:


#Challenge 055

"""
Randomly choose a number between 1 and 5. Ask the user
to pick a number. If they guess correctly, display the
message "Well done", otherwise tell them if they are
too high or too low, and ask them to pick a second 
number. If they guess correctly on their second guess,
display "Correct", otherwise display "You lose".
"""

choice = random.randint(1,5)


for k in range(2):

    user_in = int(input("Enter a number between 1 and 5: "))

    if user_in == choice:
        print("Well done")
        break
        
    else:
        
        if user_in > choice:
            print("Too high")
            
        else:
            print("Too low")
                
        if k == 1:
            print()
            print("You lose")


# In[2]:


#Challenge 056

"""
Randomly pick a whole number between 1 and 10. Ask the user to
enter a number and keep entering numbers until they enter the 
number that was randomly picked
"""
import random


rand_choice = random.randint(1,10)

user_in = int(input("Enter a number between 1 and 10: "))

if user_in != rand_choice:
        
        while user_in != rand_choice:
            
            user_in = int(input("Enter a number between 1 and 10: "))
            
        print("Your choice matches the random choice!")
        
else:
    print("Your choice matches the random choice! On the first go as well!")
    
    


# In[4]:


#Challenge 057

"""
Update the program 056 so that it tells the user if they are too
high or too low before they pick again.
"""


rand_choice = random.randint(1,10)

user_in = int(input("Enter a number between 1 and 10: "))

if user_in != rand_choice:
        
        while user_in != rand_choice:
            
            if user_in > rand_choice:
                print("Your pick is too high!")
                
            elif user_in < rand_choice:
                print("Your pick is too low!")
            
            user_in = int(input("Enter a number between 1 and 10: "))
            
        print("Your choice matches the random choice!")
        
else:
    print("Your choice matches the random choice! On the first go as well!")


# In[10]:


#Challenge 058

"""
Make a maths quiz that asks five questions by randomly generating
two whole numbers to make the question

    e.g: [num1] + [num2]
    
Ask the user to enter the answer. If they get it right add a point
to their score. At the end of the quiz, tell them how many they
got correct out of five.
"""

score = 0
operator_choice = ["addition","subtraction","multiplication","division","exponentiate"]

for k in range(5):
    
    choice = random.choice(operator_choice)
    num1 = random.randint(1,5)
    num2 = random.randint(1,5)
    
    if choice == "addition":
        print("Your question is: ")
        print("{} + {} =".format(num1,num2))
        user_ans = int(input("Enter your answer: "))
        
        if user_ans == (num1 + num2):
            score += 1
            
    elif choice == "subtraction":
        print("Your question is: ")
        print("{} - {} =".format(num1,num2))
        user_ans = int(input("Enter your answer: "))
        
        if user_ans == (num1 - num2):
            score += 1
            
    elif choice == "multiplication":
        print("Your question is: ")
        print("{} * {} =".format(num1,num2))
        user_ans = int(input("Enter your answer: "))
        
        if user_ans == (num1 * num2):
            score += 1
            
    elif choice == "division":
        print("Your question is: ")
        print("{} / {} =".format(num1,num2))
        user_ans = float(input("Enter your answer: "))
        
        if user_ans == (num1 / num2):
            score += 1
            
    elif choice == "exponentiate":
        print("Your question is: ")
        print("{} raised to power {} =".format(num1,num2))
        user_ans = int(input("Enter your answer: "))
        
        if user_ans == (num1 ** num2):
            score += 1
            

print("Your total score is {}".format(score))


# In[15]:


#Challenge 059

"""
Display five colors and ask the user to pick one. If they pick the
same as the program has chosen, say 'Well done', otherwise 
display a witty answer which involves the correct color

    e.g: "I bet you are GREEN with envy"
    e.g: "You are probably feeling BLUE right now"
    
Ask them to guess again; if they have still not got it right, keep
giving them the same clue and ask the user to enter a color until
they guess it correctly.
"""

color_choice = ["red","blue","green","orange","black"]
choice = random.choice(color_choice)

user_choice = input("Enter a color: ").lower()

if user_choice != choice:
    
    while user_choice != choice:
        
        print("You are probably feeling {} right now!".format(choice.upper()))
        
        user_choice = input("Try again! Enter a color: ").lower()
        
    print("Congratulations! You have guessed the correct color!")
    

else:
    print("Congratulations! It took you 1 try to guess the correct color!")

