def factorial(n):
    fct = 1
    for i in range(n + 1):
        if i != 0:
            fct *= i
            print(i)
    return fct


print("\nFactorial of 5 is:", factorial(5))
