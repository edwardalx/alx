num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case _ if operation == "+":
        result = num1 + num2
        print (f"The result is {result}")
    case _ if operation == "-":
        result = num1 - num2
        print (f"The result is {result}")
    case _ if operation == "*":
        result = num1 * num2
        print ("The result is", {result})
    case _ if operation == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print (f"The result is {result}")
       
    case _:
        print("Please enter (+, -, *, /) in the operation")