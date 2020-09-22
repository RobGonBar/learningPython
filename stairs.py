#Interview question - Staircase
x = {1,2}

def numWays(n, x):
    if n == 0:
        return 1
    nums = [n+1]
    nums[0] = 1
    for i in range(n+1):
        total = 0
        for j in x:
            if i-j >= 0:
                total += nums[i-j]
        nums[i] = total
    return nums[n]

print(numWays(4,x))
