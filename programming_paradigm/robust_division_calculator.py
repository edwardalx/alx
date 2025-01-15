def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError :
        result = "Error: Cannot divide by zero."
        return result
    except ValueError:
        result = "Error: Please enter numeric values only."
        return result

