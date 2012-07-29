from unittest import TestCase

from pious.transform.log import ConsoleLogger

class ConsoleLoggerTest(TestCase):
    
    def test_has_log_transform(self):
        l = ConsoleLogger()
        try:
            getattr(l, 'log_transform');
        except AttributeError:
            self.fail("Console logger is missing a log_transform method")
            
        i = { 'a': 'b' }
        o = { 'a': 'c'}
        l.log_transform(i, o)
         
