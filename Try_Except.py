def function1():
    rate = float(input("Enter the rate: "))
    hours = float(input("Enter the hours: "))

    if hours > 40:
        pay = 40 * rate
        hours2 = hours - 40
        rate2 = rate * 1.5
        pay2 = rate2 * hours2
        print("Pay :", pay + pay2)
    else:
        pay = rate * hours
        print("Pay:", pay)


try:
    function1()
except Exception as e:
    print("Enter float or integer value only.")
