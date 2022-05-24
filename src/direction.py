from __future__ import annotations
from enum import Enum


class direction(Enum):
    Long = 1
    Short = -1

    @staticmethod
    def parse(label: str) -> direction:
        l_label = label.lower()
        if l_label == 'long':
            return direction.Long
        elif l_label == 'short':
            return direction.Short
        else:
            raise NotImplementedError(msg=f"Unexpected string value {label}")
