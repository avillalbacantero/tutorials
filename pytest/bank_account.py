import random
import time

class BankAccount:
    """A class to simulate a bank account."""

    def __init__(self, name: str, money: float = 0.0) -> None:
        """Constructor.

        Args:
            name (str): The name of the owner.
            money (float, optional): Initial money. Defaults to 0.0.
        """

        assert isinstance(name, str),(
            f"Invalid name: {name}. Must be a str."
        )
        assert isinstance(money, float), f"{money} must be float."
        self.name = name
        self.money = money
        
    def __repr__(self) -> str:
        """Reproducible dunder method.

        Returns:
            str: A string representing the account info.
        """
        
        return f"Owner: {self.name} - Money: {self.money}$"

    def deposit_money(self, money: float) -> None:
        """Deposits money into the account.

        Args:
            money (float): The money to deposit.
        """

        assert isinstance(money, float), f"{money} must be float."
        assert money > 0.0, f"{money} must be a positive number."
        self.money += money

    def get_money(self, money: float):
        """Gets money from the account.

        Args:
            money (float): The money to get.
        """

        assert isinstance(money, float), f"{money} must be float."
        assert money > 0.0, f"{money} must be a positive number."
        assert self.money >= money,(
            f"There's no enough {money} in the account. " 
            f"Current money: {self.money}"
        )
        self.money -= money
        
    def has_money(self) -> bool:
        """Checks if the user has money.
        
        Return:
            bool: True if he/she has money, False otherwise.
        """     
        
        return self.money > 0.0
           
    def update_database(self) -> None:
        """Updates the database with the current information.
        
        This function is currently a simulation.

        """
        
        # Simulate that we update a database
        time.sleep(10)
        
# if __name__ == "__main__":
    
#     # Create some counts
#     NUM_ACCOUNTS = 3
#     all_accounts = []
#     for i in range(NUM_ACCOUNTS):
#         all_accounts.append(BankAccount(f"Subject {i}"))
    
#     # Some operations
#     NUM_OPS = 5
#     AVAILABLE_OPS = ["deposit", "get"]
#     for _ in range(NUM_OPS):
#         # Randomly choose what to do
#         random_account = random.choice(all_accounts)
#         random_op = random.choice(AVAILABLE_OPS)
#         random_money = random.uniform(.0, 1000.0)
        
#         print(f"Initial state: {repr(random_account)}")
        
#         # Operate
#         if random_op == "deposit":
#             random_account.deposit_money(random_money)
#         elif random_op == "get":
#             random_account.get_money(random_money)
#         else:
#             raise NotImplementedError(f"Invalid operation: {random_op}")
        
#         print(f"Final state: {repr(random_account)}")
        