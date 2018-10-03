import os
import tempfile
import unittest

from word_distance import find_shortest_distance


class FindDistanceTest(unittest.TestCase):

    def setUp(self):
        self.sample_path = tempfile.mktemp()
        with open(self.sample_path, 'w') as fp:
            fp.write('''
                “We do value and reward motivation in our development team.
                Development is a key skill for a DevOp.”
            ''')

    def tearDown(self):
        os.unlink(self.sample_path)

    def test_find_shortest_distance(self):
        shortest = find_shortest_distance('development', 'motivation', self.sample_path)
        self.assertEqual(shortest, 2)
