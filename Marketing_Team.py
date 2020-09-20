def group_list(group, users):
    mem = ""
    for usr in users:
        if usr != users[-1]:
            mem += usr + ", "
        else:
            mem += usr
    return group + ": " + mem


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"
