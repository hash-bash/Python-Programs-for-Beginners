print()
toc = {"Introduction": 1, "Chapter 1": 4, "Chapter 2": 11, "Chapter 3": 25, "Chapter 4": 30}
toc["Epilogue"] = 39
toc["Chapter 3"] = 24
del toc["Chapter 4"]
print("Chapter 5" in toc)
print(toc)
print(toc.values())
print(toc.keys())

print()
cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for a, b in cool_beasts.items():
    print("{} have {}".format(a, b))

print()
wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for x in wardrobe:
    for y in wardrobe[x]:
        print("{} {}".format(y, x))

print()
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)
