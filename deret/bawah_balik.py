row = 5

for i in range(row):
    for j in range(row-1-i):
        print("_", end="")
    print("*")