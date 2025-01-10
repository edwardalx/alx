FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return C

def convert_to_fahrenheit(celsius):
    F = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return F

while True:
    try:
     valueToConvert = float(input("Enter the temperature to convert: "))
     break
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
    # valueToConvert = float(input("Enter the temperature to convert: "))
    
unitOfValue = input("Is this temperature in Celsius or Fahrenheit? (C/F):").lower()

if unitOfValue == "c":
    result = convert_to_fahrenheit(valueToConvert)
    print(f"{valueToConvert}°C is {result}")
elif unitOfValue == "f":
    result = convert_to_celsius(valueToConvert)
    print(f"{valueToConvert}°F is {result}")
else:
    print("Invalid temperature. Please enter a numeric value.")
