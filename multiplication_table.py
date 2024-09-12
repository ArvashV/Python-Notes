import time

x = int(input("Please enter the number whose table you want to be printed: "))

print("This will print the table form y -> z (y included) \n Therefore Please enter the values of Y and Z : ")

y = int(input("Enter Y: "))
z = int(input("Enter Z: "))


for i in range(y, z+1):
    product = x * i
    time.sleep(0.1)
    print(x,"*",i,"=",product)