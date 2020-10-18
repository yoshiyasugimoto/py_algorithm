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


if __name__ == '__main__':
    import random

    lis = [random.randint(0, 100) for i in range(15)]
    print(quick_sort(lis))
