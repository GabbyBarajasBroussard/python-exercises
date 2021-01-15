#!/usr/bin/env python
# coding: utf-8

# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[16]:


def is_two (letter):
    if letter == 2 or letter == "2" or letter =="two":
        return True
    else:
        return False
is_two("four")


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[18]:


def is_vowel (string):
    lvowel= ['a', 'e', 'i', 'o', 'u']
    uvowel= ['A', 'E', 'I', 'O', 'U']
    if (string in lvowel) or (string in uvowel):
        return True
    else:
        return False
is_vowel('banana')
is_vowel('a')


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[21]:


def is_consonant (string):
    lvowel= ['a', 'e', 'i', 'o', 'u']
    uvowel= ['A', 'E', 'I', 'O', 'U']
    if (string not in lvowel) or (string not in uvowel):
        return True
    else:
        return False
is_consonant ('B')
is_consonant ('a')


# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[122]:


def capital_string(string):
    vowels= ['a', 'e', 'i', 'o', 'u']
    string= string.lower()
    if string[0] not in vowels:
        return (string.capitalize())
    else:
        return (string.lower())
capital_string('Apple')


# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[46]:


def calculate_tip(bill, percentage):
    tip= bill * percentage
    total_bill= bill + tip
    return total_bill


# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[53]:


def apply_discount(original, percentage):
    discount= original * percentage
    total_price= original - discount
    return total_price
apply_discount(100, .25)


# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[51]:


def handle_commas (string):
    return int(string.replace(",", ""))
handle_commas("1,000")


# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[54]:


def get_letter_grade (raw_score):
    if raw_score >= 90:
        return "A"
    elif raw_score >= 80 and raw_score <= 89:
        return "B"
    elif raw_score >= 76 and raw_score <= 79:
        return "C"
    elif raw_score >= 70 and raw_score <=75:
        return "D"
    elif raw_score <= 60:
        return "D"
get_letter_grade(79)


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[56]:


def remove_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    chars = []
    for i in string: 
        if i.lower() not in vow:
            chars.append(i)
    return "".join(chars)


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# In[106]:


def normalize_name(name):
    name = name.strip() #first I am removing all spaces at the beginning and the end of the string
    name = name.lower() # then I am converting all letters in the string to lowercase
    name = name.replace(" ", "_") # then I m removing all spaces and replacing them with underscores
    output="" #creating an empty string
    for letter in name: #creating my for loop to add to my empty output
        if letter.isidentifier(): # if my letter is an identifier then:
            output += letter # I want it to append to my empty output
    return output # i am now returning the output with all the corrections

normalize_name("  Ca%%RyS iS tHe B!!!eSt Do$$$G eVeR  ")


# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[72]:


def cumulative_sum (lists):
    cumulative_list = []   # i am making an empty list
    length = len(lists)  
    cumulative_list = [sum(lists[0:x:1]) for x in range(0, length+1)]  
    return cumulative_list[1:]
(cumulative_sum([1,1,1]))
cumulative_sum([1,2,3,4])


# ## Bonus

# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[117]:


def twelveto24(time):
    if "a" in time: #this if statement is looking for am
        time = time.rstrip("am") #this reassigns the time with the am removed.
        time = time.replace(":","") #removes the : which is not in 24 hour format
        zero = "0" #creating a value named zero to use to append to the beginning for the next step
        time= (zero + time) #putting a zero at the beginning of the time for 24 hr format
    elif "p" in time: #if am isn't in the time, the next thing the function is going to do is check if pm is in the time
        time = time.rstrip("pm") #this reassigns the time with the pm removed
        time = time.replace(":", ".") #replacing the : with a . so that it will be able to be converted to a float
        time = float(time) #converting to a float so that we will be able to mathematically manipulate it as you can't with a string.
        time = time + 12 #adding 12 hours to get the 24 hour format
        time = str(time) #putting the float back into a string
        time = time.replace(".", "") # removing . for proper 24 hr format
        zero = "0" #creating a value named zero to use to append to the end for the next step
        time = (time + zero) # adding a zero to the end to have the proper amount of zeros.
    else: # in case there is not a proper time in the field
        print('You did not put in a valid time. Please try again.')
    return time    
twelveto24("2:00 pm")


# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
