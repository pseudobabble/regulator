#!/usr/bin/env python3
from typing import Any

from regulator.Rule import Rule
from regulator.RuleChain import RuleChain


class TruncatorRule(Rule):

    rule_type = str

    def apply(self, item, *args, **kwargs) -> str:
        return item[:-1]

    def get_priority(self) -> int:
        return 3


class ExtenderRule(Rule):

    rule_type = str

    def apply(self, item, *args, **kwargs) -> Any:
        return item + '_some_extension'

    def get_priority(self) -> int:
        return 10


class AdderRule(Rule):

    rule_type = int

    def apply(self, item, *args, **kwargs) -> Any:
        return item + 1


    def get_priority(self) -> int:
        return 1


class MyDependency:
    def log(self, logged: Any, *args, **kwargs) -> None:
        print('{}'.format(logged))


class MyRuleChain(RuleChain):

    rules = [
        TruncatorRule(),
        ExtenderRule(),
        AdderRule()
    ]

    def __init__(self, logger: MyDependency = MyDependency) -> None:
        self.logger = logger()

    def run_logged(self, item, *args, **kwargs) -> Any:
        applied = self.run(item, args, kwargs)
        self.logger.log(applied)

        return applied




item1 = 'hello'
item2 = 'goodbye'
item3 = 5
items = [item1, item2, item3]
# items = [item1, item2, item3]
# items = [item1]

chain = MyRuleChain()
for item in items:
    chain.run_logged(item)

