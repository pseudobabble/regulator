#!/usr/bin/env python3

from typing import List, Any

from Regulable import Regulable
from Rule import Rule


class RuleChain:

    rules: List[Rule] = []

    def run(self, regulable: Regulable, *args, **kwargs) -> Any:
        rules = sorted(self.rules, key=lambda rule: rule.get_priority(), reverse=True)
        for rule in rules:
            result = rule.apply(regulable, args, kwargs)
            return result
