import unittest
from day_predictor import get_day_of_week

class TestDayPredictor(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(get_day_of_week(1, 1, 2025), "Wednesday")
        self.assertEqual(get_day_of_week(15, 8, 1947), "Friday")
        self.assertEqual(get_day_of_week(29, 2, 2024), "Thursday")  # Leap year

    def test_invalid_dates(self):
        self.assertIn("Invalid date", get_day_of_week(31, 2, 2025))
        self.assertIn("Invalid date", get_day_of_week(29, 2, 2023))  # Not a leap year

if __name__ == "__main__":
    unittest.main()
