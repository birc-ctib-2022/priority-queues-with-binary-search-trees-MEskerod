"""Testing the search-tree based priority queue."""

from pq import (
    PriorityQueue,
    st_sort, pq_sort,
    general_merge,
    general_merge_persistent,
    special_merge, 
    special_merge_persistent
)
from itertools import permutations


def test_search_tree_sort() -> None:
    """
    Test that we can extract elements in sorted order.

    This test inserts values into a search tree and extracts
    them again, which should give us them in sorted order.
    """
    x = tuple(range(5))
    for y in permutations(x):
        assert x == tuple(st_sort(y))


def test_pq_sort() -> None:
    """
    Test that we can extract elements in sorted order.

    This test inserts values into a priority queue and extracts
    them one minimal element at a time. This should give us the
    elements back in sorted order.
    """
    x = tuple(range(5))
    for y in permutations(x):
        assert x == tuple(pq_sort(y))


def test_merge() -> None:
    """Test that we can merge priority queues."""
    data = tuple(range(10))
    x = PriorityQueue(data[:5])
    y = PriorityQueue(data[5:])
    assert data == tuple(iter(general_merge(x, y)))
    x = PriorityQueue(data[:5])
    y = PriorityQueue(data[5:])
    assert data == tuple(iter(special_merge(x, y)))

def test_merge_persistent() -> None: 
    data = tuple(range(10))
    x = PriorityQueue(data[:5])
    y = PriorityQueue(data[5:])
    assert data == tuple(iter(general_merge_persistent(x,y)))
    assert data == tuple(iter(special_merge_persistent(x,y)))
