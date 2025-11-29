def factorial_recursive(n):
    """
    Вычисление факториала рекурсивно
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def factorial(n):
    """
    Вычисление факториала циклом
    """
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r