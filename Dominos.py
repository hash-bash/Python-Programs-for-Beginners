def domino():
    for i in range(7):
        for j in range(i, 7):
            print("[ ", i, j, " ]", end=" ")
        print()


domino()
