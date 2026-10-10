def second_largest(nums: list[int]) -> int:
    distinct = sorted(set(nums), reverse=True)
    if len(distinct) < 2:
        raise ValueError("need at least two distinct values")
    return distinct[1]


def unique_in_order(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def word_frequency(sentence: str) -> dict[str, int]:
    counts = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def invert_dict(d: dict) -> dict:
    return {value: key for key, value in d.items()}


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    groups = {}
    for word in words:
        groups.setdefault(len(word), []).append(word)
    return groups


def common_elements(a: list, b: list) -> list:
    return sorted(set(a) & set(b))
