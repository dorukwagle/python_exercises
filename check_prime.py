from re import T


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")