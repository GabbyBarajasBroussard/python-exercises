#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Identify the data type of the following values:

99.9 # Float
"False" #string
False #boolean
'0' #string
0 #integer
True # boolean
'True' #string
[{}] # list
{'a': []} #dictionary


# For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL. What data type would best represent:
# <ol> 
# <li>A term or phrase typed into a search box? string
# <li>If a user is logged in? a boolean
# <li>A discount amount to apply to a user's shopping cart? a dictionary and integer
# <li>Whether or not a coupon code is valid? boolean
# <li>An email address typed into a registration form? string
# <li>The price of a product? integer
# <li>A Matrix? integer
# <li>The email addresses collected from a registration form? dictionary
# <li>Information about applicants to Codeup's data science program? dictionary

# In[37]:


For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.

'1' + 2 # I predict an error because '1' is a string and 2 is an integer
6 % 4 # I predict that 4 can only go into 6 1 time and leave a remainder of 2
type(6 % 4) #I predict this will return that the product of this equation is an integer.
type(type(6 % 4))#I predict this will return that the product of this equation is an integer. What actually happened is that it returned type as the inner equation was a type equation.
'3 + 4 is ' + 3 + 4 # I predict an error because strings can't be concat with int.
0 < 0 #I predict that it will give the boolean result of false because 0 is not less than 0.
'False' == False #This will return the value of false because string cannot match boolean
True == 'True' #This will return the value of false because string cannot match boolean
5 >= -5 #This will return the value of true because 5 is larger than -5.
get_ipython().system('False or False #nothing will happen because there is no command')
True or "42" #True will print because 42 is a string and needs to be printed.
get_ipython().system('True && !False #an error will occur, not pythonically correct')
6 % 5 #will return 1
5 < 4 and 1 == 1 #will return false because 5 is not less than 4
'codeup' == 'codeup' and 'codeup' == 'Codeup' #will return false because c does not equal C
4 >= 0 and 1 !== '1' #error will occur because !== needs to be !=
6 % 3 == 0 #will return true because 6 does not fit into 3
5 % 2 != 0 #will return true because 5 does not fit into 2
[1] + 2 #error because list and int can't concat together
[1] + [2] #will add both together into one list
[1] * 2 #will make a list with [1,1]
[1] * [2] #error because cannot multiply lists only int
[] + [] == [] #this returned tru because [] does equal []
{} + {} #error because dictionaries cannot be concat this way


# In[ ]:


You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will youhave to pay? 


# In[11]:


# solving the problem through hardcoding the amount of days into each line then adding at the end
ppm= 3
tlm= 3 * ppm
bb= 5 * ppm
hr= 1 * ppm
total_cost = tlm + bb + hr
print("Your total cost will be $",total_cost)


# In[14]:


# creating a function where the user can input up to 3 different amount of rentals days to find the total cost of renting a movie. 
def movie_night(a, b, c):
    movie1= a * ppm
    movie2= b * ppm
    movie3= c * ppm
    total_cost = movie1+movie2+movie3
    return print("Your total cost will be $",total_cost)
movie_night(3, 5, 1)


# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

# In[18]:


#solving the problem through hardcoding the amount of hours worked into each line then solving the problem
google= 400
amazon= 380
facebook= 350
paycheck_amount= (facebook*10)+(google*6)+(amazon*4)
print("Your paycheck will be $",paycheck_amount)


# In[19]:


# creating a function where the user can input the three amounts of hours 
# If I prompted the user I would display the following message:
# print("Please input the amount of hours worked in the following order: facebook, google, amazon.")
def contractor (n1, n2, n3):
    fbp= facebook * n1
    gp= google * n2
    ap= amazon * n3
    paycheck = gp + ap + fbp
    return print("Your paycheck will be $",paycheck)
contractor(10, 6, 4)


# A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

# In[ ]:


#hard coding the boolean value to solve the problem
class_empty= True
class_time= False
class_enroll = class_empty and class_time
print(class_enroll)


# In[56]:


# creating a function to solve the problem
def school_schedule (opening, time):
    if opening == "yes" and time == "no":
        return print("You may enroll for the class.")
    else:
        return print("You may not enroll for the class. Please check that the class")
school_schedule("yes", "no")
school_schedule("no", "no")


# A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# In[20]:


# hardcoding the boolean value to solve the problem
regular_member= True
offer_valid= True
premium_member= False

customer= regular_member and offer_valid or premium_member
print(customer)


# In[52]:


#creating a function to check if the customer can use the offer
def offer (member, valid, num):
    if member == "premium":
        return print("The customer may use the coupon.")
    elif member == "regular":
        if num >=2 and valid == "yes":
            return print ("The customer may use the coupon")
        else:
            return print("The customer may not use the coupon")
    else:
        return print("Please check coupon requirments")


# In[53]:


offer("premium", "no", 1)
offer("regular", "no", 5)


# Use the following code to follow the instructions below:
# 
# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:
# 
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

# In[ ]:


password_length= len(password) >= 5, print ("Password is greater than 5 characters.")
password_check= password != username, print ("Password is not the username")
username_length= len(username) <= 20, print ("Username is less than 20 characters")
space_check = (username[:1] != ' ' and username[:-1] != ' ') and (password[:1] != ' ' and password[:-1] != ' ')
good_username_and_password = password_length and username_length and password_check and space_check
print (good_username_and_password, "You have a good username and password.") 


# In[28]:


#creating a function to check if a username and password meets criteria
def criteria_checker(username, passcode):
    password_length= len(passcode) >= 5
    password_check= passcode != username
    username_length= len(username) <= 20
    space_check = (username[:1] != ' ' and username[:-1] != ' ') and (passcode[:1] != ' ' and passcode[:-1] != ' ')
    if password_length and username_length and password_check and space_check == True:
        return print("You have a good username and password.")
    else:
        return print("Your username or password does not meet the criteria. Please recheck the criteria.")


# In[29]:


criteria_checker("apple", "pie")
criteria_checker("chocolate", "pudding")


# In[59]:





# In[ ]:




