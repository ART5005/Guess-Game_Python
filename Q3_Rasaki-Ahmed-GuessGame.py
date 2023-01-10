#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

def main():
    def guessNumber(x, y):
        guess = ""
        guess_count = 0
        random_number = random.randint(1, 20)
        guess_limit = 3
        while guess != random_number:

            guess = int(input("\nEnter a number between 1 and 20 inclusive: "))
            guess_count += 1
            if guess_count == guess_limit and guess != random_number:
                print("You got 0 point")
                print("The guess number is", random_number)
                break       
            if guess < random_number:
                print("Your guess was too low. Try again: ")        
            if guess > random_number:
                print("Your guess was too high. Try again: ")        
            if guess == random_number and guess_count == 1:
                print("You got 10 points")
                break
            if guess == random_number and guess_count == 2:
                print("You got 5 points")
                break
            if guess == random_number and guess_count == 3:
                print("You got 1 point")
                break    

    guessNumber(1, 20)
    print("\nDo you want to continue playing?")
    msg = ""  
    while msg != 'X':
        msg= input("Enter Y to continue or X to quit: ").upper()
        if msg == "Y":
            main()
            break
        if msg == "X":
            break
    
main()


# In[ ]:





# In[ ]:




