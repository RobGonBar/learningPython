#Compares 2 lists and returns the values that they share in common
import random


a = []
b = []
overlap = []
list_length = random.randint(1,30)

while(len(a) < list_length):
    a.append(random.randint(1,20))
while(len(b) < list_length):
    b.append(random.randint(1,20))
overlap.append(set(a) & set(b))

a.sort()
b.sort()
print(str(a) + "\n" + str(b))

print(overlap)
