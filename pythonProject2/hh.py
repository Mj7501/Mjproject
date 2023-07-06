import collections

fru_lst = ['Apple', 'Mango', 'Grapes', 'Mango', 'Apple', 'Cherry', 'Apple', 'Grapes', 'Mango', 'Apple']

fruit_count = collections.Counter(fru_lst)

for fruit, count in fruit_count.items():
    print(fruit, count)

print(fruit_count)

for k,v in fruit_count.items():
    print(k,v)

dic = { }
for i in fru_lst:
    dic[i]=dic[i,0]+1

print(dic)