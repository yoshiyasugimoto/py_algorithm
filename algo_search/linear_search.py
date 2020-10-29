def linear_search(lis, target):
    for v in lis:
        if target == v:
            return True
    return False


if __name__ == '__main__':
    import random

    random.seed(1)
    my_lis = [random.randint(0, 100) for i in range(15)]
    print(linear_search(my_lis, 32))
