row = 9
for i in range(row):
    for j in range(i):
        print(" ", end="")
    print("*", end="")
    for k in range((row-i)+row-2-i):
        print("-", end="")
    print("*", end="")
    for l in range(i):
        print(" ", end="")
    print()