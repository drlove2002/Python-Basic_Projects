import math


def get_roots(a: int, b: int, c: int):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None, None
    if discriminant == 0:
        return -b / (2 * a), None

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x1, x2


def main() -> None:
    print("ax2 + bx + c = 0 where a, b, c, ∈ R and a ≠ 0.")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if a == 0:
        raise ValueError("a must not be zero.")

    x1, x2 = get_roots(a, b, c)
    if x1 == x2 == None:
        print("The quadratic equation has no real solutions")
    elif x2 is None:
        print(f"The quadratic equation has one real solution: {x1:.2f}")
    else:
        print(f"The quadratic equation has two real solutions: {x1:.2f}, {x2:.2f}")


if __name__ == "__main__":
    main()
