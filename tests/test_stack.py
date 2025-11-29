from src.stack import LinkedList
import pytest

@pytest.mark.parametrize('nums, res', [([1, 2, 3], 3), ([1, 5], 5)])
def test_peek(nums, res):
    linked_list = LinkedList()
    for i in nums:
        linked_list.push(i)
    assert linked_list.peek() == res

@pytest.mark.parametrize('nums, res', [([1, 2, 3], [3, 2]), ([1, 5], [5, 1])])
def test_pop(nums, res):
    linked_list = LinkedList()
    for i in nums:
        linked_list.push(i)
    a = linked_list.pop()
    assert a == res[-2] and linked_list.peek() == res[-1]

@pytest.mark.parametrize('nums, res', [([1, 2, 3], 1), ([1, 5], 1)])
def test_min(nums, res):
    linked_list = LinkedList()
    for i in nums:
        linked_list.push(i)
    assert linked_list.min() == res

@pytest.mark.parametrize('nums, res', [([1, 2], False), ([], True)])
def test_is_empty(nums, res):
    linked_list = LinkedList()
    for i in nums:
        linked_list.push(i)
    assert linked_list.is_empty() == res

@pytest.mark.parametrize('nums, res', [([1, 2], 2), ([], 0)])
def test_len(nums, res):
    linked_list = LinkedList()
    for i in nums:
        linked_list.push(i)
    assert len(linked_list) == res

