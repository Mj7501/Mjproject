#a = [[1,2,3],[4,5,6],[7,8,9]]
#print(a)
#for ec in a:
#    print(ec)
#print("list in matrix style")
#for x in range(len(a)):
#    for y in range(len(a[x])):
#        print(a[x][y],end=' ')
#    print()

Vovels = ['a','e','i','o','u']
name = str(input("Enter some string to find vovels-"))
found = []
for ec in name:
    if ec in Vovels:
        if ec not in found:
            found.append(ec)
print("vovls in",name,"are",found,"count of Vovels = ",len(found))


