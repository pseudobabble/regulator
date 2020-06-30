#!/usr/bin/env python3
from abc import abstractmethod
from typing import Any


class Rule:

    rule_type = NotImplemented

    @abstractmethod
    def apply(self, item, *args, **kwargs) -> Any:
        raise NotImplemented

    @abstractmethod
    def get_priority(self) -> int:
        raise NotImplemented

    def run(self, item, *args, **kwargs):
        if isinstance(item, self.rule_type):
            return self.apply(item, *args, *kwargs)

        return item

