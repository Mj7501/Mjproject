import pytest


@pytest.fixture()
def setup():
    print("  Opening the browser...")
    yield
    print("  closing the browser...")
