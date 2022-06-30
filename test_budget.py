from unicodedata import category
import unittest
# Note to myself. relative imports are only available like this
import budget


class CategoryTest(unittest.TestCase):
    # Inicializa la clase que se prueba para que se use en toda la clase de prueba.
    def setUp(self) -> None:
        self.video_games = budget.Category("video_games")
        self.food = budget.Category('food')

    def test_instantiation(self):
        actual = type(self.video_games)
        expected = type(self.video_games)
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
            actual, expected, "Expected `get balance method` to returrn the correct balanced of the category")


if __name__ == "__main__":
    unittest.main()
