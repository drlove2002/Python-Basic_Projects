def is_leap_year(year) -> bool:
    if (not (year % 4) and (year % 100)) or not (year % 400):
        return True
    else:
        return False


def main() -> None:
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()
