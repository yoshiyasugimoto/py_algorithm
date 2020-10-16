def merge_lis(left: list, right: list) -> list:
    res = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res + left[i:] + right[j:]


if __name__ == '__main__':
    left = [12, 1234]
    right = [21, 41]
    print(merge_lis(left, right))
