def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    try:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit:", fahrenheit)
    except ValueError:
        print("Please enter a valid numeric value for temperature.")

if __name__ == "__main__":
    main()