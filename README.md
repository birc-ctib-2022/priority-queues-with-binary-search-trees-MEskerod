# Search tree priority queues

Search trees and heaps are different structure, but only in the sense that the invariant for how nodes are arranged differ. For a search tree node `v`, `v.value` is greater than all values in `v.left` and smaller than all values in `v.right`, while for a (min-)heap, `v.value` is smaller than all values in both `v.left` and `v.right`.

The difference affects what we can efficiently do with both data structures. We can easily implement the same operations on them, but the structure for a search tree enables us to search for a value in `O(log n)` time, where in a heap we would have to do an `O(n)` linear search. If we have a search tree, we can run through all elements in sorted order in `O(n)` time, but if we wanted all the elements sorted from a heap we would need to iteratively `delete_min()` which would take time `O(n log n)`. These times flip when we consider constructing the structures, it is impossible to construct a search tree in less than `O(n log n)` but we know methods for building a heap of `n` elements in time `O(n)`.

The purpose of this exercise is not to argue that one structure is better than another, or even consider when one might be better than the other (the running times above give some hint at when this might be). It is just to familiarise yourself with the operations we want from a priority queue, but implemented with a data structure that you are already familiar with, the binary search tree. We will play with heaps in other exercises.

I have implemented a binary search tree in `src/pq.py`, first as a tree structure

```python
@dataclass
class Node(Generic[T]):
    """Inner node in a search tree."""

    value: T
    left: Tree[T] = None
    right: Tree[T] = None


Tree = Optional[Node[T]]
```

and then wrapped in a class

```python
@dataclass(init=False)
class SearchTree(Generic[T]):
    """A search tree."""

    root: Tree[T]
```

The `Tree[T]` trees are implemented as a persistent data structure, so all the functions that operate on them leave the input alone but return new trees that reflect the updates. The `SearchTree` class holds a reference to the root of a tree, and if you use its operations, it will update this reference, so operations on this class will modify the tree instead of returning a new version.

Then, I have written an outline of a priority queue class that uses a search tree as its main structure.

```python
class PriorityQueue(SearchTree[T]):
    """Priority queue implemented using a search tree."""
```

The `class PriorityQueue(SearchTree[T])` syntax says that `PriorityQueue` can do anything a `SearchTree` can do, so you get the `root` attribute and all operations from `SearchTree` for free. You just need to implement the priority queue interface from it.

You are free to change any of the code, whether the functions or `SearchTree` methods, or basically anything you want, as long as you implement the priority queue operations using a search tree.

**Exercise:** Implement a heap using a search tree (i.e. fill out the missing methods in the `PriorityQueue` class).

**Exercise:** Implement a sort algorithm based on it (i.e. implement the `pq_sort()` function in `src/pq.py`).

**Exercise:** Implement a merge operation on this heap (i.e. the `general_merge()` function in `src/pq.py`). You cannot get it really effective, so the simplest thing you can think of is probably as good as it gets.

**Exercise:** If you have two search trees, where all elements in the first are smaller than all elements in the second, can you merge them smarter than if they do not have this property? What would the complexity be? Implement your idea in `special_merge()` in `src/pq.py`.