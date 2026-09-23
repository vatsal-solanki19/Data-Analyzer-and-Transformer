print("Welcome to the Data Analyzer and Transformer Program")
print()

data = []

def input_data():
    global data
    arr = input("Enter data for a 1D array (separated by spaces): ")

    for x in arr.split():
        data.append(x)
        data = list(map(int, arr.split()))

    print("Data has been stored successfully!")


def summary():
    total = sum(data)

    print("Data summary:")
    print("- Total elements: ", len(data))
    print("- Minimum value: ", min(data))
    print("- Maximum value: ", max(data))
    print("- Sum of all values: ", sum(data))
    print("- Average value: ", total / len(data))
    print()


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


def filter_data():
    v = int(input("Enter a threshold value to filter out data above this value: "))
    a = filter(lambda z: z > v, data)
    print(*a, sep=",")


def sort():
    while True:

        print("Choose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sorted Data in Ascending Order:")
            data.sort()
            print(data)
            break

        elif choice == 2:
            print("Sorted Data in Descending Order:")
            data.sort(reverse=True)
            print(data)
            break


def statistics():
    return min(data), max(data), sum(data), sum(data) / len(data)


while True:

    print("\n")
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Function)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort data")
    print("6. Display dataset statistics (Return multiple values)")
    print("7. Exit Program")
    print()

    c = int(input("Please enter your choice: "))

    if c == 1:
        input_data()

    elif c == 2:
        summary()

    elif c == 3:
        n = int(input("Enter a number to calculate its factorial :-"))
        result = factorial(n)
        print(f"Factorial of {n} is :", result)

    elif c == 4:
        filter_data()

    elif c == 5:
        sort()

    elif c == 6:

        minimum, maximum, total, average = statistics()

        print("Dataset Statistics:")
        print("Minimum value :", minimum)
        print("Maximum value :", maximum)
        print("Sum of all value :", total)
        print("Average value :", average)

    elif c == 7:
        print("Thank you for using The Data Analyzer & Transformer Program.")
        break

    else:
        print("Enter valid choice !")