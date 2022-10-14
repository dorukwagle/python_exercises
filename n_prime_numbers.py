import time

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_primes(total_primes):
    count = 0
    iterator = 2
    prime_lists = []
    while count != primes:
        if is_prime(iterator):
            prime_lists.append(iterator)
            count += 1
        iterator += 1
    return prime_lists

primes = int(input("enter the number of prime numbers to display: "))
start = time.time()
lst = get_primes(primes)
print(*lst[:10], *lst[-10:])
print(time.time() - start)