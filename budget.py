from typing import List


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
        if funds >= amount:

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
        # If the withdrawal is successful then runs the target `deposit` function
        if self.withdraw(amount, f'Transfer to {target.name.capitalize()}'):

            # Adds the amount passed to the target object with message
            target.deposit(amount, f'Transfer from {self.name.capitalize()}')

            # Returns `True` if successfull
            return True

        # Default value
        return False

    def __repr__(self) -> str:
        header: str = self.name.center(30, "*") + "\n"
        ledger: str = ""
        for item in self.ledger:
            # format description and amount
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            # Truncate ledger description and amount to 23 and 7 characters respectively
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.get_balance())

        return header + ledger + total

    def __str__(self):
        return self.__repr__()


food = Category('food')
food.deposit(900, 'For food')
food.withdraw(10, 'pizza')

entertainment = Category('entertainment')
entertainment.deposit(500, 'for movies and games')
entertainment.withdraw(20, 'movies')
entertainment.get_balance()

# print(f"entertainment before: {entertainment.ledger}")
# print(f"food before: {food.ledger} \n")

# food.transfer(200, entertainment)

# print(f"entertainment after: {entertainment.ledger}")
# print(f"food after: {food.ledger}")
