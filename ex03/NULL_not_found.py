from typing import Any

def NULL_not_found(object: Any) -> int:
    # vérifier None d'abord (identité, pas égalité : seul None est None)
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return (0)
    # puis NaN (piège 1)
    elif isinstance(object, float):
        print(f"Cheese: {object} {type(object)}")
        return (0)
    # puis 0 mais uniquement si c'est un vrai int, pas un bool (piège 2)
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
        return (0)
    # puis False (le dernier, après 0)
    elif isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
        return (0)
    # puis ""
    elif isinstance(object, str):
        print(f"Empty: {object} {type(object)}")
        return (0)
    # sinon : print("Type not Found") et return 1
    else:
        print("Type not Found")
        return (1)
