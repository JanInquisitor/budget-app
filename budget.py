from typing import List, Any


class Category:
    def __init__(self, name: str, ledger: List[dict] = None):
        self.name = name
        self.ledger = ledger

    def deposit(self, amount: int, description: str = '') -> None:
        if self.ledger is None:
            self.ledger = []
        self.ledger.append(
            {'amount': amount, 'description': description}
        )

    def check_funds(self, amount: int) -> bool:
        funds: int = 0
        for i in range(len(self.ledger)):
            funds += self.ledger[i]['amount']
        if amount <= funds:
            return True
        return False

    def get_balance(self) -> None:
        current_balance: int = 0
        for i in range(len(self.ledger)):
            current_balance += self.ledger[i]['amount']
        return current_balance

    def withdraw(self, amount: int, description: str = '') -> bool:
        # This checks if the passed ammount is greater than the overall available budget.
        if self.check_funds(amount):
            # This calls the `deposit` method with the amount passed converted to a negative integer with the description passed
            self.deposit(-abs(amount), description)
            # Returns `True` after the withdrawn amount is added to the ledger with the `deposit method`.
            return True
        # Default value
        return False

    def transfer(self, amount: int, category: str) -> bool:
      # A transfer method that accepts an amount and another budget category as arguments.
      # The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
      # The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]".
      # If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass


def create_spend_chart(categories: List[Category]):
    # The chart should show the percentage spent in each category passed in to the function.
    # The percentage spent should be calculated only with withdrawals and not with deposits.
    # Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character.
    # The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar.
    # Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

    # This function will be tested with up to four categories.
    pass


food = Category('food')
food.deposit(900, 'For food')
food.withdraw(10, 'pizza')

entertaiment = Category('entertainment')
entertaiment.deposit(500, 'for movies and games')
entertaiment.withdraw(20, 'movies')
