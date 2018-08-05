#Get user number
user_input = int(input("Choose a number"))

#Create the range of possible numbers to divide by
x = range(1,user_input+1)

#Array of divisors that work
divisors = []

#Try every number in range x, and add the ones that work to divisors array
for elem in x:
    if user_input % elem == 0:
        divisors.append(elem)
print (divisors)
