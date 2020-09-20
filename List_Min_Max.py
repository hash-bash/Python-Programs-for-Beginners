def func(list_passed):
    largest = None
    smallest = None
    for num in list_passed:
        if smallest is None:
            smallest = num
        else:
            if smallest > num:
                smallest = num
        if largest is None:
            largest = num
        else:
            if largest < num:
                largest = num
    print("Maximum is", largest)
    print("Minimum is", smallest)


list1 = []
while True:
    inpt = input("Enter a number: ")
    if inpt != 'done':
        try:
            list1.append(int(inpt))
        except:
            print("Invalid input")
    else:
        func(list1)
        break
