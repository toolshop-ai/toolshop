def merge_sort(l: list[int]):
    """Sort the list in ascending order using the merge sort algorithm."""
    if len(l) <= 1:
        return l
    else:
        half = len(l) // 2

        return merge(
            merge_sort(l[:half], l[half:])
        )

def merge(a: list[int], b):
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result
