from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 3, "test") == "test"
    assert arrs.get([], 2, "test") == "test"
    assert arrs.get([1, 2, 3], 4, "test") == "test"
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([2, 3, 4, 5], 0, 3) == [2, 3, 4]
    assert arrs.my_slice([2, 3, 4, 5], -3, ) == [3, 4, 5]
    assert arrs.my_slice([],0 ,0 ) == []
    assert arrs.my_slice([1, 2, 3, 4], -1, -1) == []
    assert arrs.my_slice([1, 2, 3, 4], None, None) == [1, 2, 3, 4]
