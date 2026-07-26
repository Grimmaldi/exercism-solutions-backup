def sieve(final_number):
    searchpt = 0
    result = list(range(2, final_number + 1))
    temp = result[searchpt:]
    remove_list = [result[searchpt] * number for number in list(range(2,len(temp)))]

    while searchpt < len(temp):
        for number in remove_list:
            if number in temp:
                result.remove(number)
        searchpt += 1
        temp = result[searchpt:]
        remove_list = [result[searchpt] * number for number in list(range(2, len(temp)))]

    return result

print(sieve(1000))