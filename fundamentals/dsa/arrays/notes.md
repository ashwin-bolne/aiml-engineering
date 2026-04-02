# Arrays — DSA Notes

---

## 🔹 Problem 1: Two Sum

### Pattern:
Hashing / Lookup Optimization

### Approach:
- Use hashmap (dictionary)
- Store: number → index
- For each element:
  - required = target - current
  - check if required exists

### Complexity:
- Time: O(n)
- Space: O(n)

### Key Insight:
Using hashmap avoids nested loops and reduces time complexity from O(n²) → O(n)

### Common Mistake:
- Inserting into hashmap before checking

---

## 🔹 Problem 2: Best Time to Buy & Sell Stock

### Pattern:
Greedy / Tracking Minimum

### Approach:
- Track minimum price so far
- At each step:
  - calculate profit = current_price - min_price
  - update max profit

### Complexity:
- Time: O(n)
- Space: O(1)

### Key Insight:
Local optimal choice (minimum price so far) leads to global optimal result

### Important Concept:
Greedy Algorithm → Making best choice at each step

### Common Mistake:
- Trying all pairs (O(n²))
- Using max-min without order constraint