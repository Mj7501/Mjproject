# 1.Program to find the max, min number from the list user input.
# listlang = []
# numbers = int(input('enter the number of items in list '))
# for num in range(numbers):
#     item = int(input('Entered number '))
#     listlang.append(item)
# print('entered list =',listlang)
# print("Max number = :", max(listlang), "\nMin number :", min(listlang))
#

# /2. Code to remove duplicate from list using List comprehension

lstnum = [12, 36, 56, 36, 36, 50, 56, 12]
uniquelist = []
for ele in lstnum:
    if ele not  in uniquelist:
        uniquelist.append(ele)

print(uniquelist)

# 3. Program to find the sum of list elements.

# lstnum = [12, 36, 56, 36, 36, 50, 56, 12]
# sum = 0
#
# for num in lstnum:
#     sum = sum+num
# print(sum)


# 4. How to Multiply all the elements of list

# lstnum = [6, 2, 3, 1, 10, 4]
# multi= 1
#
# for num in lstnum:
#     multi = multi*num
#
# print(multi)
#
# # 6.How to reverse the List using slice
# listnum = [45,67,12,14,56,87]
# revercelst = listnum[::-1]
# print(listnum)
# # print(revercelst)
#

# 7.How to flatten a list of lists with a list comprehension
listnum = [[5,6,7,'C#'], ['C++',2,3]]

flatten_list = [ele for  sublist in listnum for ele in sublist]
print(flatten_list)































