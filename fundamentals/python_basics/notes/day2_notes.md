# 📅 DAY 2 — DATA STRUCTURES (INTERVIEW-READY NOTES)

---

# 🎯 CORE OBJECTIVE

Understand **how data structures behave internally** and **when to use which**, not just syntax.

---

# 🧠 1. LIST (Dynamic Array)

## 🔹 Definition

A list is a **dynamic array** that stores elements in contiguous memory and allows index-based access.

---

## 🔹 Internal Working

* Backed by an array
* Python allocates **extra capacity**
* When full → resize + copy

👉 This leads to:

* Append → **Amortized O(1)**
* Insert/Delete (middle) → **O(n)** (due to shifting)

---

## 🔹 Time Complexity

| Operation              | Complexity |
| ---------------------- | ---------- |
| Access (arr[i])        | O(1)       |
| Append                 | O(1)*      |
| Insert/Delete (middle) | O(n)       |
| Search                 | O(n)       |

---

## 🔹 Key Insight (Interview)

> “List is fast for indexing but slow for rearrangement.”

---

## 🔹 When to Use

* Sequential data
* Sliding window problems
* Two-pointer problems

---

## 🔹 When NOT to Use

* Frequent insert/delete in middle
* Frequent membership checks (`x in arr`)

---

## 🔹 Common Mistake

```python
if x in arr  # O(n)
```

✔ Use set/dict instead

---

## 🔹 Edge Cases

* Negative indexing (`arr[-1]`)
* Copy vs reference:

```python
b = a       # same memory
b = a.copy()  # new memory
```

---

# 🧠 2. DICT (HashMap)

## 🔹 Definition

A dict is a **hash table** that stores key-value pairs and provides **O(1) average lookup**.

---

## 🔹 Internal Working

1. Key → hash function
2. Hash → index
3. Store at index

---

## 🔹 Collision Handling

* Multiple keys → same index
* Python uses **open addressing (probing)**

---

## 🔹 Time Complexity

| Operation  | Complexity |
| ---------- | ---------- |
| Insert     | O(1) avg   |
| Lookup     | O(1) avg   |
| Delete     | O(1) avg   |
| Worst case | O(n)       |

---

## 🔹 Key Insight (Interview)

> “Dict achieves O(1) using hashing, but performance depends on good hash distribution.”

---

## 🔹 Immutable Keys (IMPORTANT)

Allowed:

* int, str, tuple

Not allowed:

* list, dict

👉 Because hash must not change

---

## 🔹 Common Pattern — Frequency Counter

```python
freq[x] = freq.get(x, 0) + 1
```

---

## 🔹 When to Use

* Fast lookup
* Counting
* Caching
* Mapping

---

## 🔹 When NOT to Use

* Ordered operations (logic dependent on position)

---

## 🔹 Edge Case

* KeyError → use `.get()` or `defaultdict`

---

# 🧠 3. SET

## 🔹 Definition

A set is a **hash-based collection of unique elements**.

---

## 🔹 Internal Working

* Same as dict (only keys, no values)

---

## 🔹 Time Complexity

| Operation | Complexity |
| --------- | ---------- |
| Add       | O(1)       |
| Remove    | O(1)       |
| Lookup    | O(1)       |

---

## 🔹 Key Insight (Interview)

> “Set is optimized for membership checks and uniqueness.”

---

## 🔹 Use Cases

* Duplicate detection
* Membership checking
* Intersection / union

---

## 🔹 Example

```python
if x in seen:  # O(1)
```

---

## 🔹 Set Operations

| Operation    | Syntax |
| ------------ | ------ |
| Union        | A | B  |
| Intersection | A & B  |
| Difference   | A - B  |

---

## 🔹 When NOT to Use

* When order matters
* When indexing needed

---

# 🧠 4. TUPLE

## 🔹 Definition

A tuple is an **immutable ordered collection**.

---

## 🔹 Key Properties

* Immutable
* Hashable (if elements immutable)
* Faster than list

---

## 🔹 Key Insight (Interview)

> “Tuple is used for fixed, structured data and as dict keys.”

---

## 🔹 Use Cases

* Dict keys
* Returning multiple values
* Heap elements

---

## 🔹 Important Edge Case

```python
t = ([1,2], 3)
t[0].append(99)
```

👉 Tuple immutable, but inner list mutable

---

## 🔹 Special Syntax

```python
(1,)  # single element tuple
```

---

# 🔥 PATTERNS (MOST IMPORTANT PART)

---

## 🔹 Pattern 1 — Frequency Counting

Used in:

* Valid Anagram
* Top K Elements

```python
freq[x] = freq.get(x, 0) + 1
```

---

## 🔹 Pattern 2 — Membership Check

Used in:

* Contains Duplicate

```python
seen = set()
```

---

## 🔹 Pattern 3 — Top K Elements

* Dict → count
* Heap → extract top k

---

# ⚠️ COMMON INTERVIEW PITFALLS

---

## ❌ Using list for lookup

→ O(n)

✔ Use set/dict → O(1)

---

## ❌ Sorting when not needed

→ O(n log n)

✔ Use heap or hashmap → O(n)

---

## ❌ Mutable keys in dict/set

→ error or undefined behavior

---

# 🧠 HOW TO ANSWER IN INTERVIEW

---

## Q: Why dict is O(1)?

👉 “Because it uses hashing to map keys to indices, avoiding traversal.”

---

## Q: Why set is faster than list?

👉 “Set uses hashing (O(1)), list requires linear scan (O(n)).”

---

## Q: Why tuple can be dict key?

👉 “Because it is immutable and hashable.”

---

## Q: Why insert in list is O(n)?

👉 “Because elements need to be shifted.”

---

# 🚀 FINAL SUMMARY

| Structure | Strength            | Weakness           |
| --------- | ------------------- | ------------------ |
| List      | Index access        | Slow insert/delete |
| Dict      | Fast lookup         | Collision risk     |
| Set       | Fast membership     | No order           |
| Tuple     | Immutable, hashable | No modification    |

---

# 🎯 FINAL INTERVIEW LINE

> “Choice of data structure depends on operation — lookup → dict/set, ordered access → list, fixed structure → tuple.”
