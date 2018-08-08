#Finds all the even numbers in list a
import random
b = []

#Creates a random length list between 5 and 15 numbers long
list_length = random.randint(5,15)

#While the length of the random list is less than then random list length, add random numbers from 1 - 75
while len(b) < list_length:
    b.append(random.randint(1,75))

evenlist = [x for x in b if x % 2 == 0]

print("All: ")
print(b)
print("Evens: ")
print(evenlist)

#To do it in one line:

#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [x for x in a if x % 2 == 0]
# print(b)
