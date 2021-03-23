# Strings and Casting

# Let's have a look at some industry practices
# single and double quotes examples

# single_quotes = 'single quotes \'WoW\''
# double_quotes = "double quotes 'WOW' "
# print(single_quotes)
# print(double_quotes)


# String slicing

#greetings = "Hello world!" # string
# indexing in Python starts from 0
# H e l l o   w o r l  d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
# how can we find out the length of this statement/string

#print(len(greetings))
# We have a method called len() to find out the total length of the statement
#

# # Let's have a look at some strings methods
# white_space = "lot's of space at the end                        "
# # strip() helps us delete all white spaces
# print(len(white_space))
# print(len(white_space.strip()))

# Example_text = "here's Some text with lot's of text"
# #print(Example_text.count("text"))
# # Counts the number of times the word is mentioned in the statement
# print(Example_text)
# print(Example_text.upper())
# print(Example_text.lower())
# print(Example_text.capitalize()) # Capitalises first letter of the string
# print(Example_text.replace("with", ","))
# # will replace the word "with" , in this case

# Concatenation and Casting

First_Name = "James"
Last_Name = "Bond"
age = 99 # int
#print(First_Name + " " + Last_Name + " " + str(age))
#print(type(int(age)))

# F- String is an amazing Magical formatting f
print(f"Your First Name is {First_Name} and Last Name is {Last_Name} and you are {age} old")











