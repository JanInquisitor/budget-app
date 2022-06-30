from unicodedata import category
import unittest
# Note to myself. relative imports are only available like this
import budget


class CategoryTest(unittest.TestCase):
    # Inicializa la clase que se prueba para que se use en toda la clase de prueba.
    def setUp(self) -> None:
        self.entertainment = budget.Category("entertainment")
        self.food = budget.Category('food')

    def test_instantiation(self):
        actual = type(self.entertainment)
        expected = type(self.entertainment)
        self.assertEqual(actual, expected,
                         "Expected instance of the class 'Category'.")

    def test_deposit(self):
        self.food.deposit(900, "deposit")
        actual = self.food.ledger[0]
        expected = {"amount": 900, "description": "deposit"}
        self.assertEqual(
            actual, expected, 'Expected `deposit` method to create a specific object in the ledger instance variable.')

    def test_withdraw(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        actual: dict = self.food.ledger[1]
        expected: dict = {"amount": -45.67,
                          "description": "milk, cereal, eggs, bacon, bread"}
        self.assertEqual(
            actual, expected, 'Expected `withdraw` method to create a specific object in the ledger instance variable.')

        actual_2 = self.food.withdraw(1000, 'All my savings.')
        self.assertFalse(
            actual_2, "Expected `withdraw` method to return false if the amount withdrawed exceeds the amount available")

    def test_check_funds(self):
        self.food.deposit(100, 'deposit')
        actual = self.food.check_funds(110)
        expected = False
        self.assertEqual(actual, expected,
                         "Expected `check_funds` method to return False")
        actual = self.food.check_funds(100)
        expected = True
        self.assertEqual(actual, expected,
                         "Expected `check_funds` method to return True")

    def test_get_balance(self):
        self.food.deposit(1000, "deposit")
        self.food.deposit(200, "deposit")
        self.food.withdraw(300, "Meat, fish, milk, eggs and icecream.")
        actual: int = self.food.get_balance()
        expected: int = 900
        self.assertEqual(
            actual, expected, "Expected `get balance` method to return the correct balance of the category.")

    def test_transfer(self):
        self.food.deposit(900, "deposit")
        self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
        transfer_amount = 20
        food_balance_before = self.food.get_balance()
        entertainment_balance_before = self.entertainment.get_balance()
        good_transfer = self.food.transfer(transfer_amount, self.entertainment)
        food_balance_after = self.food.get_balance()
        entertainment_balance_after = self.entertainment.get_balance()
        actual = self.food.ledger[2]
        expected = {"amount": -transfer_amount,
                    "description": "Transfer to Entertainment"}
        self.assertEqual(
            actual, expected, 'Expected `transfer` method to create a specific ledger item in food object.')
        self.assertEqual(good_transfer, True,
                         'Expected `transfer` method to return `True`.')
        self.assertEqual(food_balance_before - food_balance_after, transfer_amount,
                         'Expected `transfer` method to reduce balance in food object.')
        self.assertEqual(entertainment_balance_after - entertainment_balance_before, transfer_amount,
                         'Expected `transfer` method to increase balance in entertainment object.')
        actual = self.entertainment.ledger[0]
        expected = {"amount": transfer_amount,
                    "description": "Transfer from Food"}
        self.assertEqual(
            actual, expected, 'Expected `transfer` method to create a specific ledger item in entertainment object.')


if __name__ == "__main__":
    unittest.main()
