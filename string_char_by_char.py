import time

x = input("Enter the string: ")
length = len(x) # length method to get the length of the string

for i in range(0, length):
    time.sleep(0.2)
    print(x[i])