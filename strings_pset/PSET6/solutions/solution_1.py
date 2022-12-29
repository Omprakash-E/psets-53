"""Write a python script that reads the first and last name of a person and returns the full name.
"""
# first name = Manoj
# last name = Kumar
first_name = input("Enter your first name\n")  #  get the first name of user
last_name = input("Enter your last name\n")  #  get the last name of user
full_name = first_name + last_name
# print(full_name) # it gives the output without space between two names

full_name_space = first_name + " " +last_name  #  space present between first and last name
# print(full_name_space)

#  print(f'{first_name} {last_name}') # using 'f' strings creating the space between first and last name

# print(first_name,last_name)  #  normal print function it will create space between first and last name
full_name_1 = full_name
full_name_1 =  full_name_1[0:4]+ " " + full_name_1[4:]  # Hardcoded solution
#  print(full_name_1)



full_name_2 = full_name[0:len(first_name)] + " " + full_name[len(first_name):]  # Generalized version
# print(full_name_2)

len_first_name = len(first_name)  #  assigning variable  to len(first_name)
print(full_name[0:len_first_name],full_name[len_first_name:]) # user to read easily
