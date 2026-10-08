import sys

NESTED_MORSE = {
    " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ",
    "D": "-.. ", "E": ". ", "F": "..-. ", "G": "--. ", 
    "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ",
    "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
    "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ",
    "X": "-..- ", "Y": "-.-- ", "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ",
}


def transform_to_morse(texte: str) -> str:
    return "".join(NESTED_MORSE[c] for c in texte.upper()).strip()

def main() -> int:
    """Encode an alphanumeric string into Morse code."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        texte = sys.argv[1]
        for c in texte.upper():
            if c not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
        morse = transform_to_morse(texte)
        print(morse)
        return 0
    except AssertionError as error:
        print(f"AssertionError: {error}")   
        return 1


if __name__ == "__main__":
    sys.exit(main())