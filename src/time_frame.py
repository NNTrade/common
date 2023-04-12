from __future__ import annotations
from enum import Enum


class TimeFrame(Enum):
    #TICKS = 1
    MINUTE1 = 2
    MINUTE5 = 3
    MINUTE10 = 4
    MINUTE15 = 5
    MINUTE30 = 6
    HOUR = 7
    HOUR4 = 8
    DAY = 9
    WEEK = 10
    MONTH = 11

    m1 = 2
    m5 = 3
    m10 = 4
    m15 = 5
    m30 = 6
    H = 7
    H4 = 8
    D = 9
    W = 10
    M = 11
    """
    -1 self > a
    0  self = a
    1  self < a
    """

    def to_seconds(self) -> int:
        if self == TimeFrame.MINUTE1:
            return 60
        elif self == TimeFrame.MINUTE5:
            return 60*5
        elif self == TimeFrame.MINUTE10:
            return 60*10
        elif self == TimeFrame.MINUTE15:
            return 60*15
        elif self == TimeFrame.MINUTE30:
            return 60*30
        elif self == TimeFrame.HOUR:
            return 60*60
        elif self == TimeFrame.HOUR4:
            return 60*60*4
        elif self == TimeFrame.DAY:
            return 60*60*24
        elif self == TimeFrame.WEEK:
            return 60*60*24*7
        elif self == TimeFrame.MONTH:
            return 365/12*60*60*24

    def compare(self, a) -> int:
        if self.value > a.value:
            return -1
        elif self.value < a.value:
            return 1
        return 0

    def short_name(self) -> str:
        if self == TimeFrame.MINUTE1 or self == TimeFrame.m1:
            return "m1"
        elif self == TimeFrame.MINUTE5 or self == TimeFrame.m5:
            return "m5"
        elif self == TimeFrame.MINUTE10 or self == TimeFrame.m10:
            return "m10"
        elif self == TimeFrame.MINUTE15 or self == TimeFrame.m15:
            return "m15"
        elif self == TimeFrame.MINUTE30 or self == TimeFrame.m30:
            return "m30"
        elif self == TimeFrame.HOUR or self == TimeFrame.H:
            return "H"
        elif self == TimeFrame.HOUR4 or self == TimeFrame.H4:
            return "H4"
        elif self == TimeFrame.DAY or self == TimeFrame.D:
            return "D"
        elif self == TimeFrame.WEEK or self == TimeFrame.W:
            return "W"
        elif self == TimeFrame.MONTH or self == TimeFrame.M:
            return "M"
        raise Exception(f"Unexpected TimeFrame {self}")

    def full_name(self) -> str:
        if self == TimeFrame.MINUTE1 or self == TimeFrame.m1:
            return "Minute1"
        elif self == TimeFrame.MINUTE5 or self == TimeFrame.m5:
            return "Minute5"
        elif self == TimeFrame.MINUTE10 or self == TimeFrame.m10:
            return "Minute10"
        elif self == TimeFrame.MINUTE15 or self == TimeFrame.m15:
            return "Minute15"
        elif self == TimeFrame.MINUTE30 or self == TimeFrame.m30:
            return "Minute30"
        elif self == TimeFrame.HOUR or self == TimeFrame.H:
            return "Hour"
        elif self == TimeFrame.HOUR4 or self == TimeFrame.H4:
            return "Hour4"
        elif self == TimeFrame.DAY or self == TimeFrame.D:
            return "Day"
        elif self == TimeFrame.WEEK or self == TimeFrame.W:
            return "Week"
        elif self == TimeFrame.MONTH or self == TimeFrame.M:
            return "Month"
        raise Exception(f"Unexpected TimeFrame {self}")

    def __eq__(self, other: TimeFrame) -> bool:
        if isinstance(other, TimeFrame):
            return self.value == other.value
        return False

    def __hash__(self) -> int:
        return hash(self.value)

    @staticmethod
    def parse(label: str):
        label = label.upper()
        if label in ('MINUTE1', 'M1'):
            return TimeFrame.MINUTE1
        elif label in ('MINUTE5', 'M5'):
            return TimeFrame.MINUTE5
        elif label in ('MINUTE10', 'M10'):
            return TimeFrame.MINUTE10
        elif label in ('MINUTE15', 'M15'):
            return TimeFrame.MINUTE15
        elif label in ('MINUTE30', 'M30'):
            return TimeFrame.MINUTE30
        elif label in ('HOUR', 'H'):
            return TimeFrame.HOUR
        elif label in ('HOUR4', 'H4'):
            return TimeFrame.HOUR4
        elif label in ('DAY', 'D'):
            return TimeFrame.DAY
        elif label in ('WEEK', 'W'):
            return TimeFrame.WEEK
        elif label in ('MONTH', 'M'):
            return TimeFrame.MONTH
        else:
            raise NotImplementedError(msg=f"Unexpected string value {label}")

    @staticmethod
    def try_parse(label: str) -> TimeFrame:
        try:
            return TimeFrame[label]
        except:
            return None

    def _compare(self, other:TimeFrame, method):
        try:
            return method(self.value, other.value)
        except (AttributeError, TypeError):
            # _cmpkey not implemented, or return different type,
            # so I can't compare with "other".
            return NotImplemented

    def __lt__(self, other):
        return self._compare(other, lambda s, o: s < o)

    def __le__(self, other):
        return self._compare(other, lambda s, o: s <= o)

    def __ge__(self, other):
        return self._compare(other, lambda s, o: s >= o)

    def __gt__(self, other):
        return self._compare(other, lambda s, o: s > o)

    def __ne__(self, other):
        return self._compare(other, lambda s, o: s != o)