# This is a sample Python script.
import math
import random


def near_miss():
    iterate = 30
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    z = random.randint(0, 1000)

    print("Simple program that produces near-misses of integer triplets that would satisfy a^n + b^n = c^n for some n "
          "> 2\n")

    n: int = int(input('Enter a number greater than 2: '))
    miss = 0
    i = 1

    while n <= 2:
        x = int(input('Please enter a number greater than 2: '))
        n = x
        return n

    while i <= iterate:
        result = math.pow(x, n) + math.pow(y, n)
        squared = math.pow(z, n)
        difference = result - squared

        n += 1
        i += 1

        if difference == squared:
            print('No Misses')
        else:
            miss += 1
            if i == iterate:
                print('total number of misses: ' + str(miss) + ' Iterations: ' + str(i))


if __name__ == '__main__':
    near_miss()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
