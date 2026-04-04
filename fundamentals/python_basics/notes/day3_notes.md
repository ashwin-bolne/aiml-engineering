# 📅 DAY 3 — FUNCTIONS + MODULAR THINKING

---

# 🎯 CORE OBJECTIVE

> Learn how to design **clean, reusable, testable functions** and combine them into a **system (pipeline)**.

---

# 🧠 1. FUNCTION DESIGN

---

## 🔹 Definition

A function is:

> A unit of logic with **clear input → processing → output**

---

## 🔥 Golden Rule

> “A function should do ONE thing and do it well” (SRP)

---

## 🔹 Good vs Bad

### ❌ Bad

* Multiple responsibilities
* Hidden dependencies
* Prints instead of returns

### ✅ Good

* Clear purpose
* Returns value
* Independent

---

## 🔹 Function Checklist

Before writing any function:

* What is input?
* What is output?
* What is responsibility?
* Any side effects?

---

# 🧠 2. REUSABILITY

---

## 🔹 Definition

> A reusable function works in **multiple contexts without modification**

---

## 🔹 Key Principles

### 1. Generalization

Avoid hardcoding

### 2. Parameterization

Make behavior configurable

### 3. No side effects

Don’t modify external state

### 4. Return, don’t print

---

## 🔹 Example

```python
def count_char(text, ch):
    return text.count(ch)
```

---

# 🧠 3. VALIDATION

---

## 🔹 Why?

* Prevent invalid inputs
* Fail early
* Avoid hidden bugs

---

## 🔹 Pattern

```python
def validate_input(data, expected_type):
```

---

## 🔹 Types of validation

* Type check (`isinstance`)
* Null check (`None`)
* Empty check (`len == 0`)

---

# 🧠 4. MODULAR THINKING

---

## 🔹 Definition

> Break system into independent modules

---

## 🔹 Example Pipeline

```text
Input → Clean → Tokenize → Analyze → Output
```

---

## 🔹 Benefits

* Reusability
* Testability
* Maintainability

---

# 🧠 5. PIPELINE DESIGN

---

## 🔹 Data Flow

| Stage    | Data Type |
| -------- | --------- |
| Input    | str       |
| Clean    | str       |
| Tokenize | list[str] |
| Analyze  | dict/int  |
| Output   | str       |

---

## 🔹 Rule

> Each function transforms data

---

# 🧠 6. CLEAN TEXT (NLP FOUNDATION)

---

## Steps:

1. Lowercase
2. Remove punctuation
3. Normalize spaces

---

# 🧠 7. TOKENIZATION

---

## Definition

> Splitting text into words

---

## Rule

* No cleaning here
* Only splitting

---

# 🧠 8. ANALYSIS PATTERNS

---

## count_words → len(list)

## unique_words → set()

## frequency → hashmap

---

# 🧠 9. SORTING (IMPORTANT)

---

```python
sorted(freq.items(), key=lambda x: x[1], reverse=True)
```

---

## Concepts:

* sorted()
* key function
* lambda
* tuple indexing

---

# 🧠 10. MAIN GUARD

---

```python
if __name__ == "__main__":
```

---

## Purpose:

> Prevent auto execution when imported

---

# 🧠 11. MODULE SYSTEM

---

## Import

```python
from utils.data_structures import frequency_counter
```

---

## Important:

* Run from root
* Use `python -m`

---

# 🧠 12. SYSTEM THINKING

---

You built:

* CLI tool
* Processing pipeline
* Modular architecture

---

# 🎯 INTERVIEW SUMMARY

> “Day 3 focuses on writing clean, reusable functions and composing them into a modular pipeline-based system.”
