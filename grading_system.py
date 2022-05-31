def get_grade(percentage: float) -> str:
    grades = ("A+", "A", "B+", "B", "C+", "C")
    if percentage < 40:
        return "D"
    else:
        return grades[-1 * (int(percentage / 10) - 3)]


def get_performance(percentage: float) -> str:
    performance_table = {
        "A+": "Outstanding",
        "A": "Excellent",
        "B+": "Good",
        "B": "Satisfactory",
        "C+": "Fair",
        "C": "Poor",
        "D": "Fail",
    }
    return performance_table[get_grade(percentage)]


def get_percentage(marks: int, total: int) -> float:
    return round((marks / total) * 100, 2)


def main() -> None:
    marks = int(input("Enter the subject marks: "))
    total = int(input("Enter total marks: "))
    percentage = get_percentage(marks, total)
    print(
        f"Percentage: {percentage}%\n"
        f"Grade: {get_grade(percentage)}\n"
        f"Performance: {get_performance(percentage)}"
    )


if __name__ == "__main__":
    main()
