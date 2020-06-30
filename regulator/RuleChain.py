#!/usr/bin/env python3

from typing import List

from regulator.Rule import Rule


class RuleChain:

    rules: List[Rule] = []

    def run(self, item, *args, **kwargs) -> None:
        rules = sorted(self.rules, key=lambda rule: rule.get_priority(), reverse=True)

        for rule in rules:
            item = rule.run(item, args, kwargs)

        return item
