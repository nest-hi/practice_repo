
name: str = "nestor bora orosco" # str -- String

"""
String slices - a PORTION of a string
"""

#within the [] square brackets we want do denote the starting index and the end index of what we want
print(name[7:11])# - "bora"
# in this example, we want to get all the characters STARTING FROM the letter 'b' into the letter 'a'. 
# Our STARTING letter 'b' has the index [7] and our ENDING letter 'a' has the index [11] and separated by a COLON ':'

print(name[:6]) # - "nestor"
#we can explicitly denote [0] as oun starting index but it is not necessary if we want to START AT THE BEGINING of the string 

print(name[12:])# - "orosco"
# we don't have to explicitly denote our ending index either.

print(name[-11:-7]) # - "bora"
"""
Using the negative numbers INDEX COUNTING:

012..............18
nestor bora orosco
18..............210

guys, if it's weird, don't use it.- :3
"""




"""

Modifying Strings

"""


print(name.upper())# - NESTOR BORA OROSCO
#big

print(name.lower())# - nestor bora orosco
#SMOL

print(name.capitalize())# - Nestor bora orosco
#! notice that this shit looks bad ^    ^  almost like i wanna kill myself for it
#! why aren't the 'b' and the 'o' not capitalize? we'll deal with it ourselves


"""
Notice that our name is separated by spaces. We use spaces to figure out which is the first, last and middle name from our name.
!the .split() method requires a separator string to denote where should there be a chop.
"""


print(name.split(" "))# - ['nestor', 'bora', 'orosco']
# The .split() method returns the string and separates it into chunks or array of strings
# in this case the .split() chopped our string into 3 because we have 2 spaces within the name string.

print(name.split(" ")[1]) # - "bora"
#we can specify which chunks we want to use by denoting the chunk's index

print(name.split(" ")[0].capitalize() , name.split(" ")[1].capitalize() , name.split(" ")[2].capitalize()) # - Nestor Bora Orosco
#! Now that the letter 'b' and 'o' are capitalized, was it even worth it? 🙁




"""

"String is an array of characters."
    it explains why SOME methods related to strings are also applicable to arrays.


"""


array_of_my_name = ['n','e','s','t','o','r',' ','b','o','r','a',' ','o','r','o','s','c','o'] #exactly like the name variable pero imbis na paganon,
# paganire sya XD



#The len() function will return the length of the array/String including the whitespaces.

print(len(name)) # - 18
print(len(array_of_my_name)) # - also 18 as well

#We also point into a single character within a String by denoting its INDEX within the [] square brackets

print(name[0])# - n

#like how we point into a value within an array

print(array_of_my_name[0]) # - n


#we can also create conditional statements with our string values.

print("n" in name) # - True
# this checks if the letter 'n' is inside the name string

#just like in an array

print("n" not in array_of_my_name) # - False
# not in keyword is NEGATION, it checks if the 'n' exist in the string and inverts the boolean that it returns.