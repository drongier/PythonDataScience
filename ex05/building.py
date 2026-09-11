import sys
import string

def main() -> int:
    if len(sys.argv) < 2:
        return 0
    assert len(sys.argv) == 2, "more than one argument is provided"

print("What is the text to count?")
text = sys.stdin.readline()

print(f"The text contains {len(text)} characters:")

upper_count = 0
for c in text:
    if c.isupper():
        upper_count += 1
print(f"{upper_count} upper letters")

lower_count = 0
for c in text:
    if c.islower():
        lower_count += 1
print(f"{lower_count} lower letters")

punctuation_count = 0
for c in text:
    if c in string.punctuation:
        punctuation_count += 1
print(f"{punctuation_count} punctuation marks")

space_count = 0
for c in text:
    if c.isspace():
        space_count += 1
print(f"{space_count} spaces")

digit_count = 0
for c in text:
    if c.isdigit():
        digit_count += 1
print(f"{digit_count} digits")


if __name__ == "__main__":
    sys.exit(main())