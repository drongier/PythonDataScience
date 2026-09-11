import string
import sys


def count_characters(text: str) -> None:
    """Print the number of characters of text, grouped by category.

    Categories: upper letters, lower letters, punctuation marks,
    spaces and digits.
    """
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif char in string.punctuation:
            punctuation += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def get_text() -> str:
    """Return the text to analyse.

    Use the single command line argument when provided, otherwise
    prompt the user on standard input.
    """
    if len(sys.argv) == 2:
        return sys.argv[1]
    print("What is the text to count?")
    return sys.stdin.readline()


def main() -> int:
    """Run the character counter program.

    Return 0 on success, 1 when too many arguments are provided.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        text = get_text()
        count_characters(text)
        return 0
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
