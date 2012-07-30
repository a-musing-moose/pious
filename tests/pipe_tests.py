from unittest import TestCase

from pious.transform.pipes import Pipe, Ensure, Rename
from pious.transform.pipes import RemoveKeys, AutoIncrement


class PipeTest(TestCase):

    def test_bind_accepts_iterator(self):
        a = [1, 2, 3]
        p = Pipe()
        try:
            p.bind(a)
        except Exception:
            self.fail("pipe.bind() raised an unexpectedly exception!")

    def test_bind_pukes_if_not_passed_an_iterator(self):
        p = Pipe()
        self.assertRaises(Exception, p, {})


class EnsureTest(TestCase):

    def test_sets_undefined_key(self):
        a = [
            {'a': 1, 'b': 1}
        ]
        p = Ensure({'c': 2})
        p.bind(a)
        for i in p:
            self.assertIn('c', i)

    def test_does_not_overwrite_existing_key(self):
        a = [
            {'a': 1, 'b': 1}
        ]
        p = Ensure({'a': 2})
        p.bind(a)
        for i in p:
            self.assertIn('a', i)
            self.assertEquals(i['a'], 1)


class RenameTest(TestCase):

    def test_renames_single_key(self):
        test_data = [
            {'old_key': 'a_value'},
            {'old_key': 'a_value'}
        ]
        key_map = {
            'old_key': 'new_key'
        }
        p = Rename(key_map)
        p.bind(test_data)
        for i in p:
            self.assertIn('new_key', i)
            self.assertEquals(i['new_key'], 'a_value')
            self.assertNotIn('old_key', i)

    def test_renames_multiple_keys(self):
        test_data = [
            {
                'old_key1': 'a_value1',
                'old_key2': 'a_value2'
            },
            {
                'old_key1': 'a_value1',
                'old_key2': 'a_value2'
            },
        ]
        key_map = {
            'old_key1': 'new_key1',
            'old_key2': 'new_key2'
        }
        p = Rename(key_map)
        p.bind(test_data)
        for i in p:
            self.assertIn('new_key1', i)
            self.assertEquals(i['new_key1'], 'a_value1')
            self.assertNotIn('old_key1', i)
            self.assertIn('new_key2', i)
            self.assertEquals(i['new_key2'], 'a_value2')
            self.assertNotIn('old_key2', i)


class RemoveKeysTest(TestCase):

    def test_single_key_removed(self):
        test_data = [
            {'a_key': 'a_value'},
        ]
        keys = [
            'a_key'
        ]
        p = RemoveKeys(keys)
        p.bind(test_data)
        for i in p:
                self.assertNotIn('a_key', i)

    def test_remaining_key_unaffected(self):
        test_data = [
            {'a_key': 'a_value', 'a_n_other_key': 'a_n_other_value'},
        ]
        keys = [
            'a_key'
        ]
        p = RemoveKeys(keys)
        p.bind(test_data)
        for i in p:
                self.assertNotIn('a_key', i)
                self.assertIn('a_n_other_key', i)
                self.assertEquals(i['a_n_other_key'], 'a_n_other_value')


class AutoIncrementTest(TestCase):

    def test_key_added(self):
        test_data = [
            {'a': 'b'},
            {'a': 'b'}
        ]
        p = AutoIncrement('counter')
        p.bind(test_data)
        for i in p:
            self.assertIn('counter', i)

    def test_key_increments(self):
        test_data = [
            {'a': 'b'},
            {'a': 'b'}
        ]
        p = AutoIncrement('counter')
        p.bind(test_data)
        c = 0
        for i in p:
            c += 1
            self.assertIn('counter', i)
            self.assertEquals(i['counter'], c)

    def test_key_increment_interval(self):
        test_data = [
            {'a': 'b'},
            {'a': 'b'}
        ]
        p = AutoIncrement('counter', interval=2)
        p.bind(test_data)
        c = 0
        for i in p:
            c += 2
            self.assertIn('counter', i)
            self.assertEquals(i['counter'], c)

    def test_key_increment_start(self):
        test_data = [
            {'a': 'b'},
            {'a': 'b'}
        ]
        p = AutoIncrement('counter', start_value=2)
        p.bind(test_data)
        c = 2
        for i in p:
            c += 1
            self.assertIn('counter', i)
            self.assertEquals(i['counter'], c)
