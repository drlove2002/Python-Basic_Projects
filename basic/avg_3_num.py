from add_2_num import get_numbers


def average(x: int, y: int, z: int) -> float:
    return (x + y + z) / 3


def print_result(n: tuple, result: float) -> None:
    print(f"The average of {n[0]}, {n[1]} and {n[2]} is {result:.2f}")


def main() -> None:
    numbers = get_numbers(3)
    avg = average(numbers[0], numbers[1], numbers[2])
    print_result(numbers, avg)


if __name__ == "__main__":
    main()
