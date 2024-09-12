n = int(input("Enter the number of rows of stars you want to be printed."))

for i in range(0, n):
    for j in range(0, n-i):
        print("*", end=" ")
    print(end="\n")
    