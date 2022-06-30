from re import M
from typing import List, Any


class Category:
    def __init__(self, name: str, ledger: List[dict] = None):
        self.name = name
        self.ledger = ledger

    def deposit(self, amount: int, description: str = '') -> None:
        # If the ledger attribute is of type `None` then it add an empty list to it.
        if self.ledger is None:
            self.ledger = []

        # appends the new dictionary to the ledger list.
        self.ledger.append({'amount': amount, 'description': description})

    def check_funds(self, amount: int) -> bool:
        # Creates a funs variable
        funds: int = 0

        # sum all of the deposits and withdraws amounts
        for i in range(len(self.ledger)):
            funds += self.ledger[i]['amount']

        # If the passed amount is less or equal than the current funds then it returns `True`
        if amount <= funds:

            # Returns true after confirming the condition
            return True

        # Default value
        return False

    def get_balance(self) -> None:
        # If the ledger attribute is of type `None` then it add an empty list to it.
        if self.ledger is None:
            self.ledger = []

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

    def transfer(self, amount: int, target) -> bool:
        # If the withdrawal is successfull then runs the target `deposit` function
        if self.withdraw(amount, f'Transfer to {target.name.capitalize()}'):

            # Adds the amount passed to the target object with message
            target.deposit(amount, f'Transfer from {self.name.capitalize()}')

            # Returns `True` if successfull
            return True

        # Default value
        return False

    def __repr__(self):
        char_limit: int  # a char limit variable
        title: str = ['*'] * char_limit

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


# food = Category('food')
# food.deposit(900, 'For food')
# food.withdraw(10, 'pizza')

# entertainment = Category('entertainment')
# entertainment.deposit(500, 'for movies and games')
# entertainment.withdraw(20, 'movies')
# entertainment.get_balance()

# print(f"entertainment before: {entertainment.ledger}")
# print(f"food before: {food.ledger} \n")

# food.transfer(200, entertainment)

# print(f"entertainment after: {entertainment.ledger}")
# print(f"food after: {food.ledger}")
