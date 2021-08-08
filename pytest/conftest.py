import pytest

from bank_account import BankAccount

@pytest.fixture
def example_bank_account():
    """An instance of BankAccount object."""
    
    return BankAccount("Test User", 1000.0)