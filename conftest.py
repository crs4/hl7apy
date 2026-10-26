import pytest

import hl7apy


@pytest.fixture(autouse=True)
def _restore_hl7apy_defaults():
    """
    Restore the library-wide defaults after each test, since some doctests
    (e.g. :func:`hl7apy.set_default_version`) change them.
    """
    saved = (hl7apy._DEFAULT_VERSION, hl7apy._DEFAULT_ENCODING_CHARS, hl7apy._DEFAULT_VALIDATION_LEVEL)
    yield
    hl7apy._DEFAULT_VERSION, hl7apy._DEFAULT_ENCODING_CHARS, hl7apy._DEFAULT_VALIDATION_LEVEL = saved
