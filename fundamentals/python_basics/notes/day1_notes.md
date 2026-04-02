# 📘 Day 1 — Python Fundamentals (Interview Notes)

---

## 🔹 1. Dynamic Typing

Python is **dynamically typed**, meaning variable types are determined at runtime.

```python
x = 10
x = "hello"
````

### 🧠 Key Points:

* No type declaration required
* Variable can change type

### 🎯 Interview Insight:

Python is **dynamically typed AND strongly typed**

```python
"2" + 2  # ❌ TypeError
```

---

## 🔹 2. Type Hints

Used for readability and better tooling support.

```python
def add(a: int, b: int) -> int:
    return a + b
```

### 🧠 Key Points:

* Not enforced at runtime
* Helps IDE and static analysis

### 🎯 Interview Question:

**Are type hints mandatory?**
→ ❌ No, but expected in production code

---

## 🔹 3. isinstance()

Used to check type safely.

```python
isinstance(5, int)  # True
```

### 🧠 Why not type()?

```python
type(x) == int  # ❌ not recommended
```

### ✅ Preferred:

```python
isinstance(x, int)
```

### 🎯 Reason:

Supports inheritance

---

## 🔹 4. TypeError vs ValueError

| Error      | Meaning                   |
| ---------- | ------------------------- |
| TypeError  | Wrong data type           |
| ValueError | Correct type, wrong value |

### Examples:

```python
"2" + 2          # TypeError
int("abc")       # ValueError
```

---

## 🔹 5. Functions

Functions allow reusable and modular code.

```python
def greet(name):
    return "Hello " + name
```

### 🎯 Key Concepts:

* Input → Process → Output
* Improves readability

---

## 🔹 6. return vs print

| return            | print           |
| ----------------- | --------------- |
| Gives output back | Displays output |
| Reusable          | Not reusable    |

---

## 🔹 7. Modulus Operator (%)

Used to get remainder.

```python
n % 2 == 0
```

### 🎯 Used for:

* Even/Odd checks
* Cyclic logic

---

## 🔹 8. Prime Number Optimization

Instead of checking till n:

```python
for i in range(2, int(n ** 0.5) + 1)
```

### 🧠 Why?

* Reduces complexity from O(n) → O(√n)

---

## 🔹 9. String Operations

```python
s.lower()
s.replace(" ", "")
s[::-1]
```

### 🎯 Key Use:

* Case normalization
* String reversal
* Cleaning input

---

## 🔹 10. Palindrome Logic

### Loop Approach:

```python
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        return False
```

### Pythonic Approach:

```python
s == s[::-1]
```

---

## 🔹 11. Vowel Counting Optimization

### ❌ Naive:

```python
if char in ["a", "e", ...]
```

### ✅ Better:

```python
vowels = set("aeiou")
```

→ O(1) lookup

---

## 🔹 12. Edge Case Handling

Always validate input:

```python
if not isinstance(x, int):
    raise TypeError(...)
```

### 🎯 Common Edge Cases:

* Invalid type
* Empty input
* Negative values

---

## 🔹 13. Clean Code Principles

* Use meaningful names (`number`, `string`)
* One function → one responsibility
* Avoid unnecessary complexity
* Keep functions reusable

---

## 🔹 14. Separation of Concerns

* `utils/` → logic only
* `experiments/` → testing

❌ No print statements inside utils

---

## 🔹 15. Complexity Awareness

Even simple problems should consider efficiency.

Example:

* Prime → O(√n)
* Vowel count → O(n)

---

