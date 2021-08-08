import pytest

from bank_account import BankAccount

def test_repr(example_bank_account):
    """Makes sure the __repr__ works properly."""
    
    assert repr(example_bank_account) == "Owner: Test User - Money: 1000.0$"

def test_deposit_money(example_bank_account):
    """Makes sure the deposit is done correctly."""

    # Arrange
    money = 562.0

    # Act
    example_bank_account.deposit_money(money)

    # Assert
    assert 1562.0 == example_bank_account.money


def test_get_money(example_bank_account):
    """Makes sure the money is got correctly."""

    # Arrange
    money = 100.0

    # Act
    example_bank_account.get_money(money)

    # Assert
    assert 900.0 == example_bank_account.money


@pytest.mark.parametrize(
    "solvent_user",
    [
        BankAccount("User A", 1000.0),
        BankAccount("User B", 100000.0),
        BankAccount("User C", 50.0),
    ],
)
def test_has_money(solvent_user):
    """Makes sure the system knows when a user has got money."""

    # Act
    user_has_money = solvent_user.has_money()

    # Assert
    assert user_has_money

@pytest.mark.parametrize(
    "insolvent_user",
    [
        BankAccount("User A", -1000.0),
        BankAccount("User B", -100000.0),
        BankAccount("User C", 0.0),
    ],
)
def test_not_has_money(insolvent_user):
    """Makes sure the system knows when a user has not got money."""

    # Act
    user_has_money = insolvent_user.has_money()
    
    # Assert
    assert not user_has_money
    
# This way of parametrization can hurt clarification
@pytest.mark.parametrize(
    "user, expected_output",
    [
        (BankAccount("User A", -1000.0), False),
        (BankAccount("User B", 100000.0), True),
        (BankAccount("User C", 0.0), False),
    ],
)
def test_maybe_has_money(user, expected_output):
    """Makes sure the system knows whether a user has got money."""
    
    # Act
    user_has_money = user.has_money()
    
    # Assert
    assert user_has_money == expected_output

@pytest.mark.access_to_database
def test_time_update_database(benchmark, example_bank_account):
    """Tests the elapsed time when updating the database."""
    
    # Call
    benchmark(example_bank_account.update_database)
    
    # Since we are simulating the function, test always passes
    assert True
    
@pytest.mark.xfail
def test_failed():
    """This test always fails."""

    assert False

@pytest.mark.skip
def test_skip():
    """This test must be skipped."""

    assert False