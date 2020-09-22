# Checks if 2 numbers in array add to 20
a = [2,4,1,6,5,40,-1]

def twenty(array):
    for i in array:
        number = 20
        seen = []
        if i not in seen:
            seen.append(i)
            if((number-i) in seen):
                    print(str(i) + "," + str(number-i))
        else:
            if((number-i) in seen):
                    print(str(i) + "," + str(number-i))

twenty(a)
