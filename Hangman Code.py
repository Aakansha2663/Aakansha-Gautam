#!/usr/bin/env python
# coding: utf-8

# In[59]:


import random                                   # importing random library to generate random numbers
import linecache                                # importing lincache library to read single line from the .txt file

# function to give alphabetical hints to the user
def alphabet_hint(word):
        generated_number=[]                      # to store the random number generated
        alphabets=[]                             # to store the value got from the index
        for i in range(0,3):                     # loop to run 3 times and produce random number
            for_alphabets=random.randint(0,length-2)  # generation of random number 
            if for_alphabets not in generated_number:
                generated_number.append(for_alphabets)
        for num in generated_number:
            alphabets.append(word[num])           # appending the aplhabets from the particular index into the list
        return(f"Some alphabets are: {alphabets}")
            
def guess(word):
    valid=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    guessed_alphabets=[]
    correct=True
    done=0
    total_chance=8
    word_list=[]
    letters_to_guess=len(word)
    for i in word:
        word_list.append(i)                         # inserting individual alphabets of word into list
    while not done:
        for alphabet in word_list:
            if alphabet.lower() not in guessed_alphabets:
                print("_",end=" ")                   # gives output as _ _ _ _ ("_" extended till the length of word)
            else:
                print(alphabet,end=" ")              # if guess matched then "_" is replaced with particular alphabet
   
        print("")
        print(f"\n letters remaining: {letters_to_guess}")
        print(f"you have total {total_chance} chances\n")
        figure(total_chance)                         # funciton call to print the figure
        print(f"guessed alphabets are: {guessed_alphabets}")
        guess=input("enter the guess: ").lower()     # use of .lower() function to make sure code runs even if user enters captial letter
        if guess in valid:
            guessed_alphabets.append(guess.lower())  # appending the guessed word 
        else:
            raise ValueError(" You Can Enter Single Character Only") # raise of exception if space or more than one character entered
            
        if guess.lower() not in word.lower():
            total_chance -= 1                       # decreases as the word don't match
            if total_chance==0:
                break                               # loop breaks once the value of total_chance reach to 0.
        for letter in word:
            if letter.lower() not in guess:         #checks whether the guessed word is in the given word or not
                done=0  
            else:
                letters_to_guess-=1
            if letters_to_guess==0:
                done=1                          # boolean value will be positive once the player guess all the letters
        
                
    if done:                                       # prints only if user guess all the letters correctly
        print("\n\tCONGRATULATIONS!!!!")
        print(f"YOU HAVE GUSSED THE WORD CORRECTLY ")
        print(f"The word was {word}")
    else:                                          # prints if user cannot make a guess 
        print(f"\nMAXIMUM ATTEMPT REACHED")
        print(f"THE WORD WAS {word}")
        
        
        
        
        
# function to draw the figure: 
def figure(chance):
    if chance==8:
        print("|",end=""), print("-",end=""), print("-",end=""),  print("-")
        print("|",end=""), print(" |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("-")
        
    if chance==7:
        print("|",end=""), print("-",end=""), print("-",end=""),  print("-")
        print("|",end=""), print(" |")
        print("|",end=""), print(" O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("-")
        
    if chance==6:
        print("|",end=""), print("-",end=""), print("-",end=""),  print("-")
        print("|",end=""), print(" |")
        print("|",end=""), print(" O")
        print("|",end=""), print(" |")
        print("|",end=""), print(" |")
        print("|",end=""), print(" |")
        print("|")
        print("-")
    
    if chance==5:
        print("|",end=""), print("-",end=""), print("-",end=""), print("-",end=""),  print("-")
        print("|",end=""),                   print(" |")
        print("|",end=""),                   print(" O")
        print("|",end=""),print("/",end=""), print(" ")        
        print("|",end=""),                   print(" |")
        print("|",end=""),                   print(" |")        
        print("|")
        print("-")
    
    if chance==4:
        print("|",end=""), print("-",end=""), print("-",end=""), print("-",end=""),  print("-")
        print("|",end=""),                   print(" |")
        print("|",end=""),                   print(" O")
        print("|",end=""),print("/",end=""), print(" ",end="")         ,print("\\")
        print("|",end=""),                   print(" |")
        print("|",end=""),                   print(" |")         
        print("-")
    
    if chance==3:
        print("|",end=""), print("-",end=""), print("-",end=""), print("-",end=""),  print("-")
        print("|",end=""),                   print(" |")
        print("|",end=""),                   print(" O")
        print("|",end=""),print("/",end=""), print(" ",end="")         ,print("\\")
        print("|",end=""),                   print(" |")
        print("|",end=""),print("/",end=""), print(" ")         
        print("|")
        print("-")
        
    if chance==2:
        print("|",end=""), print("-",end=""), print("-",end=""), print("-",end=""),  print("-")
        print("|",end=""),                   print(" |")
        print("|",end=""),                   print(" O")
        print("|",end=""),print("/",end=""), print(" ",end="")         ,print("\\")
        print("|",end=""),                   print(" |")
        print("|",end=""),print("/",end=""), print(" ",end="")         ,print("\\")
        print("|")
        print("-")
        
    if chance==1:
        print("|",end=""), print("-",end=""), print("-",end=""), print("-",end=""),  print("-")
        print("|")                    
        print("|",end=""),                   print(" O")
        print("|",end=""),print("/",end=""), print(" ",end="")         ,print("\\")
        print("|",end=""),                   print(" |")
        print("|",end=""),print("/",end=""), print(" ",end="")         ,print("\\")
        print("|")
        print("-")
        
        
        
        
        
#main body of the program:              
user_name=input("PLEASE ENTER YOUR NAME: ")
print(f"\n\t\t\t***********{user_name.upper()} WELCOME TO HANGMAN GAME*************\n")

print("CHOOSE ANY ONE OPTION: ")
print("1. Country")
print("2. Football Player")
print("3. Fruits")
print("4. Animal")
print("5. Books")

option=int(input("\nENTER THE OPTION NUMBER: ")) 

line=random.randint(1,10)                    # generation of line number to read from the file 
if option==1:
    word=linecache.getline("country.txt",line).strip()
    hint=linecache.getline("countryhint.txt",line)
    length=len(word)
    print("Guess The Country: \n") 
    print(f"Hint is: \n {hint}")            # provides the hint for the word

if option==2:
    word=linecache.getline("player.txt",line).strip()
    hint=linecache.getline("playerhint.txt",line)
    length=len(word)
    print("Guess The Football Player: \n ") 
    print(f"Hint is: \n {hint}")            # provides the hint for the word
    
if option==3:
    word=linecache.getline("fruits.txt",line).strip() # reading .txt file line by line and printing particulatar line number
    hint=linecache.getline("fruitshint.txt",line)
    length=len(word)
    print("Guess The Fruit: \n")
    print(f"Hint is: \n {hint}")           # provides the hint for the word

if option==4:
    word=linecache.getline("animal.txt",line).strip()
    hint=linecache.getline("animalhint.txt",line)
    length=len(word)
    print("Guess The Animal:\n")
    print(f"Hint is: \n {hint}")          # provides the hint for the word

if option==5:
    word=linecache.getline("book.txt",line).strip()
    hint=linecache.getline("bookhint.txt",line)
    length=len(word)
    print("Guess The Book:\n")
    print(f"Hint is: \n {hint}")          # provides the hint for the word

    
#FUNCTION CALL
print("\n")
print(alphabet_hint(word))
guess(word)
        
        
        
        
    
        
    


# In[45]:


for i in "aakansha":
    print("_",end=' ')


# In[ ]:





# In[ ]:





# In[ ]:




