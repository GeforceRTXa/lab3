from random import randint
from math import ceil

def comp_checker(comp):
    """
    Функция, проверяющая вывод компаратора. Если он некорректен, вызывается ошибка
    """
    if comp not in [-1, 0, 1]:
        raise ValueError("Incorrect comparator value")


def default_comp(a, b):
    """
    Стандартный компаратор для сортировок. Применяется для сортировки по возрастанию
    """
    if a > b:
        return 1
    if a == b:
        return 0
    return -1

def bubble_sort(a: list, comp=default_comp, flag=lambda x: x):
    """
    Пузырьковая сортировка
    :param a: список на вход
    :param comp: компаратор
    :param flag: флаг
    :return: отсортированный список
    """
    unsorted = True
    nums = a
    while unsorted:
        unsorted = False
        for i in range(len(nums) - 1):
            try:
                expr = comp(flag(nums[i]), flag(nums[i + 1]))
            except:
                raise
            comp_checker(expr)
            if expr == 0:
                continue
            if expr == 1:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                unsorted = True
    return nums

def quick_sort(a: list, comp=default_comp, flag=lambda x: x):
    """
    Быстрая сортировка
    :param a: список на вход
    :param comp: компаратор
    :param flag: флаг
    :return: отсортированный список
    """
    nums = a
    if len(nums) <= 1:
        return nums
    pivot = nums.pop(randint(0, len(nums) - 1))
    left = []
    right = []
    for num in nums:
        try:
            expr = comp(flag(pivot), flag(num))
        except:
            raise ValueError("Incorrect flag or comparator for your list")
        comp_checker(expr)
        if expr == 1 or expr == 0:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left, comp=comp, flag=flag) + [pivot] + quick_sort(right, comp=comp, flag=flag)

def counting_sort(a: list[int]):
    """
    Сортировка подсчетом
    :param a: список на вход
    :return: отсортированный список
    """
    for i in a:
        if type(i) is not int:
            raise Exception("Incorrect list for sorting")
        if i < 0:
            raise Exception("Numbers must be positive or null")
    nums = a
    counter = [0] * (max(a) + 1)
    for num in nums:
        counter[num] += 1
    result = []
    for i in range(len(counter)):
        result += [i] * counter[i]
    return result

def radix_sort(a: list[int], base: int):
    """
    Поразрядная сортировка
    :param a: список на вход
    :param base: Основание системы счисления
    :return: отсортированный список
    """
    if type(base) is not int or base <= 1:
        raise Exception("Incorrect base")
    for i in a:
        if type(i) is not int:
            raise Exception("Incorrect list for sorting")
        if i < 0:
            raise Exception("Numbers must be positive or null")
    nums = a
    max_digits = 0
    max_num = max(nums)
    while max_num != 0:
        max_digits += 1
        max_num //= base
    for i in range(max_digits):
        digits_sorting = [[] for _ in range(base)]
        for num in nums:
            current_digit = (num // (base ** i)) % base
            digits_sorting[current_digit].append(num)
        nums = []
        for number_with_digit in digits_sorting:
            for num in number_with_digit:
                nums.append(num)
    return nums

def bucket_sort(a, buckets_count=None, comp=default_comp, flag=lambda x: x):
    """
    Блочная сортировка
    :param a: список на вход
    :param comp: компаратор
    :param flag: флаг
    :return: отсортированный список
    """
    if buckets_count is not None:
        if type(buckets_count) is not int or buckets_count <= 0:
            raise Exception("Incorrect buckets count")
    if buckets_count is None:
        nums = a
        min_num = flag(min(map(lambda x: flag(x), nums), key=flag))
        max_num = flag(max(map(lambda x: flag(x), nums), key=flag))
        if type(min_num) not in (int, float) or type(max_num) not in (int, float):
            raise ValueError("Flag should return int or float")
        buckets_containers = [[] for _ in range(ceil(max_num) - int(min_num) + 4)]
        for num in nums:
            for i in range(ceil(max_num) - int(min_num) + 4):
                r = [i + int(min_num), i + 1 + int(min_num)]
                if r[0] <= flag(num) < r[1]:
                    buckets_containers[i].append(num)
                    break
    else:
        nums = a
        min_num = min(map(lambda x: flag(x), nums))
        max_num = max(map(lambda x: flag(x), nums))
        buckets_containers = [[] for _ in range(buckets_count)]
        for num in nums:
            for i in range(buckets_count):
                r = [(min_num + i * (max_num - min_num) // buckets_count), (min_num + (i + 1) * (max_num - min_num) // buckets_count)]
                if r[0] <= flag(num) <= r[1]:
                    buckets_containers[i].append(num)
                    break
    result = []
    for bucket in buckets_containers:
        result += quick_sort(bucket, comp=comp, flag=flag)
    return result

def heap(arr, n, i, flag, comp):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        try:
            comp_l = comp(flag(arr[left]), flag(arr[root]))
        except:
            raise ValueError("Incorrect flag or comparator for your list")
        comp_checker(comp_l)
        if comp_l == 1:
            root = left
    if right < n:
        try:
            comp_l = comp(flag(arr[right]), flag(arr[root]))
        except:
            raise ValueError("Incorrect flag or comparator for your list")
        comp_checker(comp_l)
        if comp_l == 1:
            root = right
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heap(arr, n, root, flag, comp)

def heap_sort(arr: list, flag=lambda x: x, comp=default_comp):
    """
    Сортировка кучами
    :param arr: Список на вход
    :param flag: флаг
    :param comp: компаратор
    :return: отсортированный список
    """
    nums = arr
    n = len(nums)

    for i in range(n // 2 -1, -1, -1):
        heap(nums, n, i, flag, comp)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heap(nums, i, 0, flag, comp)
    return nums
