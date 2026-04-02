def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers such that they add up to target.

    Uses a hashmap (dictionary) for O(n) time complexity.
    """
    num_map = {}

    for index, value in enumerate(nums):
        required = target - value

        if required in num_map:
            return [num_map[required], index]

        num_map[value] = index

    return []