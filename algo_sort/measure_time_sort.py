# ソートの時間を計測する
import time
from typing import List

from merging_two_sorted_arrays import recursive_for_merge_sort

from quick_sort import quick_sort


def measure_time_sort(sort_func, sample_data: List[list], num: int = 3):
    s = time.time()
    for _ in range(num):
        for lis in sample_data:
            sort_func(lis)
    e = time.time()
    return e - s


if __name__ == '__main__':
    import random

    sample_data = []
    for _ in range(100):
        sample_data.append([random.randint(0, 5000) for num in range(2000)])

    print(f"Merge sort performance measurements:\n{measure_time_sort(recursive_for_merge_sort, sample_data)}")
    print(f"Quick sort performance measurements:\n{measure_time_sort(quick_sort, sample_data)}")
