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


class MalformedPayloadError(BetFundLinesError):
    """MalformedPayload Error Delegation."""

    pass


class UnknownError(BetFundLinesError):
    """WHaT iS gOiNg oN!@!@?!?"""

    pass
