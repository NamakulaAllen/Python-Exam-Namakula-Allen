#Base = 2, Height = 3
def calculate_rectangle_area(base, height):
    return 0.5 * base * height

def main():
    try:
        base = float(input("Enter the base of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))

        area = calculate_rectangle_area(base, height)

        print("The area of the rectangle is:", area)
    except ValueError:
        print("Please enter valid numeric values for base and height.")

if __name__ == "__main__":
    main()


