#m= str(input("Enter some String___"))
#j=reversed(m)
#output = ''.join(j)
#for x in j:
#    print(x)
#print(output)


#print(m[::-1])

#a= "Manoj"
#output=''
#i = len(a)-1
#print(i)
#while i >= 0:
#    output=output+a[i]
#    i=i-1
#print(output)

# Write program to reverse order of words
#Ans-

#s = str(input("enter any string -"))

#i = s.split()

#print(i[::-1])
#i1 = i[::-1]
#j=' '.join(i1)
#print(j)




#m = 'Manoj joshi'
#m1 = m.split()
#print(m1[::-1])
#m2 = m1[::-1]
#output = ' '.join(m2)
#print(output)

# QUE - reverse internal words of string
#m= str(input("enter some string_"))
#j=m.split()
#print(j)
#n = j
#r = []
#for x in n:
#    r.append(x[::-1])
#output = ' '.join(r)
#print(output)

# Que - Print even and odd caraters

#m = 'Manohjjhh'
#i=0
#print("evan chartecters-")
#while i<len(m):
#    print(m[i])
#    i=i+2

#print(m[1::2])

a = "a3z2b4"
c=''
for ch in a:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        c=c+x*d
c=sorted(c)
c1=''.join(c)
print(c1)



































