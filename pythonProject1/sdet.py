# How To Swap 2 Numbers
# ans1
# num1 = 10
# num2 = 20
#
# num2,num1=num1,num2
#
# # ans 2
# num3 = num1
# num1 = num2
# num2 = num3
#
# print(num1)
# print(num2)
import re

import numpy as numpy

# Topic : How To Check A Number is Prime Or Not

# num = int(input("Enter some number -"))
# count = 0
# #
# # if num > 1:
#     for i in range(1,num+1):
#         if num%i == 0:
#             count += 1
#     if count == 2:
#         print("Number is prime")
#     else:
#         print("number is not prime")
# else:
#     print("pleasee enter no grater than 1")

# factorial = 1
# num = int(input("enter some no -"))
#
# if num == 0:
#     print("factorial of 0 is 1")
# if num < 0:
#     print("factorial dose not support negative no")
# else:
#     for i in range(1,num+1):
#         factorial= factorial*i
#     print("factorial of ",num,"is",factorial)
#

# def factorial(n):
#     return 1 if(n==1  or n==0) else n*factorial(n-1)
# num = 5
# print("factorial of ",num,"is",factorial(num))

# Topic : Print Fibonacci Series

# n1 = 0
# n2 = 1
#
# print(n1)
# print(n2)
#
# for i in range(2,15):
#     sum =  n1+n2
#     print(sum)
#     n1 = n2
#     n2 = sum
# Topic : Find Sum Of Elements in an Array
# arr =  [1,5,44,5,88]
#
# print(sum(arr))
# # sum + 10
# print(sum(arr,10))
# # sum - 10
# print(sum(arr,-10))

# Topic : Find Maximum & Minimum Elements in an Array

# arr = [1,2,3,4,5,6,7]
# max = arr[0]
# min = arr[0]
# n= len(arr)
#
# for i in range(1,n):
#     if arr[i]>max:
#         max=arr[i]
#     elif arr[i]<min:
#         min=arr[i]
# print("max no in arry",max)
# print("minimum no in arry",min)



# 1) How To Find Length of a List

# mylst = [1,2,2,3,1,2,5,6]
# count = 0
#
# for i in mylst:
#     count = count+1
# print(count)
#
# # eg 2
# print(len(mylst))

# Topic : How To Swap First & Last Elements of a List

# mylst = [1,2,3,1,4,5,6]
# size =  len(mylst)
# temp = mylst[0]
# mylst[0]=mylst[size-1]
# mylst[size-1]=temp
# print("swapped list = ",mylst)
#
# # Aproach2
# mylst[0],mylst[-1]=mylst[-1],mylst[0]
# print("swapped list = ",mylst)

# Topic : How To Swap Any 2 Elements of a List
# lst = [1,2,3,4,5,6,7,8,9,10]
# lst[2],lst[-2]=lst[-2],lst[2]
# print(lst)

# Topic : How To Remove Nth occurrence of the word from a List

# mylst =["geeks","for","geeks"]
# word = "geeks"
# n = 2
# count = 0
#
# for i in range(0,len(mylst)):
#     if mylst[i] == word:
#         count = count+1
#         if count == n:
#             del mylst[i]
# print(mylst)

# Topic : How To Search an Element in a List

# mylist = [1,2,3,4,5,6]
# ele = 5
# flag = 0
#
# for i in mylist:
#     if i == ele:
#         print("element found")
#         flag = 1
#         break
# if flag == 0:
#     print("element not in list")
#
# if (ele in mylist):
#     print("element found")
# else:
#     print("element not in list")


# Topic : How To Clear a List
# mylst = [1,2,3,4,5,6,7,8,9]
# # eg1
# mylst.clear()
# print(mylst)
# # eg2
# mylst=[]
# print(mylst)
# # eg3
# del mylst[:]
# print(mylst)

# Topic : How To Reverse a List

# mylst = [1,2,3,4,5,6,7,8,9]
# mylst.reverse()
# print(mylst)
#
# # eg2
# ylst = mylst[::-1]
# print(ylst)

# How To Clone or Copy a List
# mylst = [1,2,3,4,5,6,7,8,9]
# print(mylst)
# #eg1
# mylst_copy1 = mylst[:]
# print(mylst_copy1)
# #eg2
# mylst_copy2 = mylst
# print(mylst_copy2)
# # eg3
# mylst_copy3 =[]
# mylst_copy3.extend(mylst)
# print(mylst_copy3)
# # eg4
# mylst_copy4 = [i for i in mylst]
# print(mylst_copy4)


# mylist = [1,1,1,2,3,4,4,4,4,5,5,6,6,8,8,88,]
# x = 5
# count = 0
# for i in mylist:
#     if i == x:
#         count=count+1
# print(count)
#
# # eg2
# print(mylist.count(x))
#
# # for all accurences
#
# import collections
# from collections import Counter
#
# dec = (Counter(mylist))
# print(dec)


