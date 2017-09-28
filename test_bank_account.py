import unittest

from bank_account import BankAccount, MinimumBalanceAccount


class AccountBalanceTestCase(unittest.TestCase):

    def setUp(self):
        self.my_account = BankAccount()

    def test_balance(self):
        self.assertEqual(self.my_account.balance, 3000, msg="Account Balance Invalid.")

    def test_deposit(self):
        self.my_account.deposit(4000)
        self.assertEqual(self.my_account.balance, 7000, msg="Deposit Method Inaccurate.")

    def test_withdraw(self):
        self.my_account.withdraw(500)
        self.assertEqual(self.my_account.balance, 2500, msg="Withdraw Method Inaccurate.")

    def test_invalid_transactions(self):
        self.assertEqual(self.my_account.withdraw(6000), "Invalid Transaction", msg="Invalid Transaction.")

    def test_sub_class(self):
        self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg="Not True subclass of Balance Account.")

