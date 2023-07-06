#How to reverse a sentence in Python input by User
# revercep = input("enter string - ")
# print("reversed string = "," ".join(reversed(revercep.split())))
#
# print("reverced words =","".join(reversed(revercep)))

#2. How to find the characters at an odd position in string input by User

# entersomestring = input("enter some string -")
# outputstr =''
#
# for i in range(len(entersomestring)):
#     if i % 2 == 0:
#         outputstr = outputstr + entersomestring[i]
#
# print("input string -",entersomestring)
# print("string affter odd char - ",outputstr)


#3. How to check string start with specific character enter by the user.

# string = input("enter some string -")
#
# result =  string.startswith('Python')
# print(result)

#4. How to remove all newline from the String.

# inputstr = "'\nPython String\n with\n newline\n'"
# print(inputstr)
#
# strwithoutline = inputstr.replace('\n',"")
#
# print(strwithoutline)

#5.Different ways to get the filename without extension
# import os
#
# inputstr = input("enter some name without is (if u use if still it will not display)")
#
# xyz = inputstr.replace('is','')
# print(xyz)
#
#

#
# inputstr = input("inpute some str-")
# totaluppercase=0
# lowercasecount=0
#
# for i in inputstr:
#     if i.isupper():
#         totaluppercase+=1
#     elif i.islower():
#         lowercasecount+=1
#
# print(inputstr)
# print(totaluppercase)
# print(lowercasecount)

# inputstr = input("enter some string")
#
# print(" ".join(reversed(inputstr.split())))
# print("".join(reversed(inputstr)))
#
# inputstr = input("Enter some string - ")
# oddchar = ''
#
# for h in range(len(inputstr)):
#     if  h % 2 == 0:
#         oddchar=oddchar+inputstr[h]
#
# print(oddchar)


# inputstr = input("enter some str = ")
# if inputstr.startswith("Python"):
#     print("right")
# elif inputstr.startswith("python"):
#     print("right")
# else:
#     print("wrong")

# inputstr = "'\nPython String\n with\n newline\n'"
# newlineremoved = inputstr.replace('\n',''),inputstr.replace('with','without')
# print(newlineremoved)

#8. How to find the number of matching characters in two string
# import re
# str1 = "python is simple language"
# str2 = "python is"
#
# matching_char = 0
# for char in str1:
#     if re.search(char,str2):
#         matching_char+=1
# print(matching_char)


# str = '1,J,K,B,G,JJ,HJ,HBJ'
# print(list(str.split(',')))

# numlist = ['1', '9', '8', '7', '6', '5', '4', '4']
# numlist = [int(num) for num in numlist]
# print(numlist)

# 12.Count Total numbers of upper case and lower case characters in input string
# inputstr = input("enter some str")
# uppercase=0
# lowercase=0

# for char in inputstr:
#     if char.isupper():
#         uppercase+=1
#     elif char.islower():
#         lowercase+=1
#
# print(uppercase)
# print(lowercase)

# inputstr = input("input some str =")
# vowels ="AEIOUaeiou"
# vowels_found = ''
# vowelsare  = 0
#
# for char in inputstr:
#     if char in vowels:
#         vowels_found = vowels_found+char
#
# print(vowels_found)
# print(len(vowels_found))

# 16. How to print input string in upper case and lower case

inputstr = input("enter some str = ")

print("upper case in current str =",inputstr.upper())




































































