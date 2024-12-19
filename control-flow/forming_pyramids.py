# Number of rows for the pyramid
rows = 5  

# Generate the pyramid
for i in range(rows):
    # Print leading spaces
    print(" " * (rows - i - 1), end="")
    # Print stars
    print("*" * (2 * i + 1))