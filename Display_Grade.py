def function1():
    val2 = ""
    val = float(input("Enter Score: "))
    if val >= 0.9:
        val2 = "A"
    elif val >= 0.8:
        val2 = "B"
    elif val >= 0.7:
        val2 = "C"
    elif val >= 0.6:
        val2 = "D"
    elif val < 0.6:
        val2 = "F"
    else:
        print("Enter a correct value.")
    print(val2)


try:
    function1()
except Exception as e:
    print("Enter float or integer value only.")
