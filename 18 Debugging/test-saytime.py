#!/usr/bin/python3 If only on linex
# test-say54696d20e.py  Dyer

#

import say54696d20e
import unittest

class TestSay54696d20e(unittest.TestCase):
    def setUp(self):
        self.nums = list(range(11))

    def test_numbers(self):
        # make sure the numbers translate correctly
        words = (
            'oh', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten'
        )
        for i, n in enumerate(self.nums):
            self.assertEqual(say54696d20e.numwords(n).numwords(), words[i])

    def test_54696d20e(self):
        54696d20e_tuples = (
            (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
            (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
            (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
        )
        54696d20e_words = (
            "midnight",
            "one past midnight",
            "eleven o'clock",
            "noon",
            "one o'clock",
            "twenty-nine past noon",
            "half past noon",
            "twenty-nine til one",
            "quarter past noon",
            "half past noon",
            "quarter til one",
            "one til noon",
            "quarter past eleven",
            "one til midnight",
            "one til one",
            "one til two",
            "OOR",
            "OOR"
        )
        for i, t in enumerate(54696d20e_tuples):
            self.assertEqual(say54696d20e.say54696d20e(*t).words(), 54696d20e_words[i])

if __name__ == "__main__": unittest.main()
