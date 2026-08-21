import time
from datetime import datetime


def main():
    timestamp = time.time()
    now = datetime.now()

    formatted_seconds = f"{timestamp:,.4f}"
    scientific_notation = f"{timestamp:.2e}"

    print(
        f"Seconds since January 1, 1970: {formatted_seconds} "
        f"or {scientific_notation} in scientific notation"
    )
    print(now.strftime("%b %d %Y"))

if __name__ == "__main__":
    main()