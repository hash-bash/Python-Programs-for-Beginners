def for_counter():
    print()
    sum1 = 0
    for i in range(100):
        print(i)
        sum1 = sum1 + i
    print("\nSum: ", sum1)


def for_rev_counter():
    print()
    list0 = []
    for i in reversed(range(1, 100)):
        list0.append(i)
    print(list0)


def string_traverse():
    print()
    for i in "String":
        print(i)


def simple_while():
    x = 0
    while x < 5:
        print("Not there yet, x=" + str(x))
        x = x + 1
    print("x=" + str(x))
    print()


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    print()


def count_down(start_number):
    current = start_number
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")
    print()


def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1
    print()


def ask_done():
    while True:
        inpt = input("Enter anything: ")
        if inpt == "Done":
            print("Exiting...")
            break
        elif inpt[0] == '#':
            print("Skipping this iteration...")
            continue
            # print("This print statement will not be executed...")


def while_counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x > stop:
            return_string += str(x) + ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x < stop:
            return_string += str(x) + ","
            x += 1
    return_string += str(stop)
    return return_string


print()
simple_while()
attempts(5)
count_down(5)
print_range(1, 5)
ask_done()
for_counter()
for_rev_counter()
string_traverse()
print("\n", while_counter(1, 10))
