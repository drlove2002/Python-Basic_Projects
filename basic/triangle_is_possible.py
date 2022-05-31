def get_sides(num_count: int) -> list[int]:
    numbers = list()
    for i in range(num_count):
        numbers.append(int(input(f"Enter side({i+1}): ")))
    return numbers


def can_draw_triangle(sides: list) -> bool:
    sides.sort()
    return sides[0] + sides[1] > sides[2]


def main() -> None:
    sides = get_sides(3)
    if can_draw_triangle(sides):
        print("Triangle can be drawn.")
    else:
        print("Triangle cannot be drawn.")


if __name__ == "__main__":
    main()
