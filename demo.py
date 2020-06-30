#!/usr/bin/env python3
from typing import Any

from Regulable import Regulable
from Rule import Rule
from RuleChain import RuleChain


class TruncatorRule(Rule):

    def apply(self, regulable: Regulable, *args, **kwargs) -> int:
        if len(regulable):
            return regulable[:-1]

    def get_priority(self) -> int:
        return 3


class ExtenderRule(Rule):

    def apply(self, regulable: Regulable, *args, **kwargs) -> str:
        if len(regulable):
            return regulable + '_some_extension'

    def get_priority(self) -> int:
        return 10


class MyDependency:
    def log(self, logged: Any, *args, **kwargs) -> str:
        print('{}'.format(logged))


class MyRuleChain(RuleChain):

    rules = [
        TruncatorRule(),
        ExtenderRule()
    ]

    def __init__(self, logger: MyDependency = MyDependency):
        self.logger = logger()

    def run_logged(self, regulable: Regulable, *args, **kwargs):
        applied = self.run(regulable, args, kwargs)
        self.logger.log(applied)

        return applied


class SomeRegulableItem(Regulable, str):
    pass


item1 = SomeRegulableItem('hello')
item2 = SomeRegulableItem('goodbye')
items = [item1, item2]

chain = MyRuleChain()
for item in items:
    chain.run_logged(item)

