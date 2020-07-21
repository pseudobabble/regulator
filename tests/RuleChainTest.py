#!/usr/bin/env python3

import unittest

from regulator.Rule import Rule


class TestRuleChain(unittest.TestCase):

    def test_run(self):
        pass

    def test__higher_priority_is_run_first(self):
        first_rule = self._get_concrete_rule(str, 1, lambda x: x*2)
        second_rule = self._get_concrete_rule(str, 2, lambda x: x*3)

        item = 'X'
        item = first_rule.run(item)
        assert item == 'XX'

        item = second_rule.run(item)
        assert item == 'XXXXXX'



