#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# In[2]:


# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# In[3]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits= [x.upper() for x in fruits]
uppercased_fruits


# In[5]:


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits= [fruits.title() for fruits in fruits]
capitalized_fruits


# In[8]:


def count_vowels(string): 
    vowels = "AaEeIiOoUu"
    final = [each for each in string if each in vowels] 
    return(len(final))


# In[10]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
fruits_with_more_than_two_vowels= [x for x in fruits if count_vowels(x) > 2]
fruits_with_more_than_two_vowels


# In[13]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits_with_only_two_vowels =   [x for x in fruits if count_vowels(x) == 2]
fruits_with_only_two_vowels


# In[16]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters
more_than_five= [x for x in fruits if len(fruits) > 5]
more_than_five


# In[19]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
exactly_five= [fruits for fruits in fruits if len(fruits) == 5]
exactly_five


# In[20]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
less_than_five= [fruits for fruits in fruits if len(fruits) < 5]
less_than_five


# In[21]:


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
length_of_fruit_characters= [len(fruits) for fruits in fruits]
length_of_fruit_characters


# In[22]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
letter = "a"
fruits_with_letter_a= [fruits for fruits in fruits if letter in fruits]
fruits_with_letter_a


# In[23]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [num for num in numbers if num % 2 == 0]
even_numbers


# In[24]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers= [num for num in numbers if num % 2 ==1]
odd_numbers


# In[25]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [num for num in numbers if num > 0]
positive_numbers


# In[26]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [num for num in numbers if num < 0]
negative_numbers


# In[27]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
two_or_more =[num for num in numbers if num > 9 or num < -9]
two_or_more


# In[29]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared=[number ** 2 for number in numbers]
numbers_squared


# In[30]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [num for num in numbers if num % 2 ==1 and num < 0]
odd_negative_numbers


# In[31]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
numbers_plus_five= [num +5 for num in numbers]
numbers_plus_five


# In[32]:


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
def prime_number (num):
    for i in range (2, num):
        if (num % i) == 0:
            return False
        else:
            return True
primes = [number for number in numbers if prime_number (number) == True]
primes

