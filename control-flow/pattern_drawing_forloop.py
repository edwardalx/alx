
a = int(input("What is the size of your pattern: "))
row = a
for i in range(a):
    for j in range(i):
        b = i * j
        print(" " * (row - i - 1), end="")
        print(f"*", end="")
    print()