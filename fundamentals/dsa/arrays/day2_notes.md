# 📅 DAY 2 — DSA NOTES (INTERVIEW READY)

---

# 🔹 1. VALID ANAGRAM

## 🎯 Problem

Check if two strings are anagrams (same characters, same frequency).

---

## 🧠 Core Pattern

👉 **Frequency Matching (HashMap)**

---

## 💡 Key Idea

Instead of sorting:

* Count characters in `s`
* Decrement using `t`
* If any mismatch → not anagram

---

## ⚙️ Optimal Approach

```python
def isAnagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True
```

---

## ⏱ Complexity

* Time: **O(n)**
* Space: **O(1)** (fixed alphabet)

---

## ⚠️ Edge Cases

* Different lengths
* Extra characters
* Missing characters

---

## ❌ Common Mistakes

* Using sorting → O(n log n)
* Not handling missing keys
* Not checking negative count

---

## 🎤 Interview Line

> “This is a frequency comparison problem using hashmap in O(n) time.”

---

---

# 🔹 2. CONTAINS DUPLICATE

## 🎯 Problem

Check if any element appears more than once.

---

## 🧠 Core Pattern

👉 **Membership Check (Set)**

---

## 💡 Key Idea

Track seen elements:

* If seen before → duplicate

---

## ⚙️ Optimal Approach

```python
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
```

---

## ⏱ Complexity

* Time: **O(n)**
* Space: **O(n)**

---

## ⚠️ Edge Cases

* Empty list
* All unique
* All same elements

---

## ❌ Common Mistakes

* Using list for lookup → O(n²)
* Using dict unnecessarily

---

## 🎤 Interview Line

> “Since we only need existence, set is optimal over hashmap.”

---

---

# 🔹 3. TWO SUM

## 🎯 Problem

Find indices of two numbers such that:

```
nums[i] + nums[j] = target
```

---

## 🧠 Core Pattern

👉 **HashMap Lookup (Complement Search)**

---

## 💡 Key Idea

For each number:

```
complement = target - num
```

Check if complement already exists.

---

## ⚙️ Optimal Approach

```python
def twoSum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i
```

---

## ⏱ Complexity

* Time: **O(n)**
* Space: **O(n)**

---

## ⚠️ Edge Cases

* Duplicate values
* Negative numbers
* Only one valid answer

---

## ❌ Common Mistakes

* Inserting before checking
* Using sorting (loses indices)
* Using list for lookup

---

## 🎤 Interview Line

> “We use hashmap to store seen values and check complement in O(1), achieving O(n) time.”

---

---

# 🔥 PATTERN SUMMARY (MOST IMPORTANT)

| Problem            | Pattern            | Data Structure |
| ------------------ | ------------------ | -------------- |
| Valid Anagram      | Frequency Matching | Dict           |
| Contains Duplicate | Membership Check   | Set            |
| Two Sum            | Complement Lookup  | Dict           |

---

# 🧠 DECISION FRAMEWORK (INTERVIEW GOLD)

---

## 🔹 When to use DICT

* Need frequency
* Need mapping
* Need complement lookup

---

## 🔹 When to use SET

* Only existence matters
* Need fast membership check

---

## 🔹 When NOT to use LIST

* When lookup required (O(n))

---

# 🚀 FINAL INTERVIEW SUMMARY

> “These problems are not about coding, they are about identifying patterns:
> frequency → dict,
> membership → set,
> complement → dict lookup.”

---

# 🎯 YOUR LEVEL AFTER DAY 2

You can now:

* Identify correct data structure instantly
* Optimize brute force → O(n)
* Explain reasoning clearly

👉 This is **real DSA foundation**
