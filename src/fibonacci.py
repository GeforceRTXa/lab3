def fibo_recursive(n: int) -> int:
    """
    Вычисление n-ого числа Фибоначчи рекурсивно
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

def fibo(n : int) -> int:
    """
    Вычисление n-ого числа Фибоначчи циклом
    """
    values = [0, 1]
    for i in range(2, n + 1):
        values.append(values[i - 1] + values[i - 2])
    return values[n]