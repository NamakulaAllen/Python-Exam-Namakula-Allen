# X1 =60, X2 =30,Y1 =160.5,Y2 =97.7

import math

def calculate_distance(X1, Y1, X2, Y2):
    distance = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    return distance

def main():
    
    X1 = float(input("Enter the value of X1: "))
    Y1 = float(input("Enter the value of Y1: "))

    X2 = float(input("Enter the value of X2: "))
    Y2 = float(input("Enter the value of Y2: "))

   
    distance = calculate_distance(X1, Y1, X2, Y2)

   
    print("Distance between the points is:", distance)

if __name__ == "__main__":
    main()


