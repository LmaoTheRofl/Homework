import math
sum = 0
n = 0
res = 1
while (sum != res):
    res = sum
    sum = sum + (math.pow(-16/25,n))/(math.factorial(2*n))
    sum = round(sum, 4)
    n = n + 1
print(sum)