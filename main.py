def input_data():
    global data
    print("")
    print("1. For 1D array")
    print("2. For 2D array")

    choice = int(input("Enter the choice: "))

    if choice == 1:
        num= input("Enter the numbers with separated by spaces: ").split()
        data = list(map(int, num))
        print("Data has been stored successfully.")

    elif choice == 2:
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))

        for i in range(rows):
            a=[]
            for j in range(columns):
                num = int(input("Enter the number: "))

                data.append(a)
            print("Added successfully.")

    else:
        print("Invalid input")


def summary(data):

    if len(data) > 0:
        for i in data:
            if type(i) == list:
                data.extend(i)
            else:
                data.append(i)

        print("Data Summary")
        print("Total elements:", len(data))
        print("Minimum value is:", min(data))
        print("Maximum value is:", max(data))
        print("Sum of all values is:", sum(data))
        print("The average is:", sum(data) / len(data))

    else:
        print("No data available")


def fact(num):
    if num <= 1:
        return 1

    return num * fact(num - 1)


def factorial():
    num = int(input("Enter the number: "))

    fact = fact(num)

    print(f"Factorial of {num} is {fact}")


def threshold(data):
    
    for i in data:
        if type(i) == list:
            data.extend(i)
        else:
            data.append(i)

    threshold = int(input("Enter the threshold value to filter out data above this value: "))

    threshold_val = list(filter(lambda x: x > threshold, data))

    print(f"Values greater than threshold are:{threshold}")


def sorting(data):
    for i in data:
        if type(i) == list:
            data.extend(i)
        else:
            data.append(i)

    print("Select an option:")
    print("1. Ascending")
    print("2. Descending")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data.sort()
        print(data)

    elif choice == 2:
        data.sort(reverse=True)
        print(data)

    else:
        print("Invalid choice")


def calculate_data(data):
    for i in data:
        if type(i) == list:
            data.extend(i)
        else:
            data.append(i)

    total = len(data)
    sum = sum(data)
    minimum = min(data)
    maximum = max(data)
    avg = sum / total

    return total,sum, minimum, maximum, avg


def statistics(data):
    sum, minimum, maximum, avg = calculate_data(data)

    print("Sum:", sum)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", avg)


data = []

while True:
    print()
    print("Welcome to the Data Analyzer and Transformer program")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Threshold Value")
    print("5. Sorting Data")
    print("6. Statistics Data")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        summary(data)

    elif choice == 3:
        factorial()

    elif choice == 4:
        threshold(data)

    elif choice == 5:
        sorting(data)

    elif choice == 6:
        statistics(data)

    elif choice == 7:
        print("Thank you for using system.")
        break

    else:
        print("Invalid choice")

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