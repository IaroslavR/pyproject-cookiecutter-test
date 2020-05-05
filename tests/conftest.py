"""Package-wide test fixtures and pytest hooks"""

from typing import List, Optional

from _pytest.config import Config


# flake8: noqa: DAR101 DAR201
def pytest_assertrepr_compare(
        config: Config, op: str, left: str, right: str
) -> Optional[List[str]]:
    """Hook for PyCharm full diff fix.

    References:
        https://stackoverflow.com/a/50625086/4249707
    """
    if op in ("==", "!="):
        return ["{0} {1} {2}".format(left, op, right)]
