# l = ('india', 'china', 'france', 'usa', 'germany')
# p = []
# q = []
# for i in l:
#     p.append(i[1])
# p.sort()
# print(p)
# for c in p:
#     for h in l:
#         if c == h[1]:
#          q.append(h)
#
# print(q)


s = "aaaaabbbbbcccccddddddaaaa"
prev=s[0]
i=c=1
out=''
while i<len(s):
    if s[i]==prev:
        c+=1
    else:
        out=out+prev+str(c)
        prev=s[i]
        c=1
    if i==len(s)-1:
        out=out+prev+str(c)
    i+=1
print(out)








