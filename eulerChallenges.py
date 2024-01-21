from math import sqrt
import prime

def eulerchallenge1():
    i = 0
    #Check which numbers are divisible by 3 or 5 and add them together
    for x in range(1, 1000):
        if x % 3 == 0 or x % 5 == 0:
            i = i + x
    return i


def eulerchallenge2():
    i=0
    fiblist = [1, 2]
    while fiblist [-1] <= 4000000:
        fiblist.append(fiblist[-1] + fiblist[-2])
    fiblist.pop()
    for x in fiblist:
        if x % 2 == 0:
            i = i + x
    return i


def eulerchallenge3(): 
    #we need to calculate the highest prime factor of the following very large number
    question_number = 600851475143
    #luckily, we only need to calculate from its square root downwards.
    prime_list = prime.primeListint(sqrt(600851475143))
    prime_list.reverse()
    for x in prime_list:
        #Check if question_number is divisible by a series of primes
        if question_number % x == 0:
            return x
    return 0