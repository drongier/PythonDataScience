from typing import Any


def all_thing_is_obj(object: Any) -> int:
    """Identify the container or string type of object and print it.

    Prints a label with the object's type for list, tuple, set, dict and
    str. Any other type falls through to "Type not found". Always
    returns 42.
    """
    if isinstance(object, list):
        print(f"List : {type(object)}")
    elif isinstance(object, tuple):
        print(f"Tuple : {type(object)}")
    elif isinstance(object, set):
        print(f"Set : {type(object)}")
    elif isinstance(object, dict):
        print(f"Dict : {type(object)}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
    return 42
