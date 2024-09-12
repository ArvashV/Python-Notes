n = int(input("Enter the number whose factorial you want to be printed: "))
factorial = 1

# Checking if the input number is negative, zero, or positive
if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0 or n == 1:
    print("The factorial of", n, "is 1.")
else:
    for i in range(1, n + 1):
        factorial *= i

    print("The factorial of", n, "is", factorial)


# 4-> range (1,5)-> f =1, f=2, f=6, f=24 done....
