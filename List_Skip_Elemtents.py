def skip_elements(elements):
    list1 = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            list1.append(element)
    return list1


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
