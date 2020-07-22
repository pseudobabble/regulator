#!/usr/bin/env python3

import pytest
from pytest import mark, raises
from typing import Any

from regulator.Rule import Rule


class TestRule:

    def test__create(self):
        rule = self._get_concrete_rule(str, 1, lambda x: x*2)
        assert rule.rule_type == str
        assert rule.get_priority() == 1

    def test__exceptions_raised_calling_abstract(self):
        rule = Rule()
        with raises(NotImplementedError):
            rule.apply('a')
        with raises(NotImplementedError):
            rule.get_priority()

    @mark.parametrize('valid_type, invalid_items, function', [
        (str, (True, 1, 1.0, [], {}), lambda x: x*2),
        (bool, ('hello', 1, 1.0, [], {}), lambda x: not x),
        (int, (True, 'hello', 1.0, [], {}), lambda x: x*2),
        (float, (True, 1, 'hello', [], {}), lambda x: x*2),
        (list, (True, 1, 1.0, 'hello', {}), lambda x: x.append(1)),
        (dict, (True, 1, 1.0, [], 'hello'), lambda x: x.set('a', 'a')),
    ])
    def test__no_change_on_invalid_type(self, valid_type, invalid_items, function):
        rule = self._get_concrete_rule(valid_type, 1, function)
        for invalid_item in invalid_items:
            assert rule.run(invalid_item) == invalid_item

    @mark.parametrize('valid_type, function, item, expected_change', [
        (str, lambda x: x*2, 'hello', 'hellohello'),
        (bool, lambda x: not x, True, False),
        (int, lambda x: x*2, 2, 4),
        (float, lambda x: x*2, 2.0, 4.0),
        (list, lambda x: x + [1], [], [1]),
        (dict, lambda x: dict({}, **{'a': 'a'}), {}, {'a': 'a'}),
    ])
    def test__expected_change_on_valid_type(self, valid_type, function, item, expected_change):
        rule = self._get_concrete_rule(valid_type, 1, function)
        assert rule.run(item) == expected_change

    def _get_concrete_rule(self, type, priority, function):
        class ConcreteRule(Rule):
            rule_type = type

            def apply(self, item, *args, **kwargs) -> Any:
                return function(item)

            def get_priority(self) -> int:
                return priority

        concrete_rule = ConcreteRule()

        return concrete_rule

