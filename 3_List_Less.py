
#List of numbers
first_list = [1,2,3,4,5,6,7,8,9,10]

#User number
user_input = int(input("Give me a number: "))

#Create list of numbers less than user number
second_list = []

for i in first_list:
    if i < user_input:
        second_list.append(i)
print (second_list)
