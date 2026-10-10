def squares_of_evens(nums: list[int]) -> list[int]:
    return [n * n for n in nums if n % 2 == 0]


def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}


def flatten(matrix: list[list]) -> list:
    return [item for row in matrix for item in row]


def transpose(matrix: list[list]) -> list[list]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def has_negative(nums: list[int]) -> bool:
    return any(n < 0 for n in nums)


def pairs_summing_to(nums: list[int], target: int) -> list[tuple[int, int]]:
    return [
        (nums[i], nums[j])
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
        if nums[i] + nums[j] == target
    ]
