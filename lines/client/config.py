"""Configuration file for TheRundown API."""
from enum import Enum


class ExtendedEnum(Enum):
    """ExtendedEnum delegation.."""

    @classmethod
    def list(cls):
        """List ExtendedEnum for Enum."""
        return list(map(lambda c: c.value, cls))


class RundownSportId(ExtendedEnum):
    """Sport ID Enumeration."""

    NCAAF = 1
    NFL = 2
    MLB = 3
    NBA = 4
    NCAAMB = 5
    NHL = 6
    UFC = 7
    WMBA = 8
    CFL = 9
    MLS = 10
