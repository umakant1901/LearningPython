
# For : 1
for i in range(10):
    print(i)

# For : 2

for odd in range(20):
    if (odd % 2) != 0:
        print(odd)

# Nested Loop
for x in range(3):
    for y in range(3):
        print(f"co-ordinate is ({x}, {y})")

# Irerables Loop
for char in "hello":
    print(char)

print("***********")
for fruite in {"apple", "banana", "Mango"}:
    print(fruite)

print("***********")
for item in [1, 2, 3, 4]:
    print(item)


print("***********")
for items in (1, 2, 3, (1, 2)):
    print(items)


# while loop
t = 35

while t > 20:
    print(t)
    t = t-2
