import unittest
import calculation


class TestCalculation(unittest.TestCase):
    def test_calculate_paid_amounts(self):
        # Test success case
        bidders = {
            "John Doe": 100,
            "John Smith": 500,
            "Sara Conor": 280,
            "Martin Fowler": 320,
        }
        paid_amounts = calculation.calculate_paid_values(bidders)
        self.assertEqual(paid_amounts["John Smith"], 320)
        self.assertEqual(paid_amounts["John Doe"], "Lost")

        # Test failure case
        bidders = "test bidders type"
        with self.assertRaises(ValueError) as ex:
            calculation.calculate_paid_values(bidders)
        err = ex.exception
        self.assertEqual(str(err), "Bidders must be a dict")

if __name__ == "__main__":
    unittest.main()
