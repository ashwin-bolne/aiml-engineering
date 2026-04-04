from typing import List, Dict, Any, Tuple
import heapq


def frequency_counter(arr: List[Any]) -> Dict[Any, int]:
    """
    Counts frequency of elements.

    Time: O(n)
    Space: O(n)
    """
    freq: Dict[Any, int] = {}

    for item in arr:
        # 핵심: safe increment without KeyError
        freq[item] = freq.get(item, 0) + 1

    return freq


def top_k_elements(arr: List[Any], k: int) -> List[Tuple[Any, int]]:
    """
    Returns top k frequent elements using min-heap.

    Time: O(n log k)
    Space: O(n)
    """

    if k <= 0:
        return []

    freq = frequency_counter(arr)

    # (count, element) → min-heap based on count
    heap: List[Tuple[int, Any]] = []

    for element, count in freq.items():
        heapq.heappush(heap, (count, element))

        # Keep heap size <= k
        if len(heap) > k:
            heapq.heappop(heap)

    # Convert to (element, count) and sort descending
    result = [(element, count) for count, element in heap]
    return sorted(result, key=lambda x: -x[1])


def lookup_map(keys: List[Any], values: List[Any]) -> Dict[Any, Any]:
    """
    Safely creates a mapping from keys to values.

    Raises:
        ValueError if lengths mismatch
    """

    if len(keys) != len(values):
        raise ValueError("Keys and values must have same length")

    return {k: v for k, v in zip(keys, values)}