from pious.transform.errors import InvalidIterator

class Pipe(object):
    """
    The base object that should be extended by your own
    pipes
    """

    def __init__(self):
        self.watches = []
        self.logger = None

    def bind(self, iterator):
        """
        Binds an iterator (anything that provides __iter__)
        to this pipe
        """
        if not getattr(iterator, '__iter__'):
            raise InvalidIterator()
        self.iterator = iterator.__iter__()

    def set_logger(self, logger):
        """
        
        """
        self._logger = logger

    def add_watch(self, watch):
        self.watches.append(watch)
        
    def _apply(self, data):
        """
        This is the method called to perform the
        translation and should therefore be overridden
        in derived classes
        """
        return data

    def _is_watched(self, data):
        for watch in self.watches:
            if watch(data):
                return True
        return False

    def _log_watched(self, data_in, data_out):
        self.logger.log_transform(data_in, data_out)
    
    def __iter__(self):
        return self

    def next(self):
        data_in = self.iterator.next()
        data_out = self._apply(data_in)
        if self._is_watched(data_in) or self._is_watched(data_out):
            self._log_watched(data_in, data_out)
        return data_out


class Ensure(Pipe):
    """
    Ensure that the dict passing through has certain keys and that if they
    are not present then we set a default value
    """
    def __init__(self, map):
        super(Ensure, self).__init__()
        self.map = map

    def _apply(self, data):
        return dict(self.map.items() + data.items())


class Filter(Pipe):
    """
    Skips items that the passed in matcher
    tells it to

    matcher should be a function that returns
    True if the items should be filtered out
    """
    def __init__(self, matcher):
        self.matcher = matcher
        super(Filter, self).__init__()

    def next(self):
        data_out = super(Filter, self).next()
        while self.matcher(data_out):
            data_out = super(Filter, self).next()
        return data_out

class Rename(Pipe):
    """
    Renames keys based on the passed in key_map

    The key_map should be in the form:
    {'old key name': 'new key name',}
    """
    def __init__(self, key_map):
        self.key_map  = key_map
        super(Rename, self).__init__()

    def _apply(self, data):
        for key in self.key_map:
            if key in data:
                data[self.key_map[key]] = data[key]
                del data[key]
        return data

class Winnow(Pipe):
    """
    Removes unwanted keys from the data passing through
    """
    def __init__(self, keys):
        self.keys = keys
        super(Winnow, self).__init__()

    def _apply(self, data):
        for key in self.keys:
            if key in data:
                del data[key]
        return data

class AutoIncrement(Pipe):
    """
    Added a unique (for this pipe) auto-incrementing
    number to to the specified key
    """
    def __init__(self, key, start_value = 0, interval = 1):
        super(AutoIncrement, self).__init__()
        self.key = key
        self.counter_value = start_value
        self.interval = interval

    def _apply(self, data):
        self.counter_value += self.interval
        data[self.key] = self.counter_value
        return data