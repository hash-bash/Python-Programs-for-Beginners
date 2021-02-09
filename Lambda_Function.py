sum = lambda a, b: a + b
print("Sum of 20,30 = ", sum(20, 30))

ages = [20, 21, 8, 19, 22, 14, 8, 6]
print("Ages above 18 are: ", list(filter(lambda x: x > 18, ages)))

fruits = ["Mango", "Strawberry", "Litchy", "Banana", "Apple", "Pear", "Blue Berries"]
startsWithA = list(filter(lambda x: x.startswith("A"), fruits))
print("Fruits which start with 'A' are:", startsWithA)

num_list = [10, 20, 40, 22, 33]
doubled_list = list(map(lambda x: x * 2, num_list))
print("Doubled elements are: ", doubled_list)
