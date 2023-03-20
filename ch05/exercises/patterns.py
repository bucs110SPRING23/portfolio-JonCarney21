def star_pyramid():
    n = int(input("Enter the number of rows: "))

    for i in range(1, n+1):
        # Print spaces before the stars
        for j in range(n-i):
            print(" ", end="")
        
        # Print the stars for this row
        for j in range(2*i-1):
            print("*", end="")
        
        print()

star_pyramid()

def rstar_pyramid(rows):
    for i in range(rows, 0, -1):
        print("*", * i)
        
levels = int(input("Enter the desired height of the pyramid: "))


rstar_pyramid(levels)

