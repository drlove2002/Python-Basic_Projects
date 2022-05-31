from add_2_num import get_numbers


def is_smaller(num1: int, num2: int) -> bool:
    return num1 < num2


def main() -> None:
    numbers = get_numbers(2)
    if is_smaller(numbers[0], numbers[1]):
        print(f"{numbers[0]} is smaller than {numbers[1]}")
    else:
        print(f"{numbers[0]} is larger than {numbers[1]}")


if __name__ == "__main__":
    main()
