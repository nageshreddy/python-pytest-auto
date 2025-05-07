
def setup_method(self):
    self.sample_set = {1, 2, 3}


def test_add_element(self):
    # Add an element to the set
    self.sample_set.add(4)
    assert 4 in self.sample_set


def test_remove_element(self):
    # Remove an element from the set
    self.sample_set.remove(2)
    assert 2 not in self.sample_set


def test_union(self):
    # Test union of two sets
    other_set = {3, 4, 5}
    result = self.sample_set.union(other_set)
    assert result == {1, 2, 3, 4, 5}


def test_intersection(self):
    # Test intersection of two sets
    other_set = {2, 3, 4}
    result = self.sample_set.intersection(other_set)
    assert result == {2, 3}


def test_clear(self):
    # Clear the set
    self.sample_set.clear()
    assert len(self.sample_set) == 0