from operator import le

from yaml import serialize


def get_fibonacci(length):
    a, b, series = 0, 1, [0, 1]
    for i in range(length):
        next_num = a + b
        series.append(next_num)
        a = b
        b = next_num
    return series
       
       

series = get_fibonacci(15)
print(series)