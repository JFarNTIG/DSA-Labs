import pytest
from sortlib.linkedlist import LinkedList


@pytest.fixture
def ll() -> LinkedList:
    return LinkedList()


def test_push_back(ll: LinkedList):
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    assert len(ll) == 3
    assert ll[0] == 1
    assert ll[1] == 2
    assert ll[2] == 3


def test_push_front(ll: LinkedList):
    ll.push_front(1)
    ll.push_front(2)
    ll.push_front(3)
    assert len(ll) == 3
    assert ll[0] == 3
    assert ll[1] == 2
    assert ll[2] == 1


def test_pop_front(ll: LinkedList):
    ll.push_back(10)
    ll.push_back(20)
    assert ll.pop_front() == 10
    assert len(ll) == 1
    assert ll[0] == 20

    assert ll.pop_front() == 20
    assert len(ll) == 0

    with pytest.raises(IndexError):
        ll.pop_front()


def test_pop_back(ll: LinkedList):
    ll.push_back(10)
    ll.push_back(20)
    assert ll.pop_back() == 20
    assert len(ll) == 1
    assert ll[0] == 10

    assert ll.pop_back() == 10
    assert len(ll) == 0

    with pytest.raises(IndexError):
        ll.pop_back()


def test_indexing(ll: LinkedList):
    data = [10, 20, 30, 40, 50]
    for val in data:
        ll.push_back(val)

    for i, val in enumerate(data):
        assert ll[i] == val

    with pytest.raises(IndexError):
        _ = ll[len(data)]

    with pytest.raises(IndexError):
        _ = ll[-1]


def test_size_tracking(ll: LinkedList):
    assert len(ll) == 0
    ll.push_front(1)
    assert len(ll) == 1
    ll.push_back(2)
    assert len(ll) == 2
    ll.pop_front()
    assert len(ll) == 1
    ll.pop_back()
    assert len(ll) == 0


def test_mixed_operations(ll: LinkedList):
    ll.push_back(1)
    ll.push_front(0)
    ll.push_back(2)
    ll.push_back(3)
    assert [ll[i] for i in range(len(ll))] == [0, 1, 2, 3]

    # should remove 0
    ll.pop_front() 
    
    # should remove 3
    ll.pop_back()
    assert [ll[i] for i in range(len(ll))] == [1, 2]


def test_empty_pop_errors(ll: LinkedList):
    with pytest.raises(IndexError):
        ll.pop_front()
    with pytest.raises(IndexError):
        ll.pop_back()


def test_single_element_behavior(ll: LinkedList):
    ll.push_back(99)
    assert len(ll) == 1
    assert ll[0] == 99
    assert ll.pop_front() == 99
    assert len(ll) == 0

    ll.push_front(88)
    assert ll[0] == 88
    assert ll.pop_back() == 88
    assert len(ll) == 0


def test_set_item(ll: LinkedList):
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)
    
    ll[0] = -1
    ll[3] = 99
    ll[4] = 101

    assert ll[0] == -1
    assert ll[1] == 2
    assert ll[2] == 3
    assert ll[3] == 99
    assert ll[4] == 101

    with pytest.raises(IndexError):
        ll[10] = 1

    with pytest.raises(IndexError):
        ll[-5] = 1