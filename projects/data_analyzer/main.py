from typing import Any
from utils.data_structures import frequency_counter


def validate_input(data: Any, expected_type: type) -> None:
    """Validate input type and ensure it is not empty."""
    if data is None:
        raise ValueError("Input cannot be None")

    if not isinstance(data, expected_type):
        raise TypeError(f"Expected {expected_type}, got {type(data)}")

    if hasattr(data, "__len__") and len(data) == 0:
        raise ValueError("Input cannot be empty")


def clean_text(text: str) -> str:
    """Normalize text: lowercase, remove punctuation, normalize spaces."""
    validate_input(text, str)

    text = text.lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch.isspace())
    text = " ".join(text.split())

    return text


def tokenize(text: str) -> list[str]:
    """Split cleaned text into tokens."""
    validate_input(text, str)
    return text.split()


def count_words(tokens: list[str]) -> int:
    """Return total number of words."""
    validate_input(tokens, list)
    return len(tokens)


def count_unique_words(tokens: list[str]) -> int:
    """Return number of unique words."""
    validate_input(tokens, list)
    return len(set(tokens))


def get_frequency(tokens: list[str]) -> dict[str, int]:
    """Return frequency of each word."""
    validate_input(tokens, list)
    return frequency_counter(tokens)


def format_output(total_words: int, unique_words: int, frequency: dict[str, int]) -> str:
    """Format analysis results into readable string."""
    lines = [
        f"Total words: {total_words}",
        f"Unique words: {unique_words}",
        "Frequency:"
    ]

    for word, count in sorted(frequency.items(), key=lambda x: -x[1]):
        lines.append(f"{word} -> {count}")

    return "\n".join(lines)


def main():
    text = input("Enter text: ")

    cleaned = clean_text(text)
    tokens = tokenize(cleaned)

    total = count_words(tokens)
    unique = count_unique_words(tokens)
    freq = get_frequency(tokens)

    output = format_output(total, unique, freq)

    print("\n--- Analysis ---")
    print(output)


if __name__ == "__main__":
    main()