#!/usr/bin/env python3

from typing import Any

from pytest import mark

from regulator import RuleChain
from regulator.Rule import Rule


class TestRuleChain:

    def test__create(self):
        rules = [Rule()]
        chain = self._get_rule_chain(rules)
        assert chain.rules == rules

    @mark.parametrize('rule_type, priority, function, item', [
        [str, 1, lambda x: x*2, 'a'],
        [bool, 1, lambda x: x, True],
        [int, 1, lambda x: x, 1],
        [float, 1, lambda x: x, 1.0],
        [list, 1, lambda x: x, []],
        [dict, 1, lambda x: x, {}],
    ])
    def test_run_chain(self, rule_type, priority, function, item):
        rules = [self._get_concrete_rule(rule_type, priority, function)]
        rule_chain = self._get_rule_chain(rules)
        modified_item = rule_chain.run(item)
        assert modified_item == function(item)


    def test__higher_priority_is_run_first(self):
        first_rule = self._get_concrete_rule(str, 1, lambda x: x.replace('X', 'U'))
        second_rule = self._get_concrete_rule(str, 2, lambda x: x*3)
        rule_chain = self._get_rule_chain([first_rule, second_rule])

        item = 'X'
        modified_item = rule_chain.run(item)
        assert modified_item == 'UUU'
        assert modified_item != 'XXX'

    def _get_rule_chain(self, rules_list):
        class MyRuleChain(RuleChain):
            rules = rules_list

        rule_chain = MyRuleChain()

        return rule_chain

    def _get_concrete_rule(self, type, priority, function):
        class ConcreteRule(Rule):
            rule_type = type

            def apply(self, item, *args, **kwargs) -> Any:
                return function(item)

            def get_priority(self) -> int:
                return priority

        concrete_rule = ConcreteRule()

        return concrete_rule
