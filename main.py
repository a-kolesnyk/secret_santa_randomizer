import random

names = []

while True:
    name = input("Enter a name (or type 'done' to finish): ")

    if name.lower() == 'done':
        break
    else:
        names.append(name)

random.shuffle(names)
pairs = [(names[i], names[(i + 1) % len(names)]) for i in range(len(names))]

print("Random pairs (circular rotation):")
for pair in pairs:
    print(f"{pair[0]} -> {pair[1]}")

