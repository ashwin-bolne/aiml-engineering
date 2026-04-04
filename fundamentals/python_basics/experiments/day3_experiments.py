# experiments_day3.py

# 🔹 1. validate_input testing
from typing import Any

def validate_input(data: Any, expected_type: type) -> None:
    if data is None:
        raise ValueError("Input cannot be None")
    if not isinstance(data, expected_type):
        raise TypeError(f"Expected {expected_type}")
    if hasattr(data, "__len__") and len(data) == 0:
        raise ValueError("Input cannot be empty")


# 🔹 2. clean_text experiments
def clean_text(text: str) -> str:
    text = text.lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch.isspace())
    text = " ".join(text.split())
    return text


print("---- clean_text ----")
print(clean_text("Hello!!!   World??"))
print(clean_text("  PYTHON   is   GREAT  "))


# 🔹 3. tokenize experiments
def tokenize(text: str) -> list[str]:
    return text.split()


print("\n---- tokenize ----")
print(tokenize("hello world python"))


# 🔹 4. set behavior (unique words)
print("\n---- set (unique) ----")
tokens = ["hello", "world", "hello"]
print(set(tokens))


# 🔹 5. frequency sorting experiment
freq = {"hello": 2, "world": 1, "python": 3}

print("\n---- sorting ----")
print(sorted(freq.items(), key=lambda x: x[1]))          # ascending
print(sorted(freq.items(), key=lambda x: -x[1]))         # descending
print(sorted(freq.items(), key=lambda x: x[1], reverse=True))


# 🔹 6. join + split experiment
print("\n---- split & join ----")
text = "   hello   world   python   "
tokens = text.split()
print(tokens)
print(" ".join(tokens))


# 🔹 7. pipeline simulation
print("\n---- pipeline ----")
raw = "Hello!!!   world hello"
cleaned = clean_text(raw)
tokens = tokenize(cleaned)

print("Cleaned:", cleaned)
print("Tokens:", tokens)
print("Total:", len(tokens))
print("Unique:", len(set(tokens)))