"""Swap the casing of a given string at the specified indices.
"""
#  Taking string 'omprakash' in this swap lower case 'p' & 'k' in to upper case by using index and .upper method

x = 'omprakash'

str_sc = x[0:2]+x[2].upper()+x[3:5]+x[5].upper()+x[6:]  #  work for all charcters >6 

print(str_sc)  #  It will print as 'omPraKash'



#  Taking string 'omprakash' in this swap  all letters to uppercase by using .swapcase method

str_sc2 = x.swapcase()  # It will convert all lower case to upper case letter 

print(str_sc2)  #  It will print as 'OMPRAKASH'
