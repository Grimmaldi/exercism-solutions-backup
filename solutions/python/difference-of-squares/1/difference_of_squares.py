def square_of_sum(num):
    total = 0
    for number in range(1, 1 + num):
        total += number
    return total ** 2

def sum_of_squares(num):
    total = 0
    for number in range(1, 1 + num):
        total += (number ** 2)
    return total

def difference(num):
    return square_of_sum(num) - sum_of_squares(num)