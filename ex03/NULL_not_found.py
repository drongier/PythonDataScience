from typing import Any


def NULL_not_found(object: Any) -> int:
    """Identify null-like values and print their label, value and type.

    Recognises None, NaN, 0, the empty string and False. Returns 0
    when the value is recognised, 1 otherwise.
    """
    # None first: identity check, only None is None
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    # NaN: the only float that is not equal to itself
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    # bool before int: bool is a subclass of int
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
        return 0
    # int after bool, so a real 0 lands here
    elif isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
        return 0
    # empty string only, "Brian" must not match
    elif isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0
    # not a null-like value
    else:
        print("Type not Found")
        return 1


def main() -> None:
    """Run the program: nothing to do, the script is a library."""
    return None


if __name__ == "__main__":
    main()
