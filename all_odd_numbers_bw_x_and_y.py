print("This is print all odd number between x -> y \n Please enter the values of x and y.")
x = int(input("Enter x: "))
y = int(input("Enter y: "))

for i in range(x, y+1): 
    if(i%2 != 0):
        print(i)