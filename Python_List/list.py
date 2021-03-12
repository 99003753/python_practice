# here we do simple list program
a =[1,2,3,4,4.70,6]
b = ["ASHU_MISHRA",7,4,988888,1.222]

print(a==b)
# here print the list
print(a)
print(b)
print(list[a])
print(list[b])
# here we find the length of the list
print(len(a))
print(len(b))


# sum of list a

sum=0
for i in a:
    sum = sum+i
print(sum)

# common element
for x in a:
    for y in b:
        if x==y:
            print(x)

