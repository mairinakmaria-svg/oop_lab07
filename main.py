from rational import Rational, RationalError, RationalValueError
from rational_list import RationalList


def read_rationals(filename):
    result = RationalList()
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            parts = line.split("/")
            try:
                if len(parts) == 1:
                    value = Rational(int(parts[0]))
                elif len(parts) == 2:
                    value = Rational(int(parts[0]), int(parts[1]))
                else:
                    raise RationalValueError(line, "reading from file")

                result.append(value)

            except RationalError as error:
                print(f"RationalError in file {filename}: {error}")
            except RationalValueError as error:
                print(f"RationalValueError in file {filename}: {error}")
            except ValueError:
                print(f"RationalValueError in file {filename}: invalid text value {line}")

    return result


def task_731():
    print("Task 7.3.1")
    print("Trying to create Rational(5, 0)")
    try:
        number = Rational(5, 0)
        print(number)
    except RationalError as error:
        print("Caught exception:", error)


def task_732():
    print("\nTask 7.3.2")
    a = Rational(1, 2)
    print("Correct rational number:", a)

    try:
        print("Trying to add incorrect value: Rational(1, 2) + 'abc'")
        result = a + "abc"
        print(result)
    except RationalValueError as error:
        print("Caught exception:", error)

    try:
        print("Trying to divide by zero rational number: Rational(1, 2) / Rational(0, 3)")
        result = a / Rational(0, 3)
        print(result)
    except RationalValueError as error:
        print("Caught exception:", error)


def task_733():
    print("\nTask 7.3.3")
    filename = "test_data/rationals.txt"
    numbers = read_rationals(filename)
    print("Values from file:", numbers)
    print("Sum:", numbers.sum())

    print("Trying to add incorrect data to RationalList")
    try:
        numbers.append("not rational")
    except RationalValueError as error:
        print("Caught exception:", error)


if __name__ == "__main__":
    task_731()
    task_732()
    task_733()
