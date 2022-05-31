def get_numbers(num_count: int) -> tuple:
    numbers = list()
    for i in range(num_count):
        numbers.append(int(input(f"Enter the num_{i+1}: ")))
    return tuple(numbers)


def sum_numbers(first_num: int, second_num: int) -> int:
    return first_num + second_num


def print_result(first_num: int, second_num: int, sum) -> None:
    print(f"The sum of {first_num} and {second_num} is {sum}")


def main() -> None:
    numbers = get_numbers(2)
    sum = sum_numbers(numbers[0], numbers[1])
    print_result(numbers[0], numbers[1], sum)


if __name__ == "__main__":
    main()
