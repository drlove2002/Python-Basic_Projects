while True:
    print("Enter number of row in pattern ")
    row_no = int(input())

    print("Enter 0 or 1")
    Boolean = int(input())
    count = 1

    if Boolean == 1:
        while count <= row_no:
            print("*" * count)
            count = count + 1

    elif Boolean == 0:
        while count <= row_no:
            print("*" * row_no)
            row_no = row_no - 1

    else:
        print("Please check your input \n Only enter integer")

    print("do you wanna retry? \n type(y/n)")
    error = str(input())
    if error == "y":
        print("your input is Y")
        continue
    elif error == "n":
        print("your input is N")
        break
