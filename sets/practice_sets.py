Weak = {"mon","tue","wed","thu","fri","sat","Sunday"}

print(Weak)
print(type(Weak))
print(len(Weak))
print(max(Weak))
print(min(Weak))

a = {1,3,4,5,"ASHU",'a'}
b = {1,2,5,6,5,6,'a'}
print("Set is",a)
print(len(a))
# print one by one 
for i in a:
    print(i)
# in add we only add one word
a.add("Mishra",)
print("Updated set",a)

# in update we add multiple words
a.update(["HEY","How","ARE","YOU"])

print("Updated SET",a)

# Removing word 

a.discard("Mishra")
print("removed ",a)

# Compare b/w two sets

print(a.intersection(b))

