print("Welcome to The Data Analyzer and Transformer Program")

data = []

def input_data():
    """Get input from user and store into Array"""
    global data

    print("choose one option:")
    print("1. 1D Array")
    print("2. 2D Array")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        values = input("Enter data for a 1D array (Separated By Spaces): ").split()
        data = list(map(int, values))
        print("Data has been stored successfully!")

    elif choice == 2:
        data = []  
        rows = int(input("Enter Number Of Rows: "))
        columns = int(input("Enter Number Of Columns: "))

        for i in range(rows):
            row = []
            for j in range(columns):
                num = int(input("Enter The Number: "))
                row.append(num)
            data.append(row)  

        print("Data has been stored successfully!")

    else:
        print("Invalid Choice!!")


def converter(data):
    """Flatten nested row data into a 1D list when needed."""
    if len(data) > 0 and isinstance(data[0], list):
        values = []
        for i in data:
            values.extend(i)
        return values
    else:
        return data


def summary():
    """shows summary of the current dataset."""
    values = converter(data)

    if len(values) == 0:
        print("No data found.")
        return

    print("Data Summary:")
    print(f"- Total Elements: {len(values)}")
    print(f"- Minimum Value: {min(values)}")
    print(f"- Maximum Value: {max(values)}")
    print(f"- Sum of all values: {sum(values)}")
    print(f"- Average Value: {sum(values) / len(values)}")
    print()


def factorial(n):
    """Calculate Factorial"""

    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fact_data():
    """Factorial using recursion."""
    num = int(input("Enter Your Number for Factorial: "))

    if num < 0:
        print("Please enter a greater number because Factorial is not defined for negative numbers.")
        return

    a = factorial(num)
    print(f"Factorial of {num} is: {a}")


def thresold():
    """Filtering values using lambda & filter."""
    values = converter(data)

    if len(values) == 0:
        print("No data found.")
        return

    value = int(input("Enter a threshold value: "))

    a = filter(lambda x: x > value, values)
    print("Values greater than threshold:")
    print(list(a))


def sort():
    """Sorting into ascending or descending order."""
    values = converter(data)

    if len(values) == 0:
        print("No data found.")
        return

    print("Select An Option (1-2):")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        values = sorted(values)
        print(f"Sorted data in Ascending order: {values}")

    elif choice == 2:
        values = sorted(values, reverse=True)
        print(f"Sorted data in Descending order: {values}")

    else:
        print("Invalid Choice!!")


def statistics(values):
    """Return minimum, maximum, total, and average values."""
    values = converter(values)

    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = total / len(values)

    return minimum, maximum, total, average


while True:

    print()
    print("Main Menu:")
    print("1. Input Data")
    print("2. Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Data Set Statistics (Return Multiple Values)")
    print("7. Exit Program")
    print()

    ch = int(input("Please Enter Your Choice: "))

    if ch == 1:
        print(input_data.__doc__)
        input_data()

    elif ch == 2:
        print(summary.__doc__)
        summary()

    elif ch == 3:
        print(fact_data.__doc__)
        fact_data()

    elif ch == 4:
        print(thresold.__doc__)
        thresold()

    elif ch == 5:
        print(sort.__doc__)
        sort()

    elif ch == 6:
        print(statistics.__doc__)
        if len(converter(data)) == 0:
            print("No data found.")
        else:
            minimum, maximum, total, average = statistics(data)
            print(f"Minimum Value: {minimum}")
            print(f"Maximum Value: {maximum}")
            print(f"Sum of all Value : {total}")
            print(f"Average Value: {average}")

    elif ch == 7:
        print("Thank you for using the program. Goodbye!")
        break

    else:
        print("Invalid Choice! Please enter a number from 1 to 7.")