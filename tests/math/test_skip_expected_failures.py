import pytest

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    assert False

@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert 1 == 2
