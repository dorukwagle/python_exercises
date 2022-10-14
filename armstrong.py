def is_amstrong(number):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == number:
        return True
    return False


# for i in range(1, 1000):
#     if is_amstrong(i):
#         print(i)
try:
    print(is_amstrong(int(input("enter a number: "))))
except ValueError as e:
    print(e)