fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]

# First letter of each
for string in fish:
    print(string[0])

# First three letters of each
for string in fish:
    print(string[0], string[1], string[2])

# longest fish name
print(max(fish, key=len))

# two word fishes
for string in fish:
    if ' ' in string:
        print(string)

# contains cod
for string in fish:
    if 'cod' in string:
        print(string)
        