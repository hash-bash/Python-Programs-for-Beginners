def odd_numbers(n):
    return [x for x in range(n + 1) if x % 2 != 0]


def renamer(list1):
    return [x.replace(".hpp", ".h") for x in list1]


print(odd_numbers(10))

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
print(renamer(filenames))
