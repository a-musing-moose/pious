class KeyExists(object):
    """
    Creates a matcher that matches on the specified key
    """
    def __init__(self, key):
        self.key = key

    def as_matcher(self):
        def matcher(data):
            return self.key in data
        return matcher


class KeyEquals(object):
    """
    Creates a matchers that matches when `key` == `value`
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def as_matcher(self):
        def matcher(data):
            return self.key in data and data[self.key] == self.value
        return matcher


class Collection(object):
    """
    Holds a collection of matchers and returns true if any of them match
    """
    def __init__(self):
        self.matchers = []

    def add_matcher(self, matcher):
        """
        Add a new matcher

        `matcher` should either be a matcher function or an object that
        provides a `as_matcher` function which returns a matcher function
        """
        m = matcher
        if hasattr(m, 'as_matcher'):
            m = m.as_matcher()
        self.matchers.append(m)

    def as_matcher(self):
        def matcher(data):
            for m in self.matchers:
                if m(data):
                    return True
            return False
        return matcher
