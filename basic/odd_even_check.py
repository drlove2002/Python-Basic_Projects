def is_odd(number: int) -> bool:
    return number % 2 != 0


def main() -> None:
    n = int(input("Enter a number: "))
    if is_odd(n):
        print("The number is odd.")
    else:
        print("The number is even.")


if __name__ == "__main__":
    main()
