#Method 1:
def merge_arr(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # To append any remaining elements
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1

    if j < m:
        while j < m:
            result.append(right[j])
            j += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    return merge_arr(left, right)


nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]

sorted_nums = merge_sort(nums)

print(sorted_nums)

# Method 2:
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # It's Pythonic shortcut instead of appending
    result.extend(left[i:])
    result.extend(right[j:])

    return result

nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]
print(merge_sort(nums))