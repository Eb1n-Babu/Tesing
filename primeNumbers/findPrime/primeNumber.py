import math


def findPrime(num):
    if num >=2:
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True
    else:
        return False

for k in range(1, 100):
    print(findPrime(k), k)

