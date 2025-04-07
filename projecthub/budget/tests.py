from django.test import TestCase
from .models import Budget
from django.core.exceptions import ValidationError
from django.db.utils import DataError


class BudgetTests(TestCase):

    def test_valid_budget(self):
        budget = Budget(name='valid_budget', budget=100.00, category='IN', active=True)
        budget.full_clean()
        self.assertEquals(budget.name, 'valid_budget')

    def test_negative_budget(self):
        budget = Budget(name='negative_budget', budget=-100.00, category='IN', active=True)
        self.assertRaises(ValidationError, budget.full_clean)

    def test_big_budget(self):
        budget = Budget(name='big_budget', budget=10000, category='IN', active=True)
        self.assertRaises(ValidationError, budget.full_clean)

    def test_invalid_category(self):
        budget = Budget(name='big_budget', budget=100.00, category='OUT', active=True)
        self.assertRaises(ValidationError, budget.full_clean)
