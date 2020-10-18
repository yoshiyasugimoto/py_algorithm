# クイックソートの実装
def quick_sort(lis: list):
    if not lis:
        return lis
    p = lis[-1]
    left = []
    right = []
    pivots = []
    for v in lis:
        if v < p:
            left.append(v)
        elif v == p:
            pivots.append(v)
        else:
            right.append(v)
    return quick_sort(left) + pivots + quick_sort(right)
