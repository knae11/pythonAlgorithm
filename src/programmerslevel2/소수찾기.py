from itertools import permutations
import math


def isPrime(primes, combi):
    string = ""
    for i in range(len(combi)):
        string += combi[i]
    number = int(string)
    if number in primes:
        return 0
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return 0
    else:
        primes.add(number)
        return 1


def solution(numbers):
    answer = 0
    cards = [i for i in numbers]
    primes = {0,1}
    for i in range(1, len(numbers) + 1):
        for combi in permutations(cards, i):
            answer += isPrime(primes, combi)
    return answer