# Topic : Find Sum of Elements in the List

# # eg1
# myleast = [10,20,30,40,50]
# print(sum(myleast))
# # eg2
# total = 0
# for i in range(0,len(myleast)):
#     total = total+myleast[i]
# print(total)

# Topic : Multiply All Numbers in the List
# mylst = [2,2,2,2]
# mul =  1
# for i  in mylst:
#     mul = mul*i
# print(mul)
# # eg2
# import numpy
# result = numpy.prod(mylst)
# print(result)

# Topic : Find Smallest & Largest Numbers in a List
# mylst = [10,5,8,9,6,2,52,11]
# mylst.sort()
# print(mylst)
# print("small no - ",mylst[0])
# print("large no -",mylst[-1])
#
# # eg2
# print("min no",min(mylst))
# print("max no  -",max(mylst))


#Topic : Find 2nd Largest Number in a List
# mylst = [22,54,82,5,24,88,6,7,99]
# mylst.sort()
# print("max no - ",mylst[-1])
# print("min no - ",mylst[0])

# Topic : Check String is Palindrome or Not
# s = input("Enter some str =")
# rev_s = s[::-1]
# if s==rev_s:
#     print("its a palidrome str")
# else:
#     print("its not a palidrome str")

# How t reverse a str
# mystr = input("enter some str =")
# # eg1 reversed line
# print(" ".join(reversed(mystr.split( ))))
#
# # eg2 reversed words
# print("".join(reversed(mystr)))
#
# mystr_copy = mystr[::-1]
# print(mystr_copy)


# Topic : How To Find Length of a String

# str =  input("enter some str-")
# count = 0
# for i in str:
#     count = count+1
# print(count)
#
# # eg2
# print(len(str))

# Topic : Check if a string contains any special character
# import  re
# str = "*()&&^%manoj^^&is@@!#greate"
# regex = re.compile('[~!@#$%^&*()]')
#
# if regex.search(str)==None:
#     print("sc is not present in given string")
# else:
#     print("sc is present in given string")

# Topic : Check for URL in a String
# import re
# # https://urlregex.com/ (to search reg expressions for py)
#
# # http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
# str ="https://www.youtube.com/watch?v=Nk-CJcDZkAc&list=PLUDwpEzHYYLv"
# url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)
# print(url)

# sort list by second char

# mylst = ('india', 'china', 'france', 'usa', 'germany')
# lst1 =[]
# lst2 = []
#
# for i in mylst:
#     lst1.append(i[1])
# lst1.sort()
# for h in lst1:
#     for j in mylst:
#      if h == j[1]:
#         lst2.append(j)
#
# print(lst1)
# print("sorted list by secont char",lst2)

# 26) input = a4s5d6f7     output = aaaasssssddddddfffffff

# str = "a4s5d6f7"
# outp = ''
# x = ''
# d = ''
#
# for ch in str:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch)
#         outp = outp+x*d
# print(outp)

# s = "aaaaabbbbbcccccdddddd"
# previous = s[0]
# i = 1
# f = 1
# output = ''
#
# while i<len(s):
#     if s[i] == previous:
#         f = f+1
#     else:
#         output = output+previous+str(f)
#         previous = s[i]
#         f = 1
#     if i == len(s)-1:
#         output=output+str(f)+previous
#     i = i+1
# print(output)


# input = a4b3c6g9      output =aebecigp

# s = "a4b3c6g9"
# x = ""
# h = ""
# newc = ""
# output =""
#
# for i in s:
#     if i.isalpha():
#         output=output+i
#         x = i
#     else:
#         d = int(i)
#         newc = chr(ord(x)+d)
#         output = output+newc
#
# print(output)

# 29) how to  remove duplicate of list

s = "xdcftvgbhjnmkbbvbnfcvfcvvhxxasdfasdfasdfasd"
# output = ""
# for ch in s:
#     if ch not in output:
#         output = output+ch
# print(output)
# # eg2 sorted str
# l = [ ]
# output = " "
# for ch in s:
#     if ch not in l:
#         l.append(ch)
#         l.sort()
#     output = "".join(l)
# print(output)

# input = "ABAABBCA"     output = "4A3B1C"
# s = "ABAABBCA"
# output = ''
# x = {}
# for ch in s:
#     x[ch]=x.get(ch,0)+1
# for k,v in sorted(x.items()):
#     output=output+str(v)+k
# print(output)

mystr = "asexdrfftgbhujnok"
vowels = "AEIOUaeiou"
outp = ''
for ch in mystr:
    if ch in vowels:
        outp=outp+ch
print("vowels found = ",outp)

v = ["A","E","I","O","U","a","e","i","o","u"]
d = {}
for i in mystr:
        if i in v:
            d



































































































































































