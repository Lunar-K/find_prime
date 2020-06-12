import time

def Eprime(x):
    sieve = [True] * x
    m = int(n**0.5)
    for k in range(2, m + 1):
        if sieve[k] == True:
            for j in range(2*k, x, k):
                sieve[j] = False
    return sieve.count(True) - 2

n = int(input('Enter the max: '))
start = time.time()
number_of_prime = Eprime(n) 
print(number_of_prime)
print('time taken:', time.time() - start)