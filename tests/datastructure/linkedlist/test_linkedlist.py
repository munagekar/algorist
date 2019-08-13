from algorist.datastructure.linkedlist import LinkedList
import pytest


def test_linkedlist():
    li = LinkedList()
    assert list(li) == []
    li.push(1)
    assert list(li) == [1]
    li.push(2)
    assert li.front() == 2
    assert li.pop() == 2
    assert li.pop() == 1
    with pytest.raises(IndexError):
        li.pop()

    li.push(1)
    li.push(2)
    assert list(li) == [2, 1]
    assert len(li) == 2
