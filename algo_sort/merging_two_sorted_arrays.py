import random


def merge_lis(left: list, right: list = []) -> list:
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


def step(row_lis: list) -> list:
    res = []
    for i in range(0, len(row_lis), 2):
        breakpoint()
        res.append(merge_lis(*row_lis[i:i + 2]))
    return res


if __name__ == '__main__':
    left = [12, 1234]
    right = [21, 41]
    print(merge_lis(left, right))

    random.seed(4)
    random_array = [random.randint(0, 100) for i in range(15)]
    print(random_array)
    my_array = [[v] for v in random_array]
    step1 = step(my_array)
    print(step1)
    step2 = step(step1)
    print(step2)
    step3 = step(step2)
    print(step3)
    step4 = step(step3)
    print(step4)


