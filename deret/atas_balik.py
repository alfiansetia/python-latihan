row = 5
for i in range(row):
    for j in range(row-1-i):
        print(" ", end="")
    print("*", end="")
    for k in range(i):
        print("_", end="")
    print()