from unittest import TestCase

from pious.transform.matchers import KeyExists, KeyEquals, Collection

class KeyExistsText(TestCase):

    def test_matches_if_key_present(self):
        test_data = {'a':'a'}
        m = KeyExists('a').as_matcher()
        self.assertTrue(m(test_data))

    def test_does_not_match_if_key_not_present(self):
        test_data = {'b':'b'}
        m = KeyExists('a').as_matcher()
        self.assertFalse(m(test_data))

class KeyEqualsTest(TestCase):

    def test_matches_if_key_value_correct(self):
        test_data = {'a':'a'}
        m = KeyEquals('a', 'a').as_matcher()
        self.assertTrue(m(test_data))

    def test_does_not_match_if_key_value_incorrect(self):
        test_data = {'a':'b'}
        m = KeyEquals('a', 'a').as_matcher()
        self.assertFalse(m(test_data))

    def test_does_not_match_if_key_does_not_exist(self):
        test_data = {'b':'a'}
        m = KeyEquals('a', 'a').as_matcher()
        self.assertFalse(m(test_data))

class CollectionTest(TestCase):

    def test_matches_with_one_matcher(self):
        test_data = {'a':'a'}
        collection = Collection()
        collection.add_matcher(KeyExists('a').as_matcher())
        m = collection.as_matcher()
        self.assertTrue(m(test_data))

    def test_matches_with_multiple_matchers(self):
        test_data = {'a':'a'}
        collection = Collection()
        collection.add_matcher(KeyExists('b').as_matcher())
        collection.add_matcher(KeyExists('a').as_matcher())
        m = collection.as_matcher()
        self.assertTrue(m(test_data))

    def test_does_not_match_when_none_added(self):
        test_data = {'a':'a'}
        collection = Collection()
        m = collection.as_matcher()
        self.assertFalse(m(test_data))

    def test_does_not_match_when_added_dont_match(self):
        test_data = {'a':'a'}
        collection = Collection()
        m = collection.as_matcher()
        collection.add_matcher(KeyExists('b').as_matcher())
        collection.add_matcher(KeyExists('c').as_matcher())
        self.assertFalse(m(test_data))