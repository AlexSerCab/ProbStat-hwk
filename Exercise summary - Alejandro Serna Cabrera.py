#!/usr/bin/env python
# coding: utf-8

# # A good first program

# In this first exercise the book puts into practice the print 
# that is the order or command that will make a text that we choose,
# be displayed on the screen.

# ###### EXAMPLE

# In[5]:


print("I am doing homework")


# # Comments and Pound Characters

# You can also put some comments in your code in order to help you or someone else to understand what you are coding and what does every line do. To do this we use "#" which makes the code enter in a "standby" mode, the program won't execute any text after the "#".

# ###### EXAMPLE

# In[6]:


print("I am doing homework") # This will show in the screen all the text that we put between quotation marks


# # Numbers and Math

# This chapter will help us with basically all the numbers and things we want to do with them. The programming language let us do mathematical exercises and evaluate certain situations. You can compare numbers and give a non-numerical result, evaluating the data that is written.

# ###### EXAMPLE

# In[10]:


print ("You can do arithmetic operations like: 2+3+4/6 =", 2+3+4/6)


# In[11]:


print ("Or you can compare numbers like: 2+3<5+1?", 2+3<5+1)


# # Variables and Names

# Variables and numbers are shortcuts, so to speak, that can be given to numbers. To make it clearer, you are giving a numeric value to a letter or sentence. This serves for too many things, such as to do chain actions. In fact, they are the basis of number system converters and many other programs.

# ###### EXAMPLE

# In[19]:


calif1 = 90
calif2 = 95
calif3 = 80
e=15

print("Sum Ratings:", calif1+calif2+calif3)

print("Total Score:", calif1+calif2+calif3+e)


# # More Variables and Printing

# We can also use variables between text using "f{here_is_the_name_of_the_variable}".We use the "f" to stablish an order to python put variables in the string. This has some uses to elaborate personalized text and save some time to avoid writting the same number and instead use variables and names.

# ###### EXAMPLE

# In[21]:


calif1 = 90
calif2 = 95
calif3 = 80
e=15

print(f"Well mom, in Englis, my actual grade is {calif1}")
print(f"In Derivative Calculous is {calif2}")
print(f"But I  got {calif3} in PLC")
print(f"Oh i also have {e} extra points")


# # Strings and Text

# Strings are the lines of text that we have been using since now. They can contain variables, numbers and formats. 
# Python knows when we want to use a string when we put a text in quotes or double-quotes.
# We can print the strings in order to show the text outside the code. But we can also save strings in variables. The principal function I see to this is avoiding "copy paste" when you are going to write the same thing several times.

# ###### EXAMPLE

# In[27]:


he = "His" # Variables
she = "Her" # Variables
x = "name is" # Variables
c = "Carlos" # Variables
p = "Pepe" # Variables
k = "Karla" # Variables
m = "Montse" # Variables

print(f"{he} {x} {c}") # Printing Variables
print(f"{he} {x} {p}") # Printing Variables
print(f"{she} {x} {k}") # Printing Variables
print(f"{she} {x} {m}") # Printing Variables
print("You see what I did? :D") # Just text


# # More Printing

# I only understood that we can also multiply text. Maybe this will be useful to do some repetitions.

# ###### EXAMPLE

# In[39]:


print("Umbrella - Rihana (chorus)")

el = "ella"
e = "eh"
print("Under my umbrella, ella, ella, eh, eh, eh \n" * 3)


# #  Printing, Printing

# ###### Invalid Understanding

# I didn't understand this exercise :(

# # Printing, Printing, Printing

# In this last "print" section we can see that we can also stablish variables in a list form, using "\n", but we can also use this to do other things, like a line jump.

# ###### EXAMPLE

# In[41]:


cellphones = "Samsung\nHuawei\nApple"

print(cellphones)


# # What Was That?

# We can use the backslash to type some characters that are difficult for the programming language to interpretate. For example a to use vignettes, use a tab, or a simple backslash.

# ###### EXAMPLE

# In[49]:


print("\t This is with a tabulation")
print("This is without a tabulation \n")
print("\\ A backslash")
print("\t*a \n \t*b \n \t*c")


# In[ ]:




