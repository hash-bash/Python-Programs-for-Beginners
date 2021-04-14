def sum_divisors(n):
    sum = 0
    i = 0
    while i < n:
        if i != 0:
            if n % i == 0:
                sum = sum + i
        i += 1
    return sum


print(sum_divisors(0))
print(sum_divisors(3))  # Should be sum of 1
print(sum_divisors(36))  # Should be sum of 1+2+3+4+6+9+12+18
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
