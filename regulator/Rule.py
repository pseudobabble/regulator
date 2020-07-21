#!/usr/bin/env python3
from abc import abstractmethod
from typing import Any


class Rule:

    rule_type = NotImplementedError

    @abstractmethod
    def apply(self, item, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def get_priority(self) -> int:
        raise NotImplementedError

    def run(self, item, *args, **kwargs) -> Any:
        if type(item) == self.rule_type:
            return self.apply(item, *args, *kwargs)

        return item

