#!/usr/bin/env python3
from abc import abstractmethod
from typing import Any

from Regulable import Regulable


class Rule:

    @abstractmethod
    def apply(self, regulable: Regulable, *args, **kwargs) -> Any:
        raise NotImplemented

    @abstractmethod
    def get_priority(self) -> int:
        raise NotImplemented
