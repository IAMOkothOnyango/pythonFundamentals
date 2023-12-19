def raiseToPower(base, exponent):
    result = 1
    for index in range(exponent):
        result = result * base
    return result

print(raiseToPower(2, 3))