import pytest

from src.sorts import bubble_sort, quick_sort, bucket_sort, radix_sort, counting_sort, heap_sort, default_comp


@pytest.mark.parametrize(
    "expr, ans", [([1, 3, 2, 6 , 5], [1, 2, 3, 5, 6]),
                    ([1, 1.1, 4, 3.2], [1, 1.1, 3.2, 4]),
                  ([1], [1]),
                  ([1, 1], [1, 1]),
                  ([3, 2, 1], [1, 2, 3]),
                      ([-3, 1, -2, 5], [-3, -2, 1, 5])]
)
def test_bubble_sort(expr, ans):
    assert bubble_sort(expr) == ans


@pytest.mark.parametrize(
    "expr, ans", [([1, 3, 2, 6 , 5], [1, 2, 3, 5, 6]),
                    ([1, 1.1, 4, 3.2], [1, 1.1, 3.2, 4]),
                  ([1], [1]),
                  ([1, 1], [1, 1]),
                  ([-3, 2, 1], [-3, 1, 2]),
                    ([-3, 1, -2, 5], [-3, -2, 1, 5])]
)
def test_quick_sort(expr, ans):
    assert quick_sort(expr) == ans

@pytest.mark.parametrize(
    "expr, ans", [([1, 3, 2, 6 , 5], [1, 2, 3, 5, 6]),
                    ([1, 1.1, 4, 3.2], [1, 1.1, 3.2, 4]),
                  ([1], [1]),
                  ([1, 1], [1, 1]),
                  ([-3, 2, 1], [-3, 1, 2])]
)
def test_bucket_sort_with_none(expr, ans):
    assert bucket_sort(expr) == ans

@pytest.mark.parametrize(
    "expr, ans", [([1, 3, 2, 6 , 5], [1, 2, 3, 5, 6]),
                    ([1, 1.1, 4, 3.2], [1, 1.1, 3.2, 4]),
                  ([1], [1]),
                  ([1, 1], [1, 1]),
                  ([-3, 2, 1], [-3, 1, 2])]
)
def test_bucket_sort(expr, ans):
    assert bucket_sort(expr, 2) == ans

@pytest.mark.parametrize(
    "expr, ans", [([1, 3, 2, 6 , 5], [1, 2, 3, 5, 6]),
                  ([1], [1]),
                  ([1, 1], [1, 1]),
                  ([3, 2, 1], [1, 2, 3])]
)
def test_radix_sort(expr, ans):
    assert radix_sort(expr, 2) == ans

@pytest.mark.parametrize(
    "expr, ans", [([1, 3, 2, 6 , 5], [1, 2, 3, 5, 6]),
                    ([1, 1.1, 4, 3.2], [1, 1.1, 3.2, 4]),
                  ([1], [1]),
                  ([1, 1], [1, 1]),
                  ([-3, 2, 1], [-3, 1, 2]),
                  ([-3.1, 2, -3, 1], [-3.1, -3, 1, 2])]
)
def test_heap_sort(expr, ans):
    assert heap_sort(expr) == ans

@pytest.mark.parametrize(
    "expr, ans", [([1, 3, 2, 6 , 5], [1, 2, 3, 5, 6]),
                  ([1], [1]),
                  ([1, 1], [1, 1]),
                  ([3, 2, 1], [1, 2, 3]),
                  ([1, 1000, 100], [1, 100, 1000])]
)
def test_counting_sort(expr, ans):
    assert counting_sort(expr) == ans

@pytest.mark.parametrize(
    "expr, ans, flag, comp", [(["c", "b", "a", "ab", "ba", "abc", "aaa", "abcd"], ["a", "b", "c", "ab", "ba", "aaa", "abc", "abcd"], lambda x: (len(x), x), default_comp)]
)
def test_quick_with_flag_and_comp(expr, ans, flag, comp):
    assert quick_sort(expr, flag=flag, comp=comp)

@pytest.mark.parametrize(
    "expr, ans, flag, comp", [(["c", "b", "a", "ab", "ba", "abc", "aaa", "abcd"], ["a", "b", "c", "ab", "ba", "aaa", "abc", "abcd"], lambda x: (len(x), x), default_comp),
                              (["c", "b", "a", "ab", "ba", "abc", "aaa", "abcd"], ["a", "b", "c", "ab", "ba", "aaa", "abc", "abcd"], lambda x: (-len(x), x), lambda x, y: -1 if x > y else 0 if x == y else 1)]
)
def test_bubble_with_flag_and_comp(expr, ans, flag, comp):
    assert bubble_sort(expr, flag=flag, comp=comp)

@pytest.mark.parametrize(
    "expr, ans, flag, comp", [(["c", "b", "a", "ab", "ba", "abc", "aaa", "abcd"], ["a", "b", "c", "ab", "ba", "aaa", "abc", "abcd"], lambda x: (len(x), x), default_comp),
                              (["c", "b", "a", "ab", "ba", "abc", "aaa", "abcd"], ["a", "b", "c", "ab", "ba", "aaa", "abc", "abcd"], lambda x: (-len(x), x), lambda x, y: -1 if x > y else 0 if x == y else 1)]
)
def test_heap_with_flag_and_comp(expr, ans, flag, comp):
    assert heap_sort(expr, flag=flag, comp=comp)

@pytest.mark.parametrize(
    "expr, ans, flag, comp", [(["c", "b", "a", "ab", "ba", "abc", "aaa", "abcd"], ["a", "b", "c", "ab", "ba", "aaa", "abc", "abcd"], lambda x: (len(x), x), default_comp),
                              (["c", "b", "a", "ab", "ba", "abc", "aaa", "abcd"], ["a", "b", "c", "ab", "ba", "aaa", "abc", "abcd"], lambda x: (-len(x), x), lambda x, y: -1 if x > y else 0 if x == y else 1)]
)
def test_quick_with_flag_and_comp(expr, ans, flag, comp):
    assert quick_sort(expr, flag=flag, comp=comp)