"""Lines Error Library."""


class BetFundLinesError(Exception):
    """BetFundLinesError Base Class."""
    pass


class InvalidSportIdError(BetFundLinesError):
    """InvalidSportId Error Delegation."""
    pass


class MalformedKeyError(BetFundLinesError):
    """MalformedKey Error Delegation."""
    pass
