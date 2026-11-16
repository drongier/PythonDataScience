import sys


def filter_words(texte: str, n: int) -> list[str]:
    """Return the words of text longer than n."""
    return [word for word in filter(lambda word: len(word) > n, texte.split())]


def main() -> int:
    """ Print the words of S longer than N """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad") from None
        words = filter_words(sys.argv[1], number)
        print(words)
        return 0

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
