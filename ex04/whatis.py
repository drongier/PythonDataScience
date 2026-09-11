import sys


def main() -> int:
    """Check whether the single integer argument is even or odd.

    Prints the result and returns 0 on success.
    Returns 1 on error (no conversion possible, or too many arguments).
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) < 2:
            return 0
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer") from None

        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
        return 0
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
