def friends():
    list1 = ["Ritik", "Saurabh", "Raj", "Akash"]
    curl = ""
    curs = "SomeVeryLargeValue"
    print()
    for list_item in list1:
        if list_item > curl:
            curl = list_item
        if list_item < curs:
            curs = list_item
        print(list_item)
    print("\nLargest: ", curl)
    print("Smallest: ", curs)


friends()
