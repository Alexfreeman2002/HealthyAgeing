from CaloriesQuestions.views import calulate_TDEE
import unittest


class TestCalories(unittest.TestCase):
    def test_calculate_calories(self):
        #define test data and run the function
        calories, deficit, gain = calulate_TDEE(weight=188, height=75, age=21, gender='m', activity=1.725)

        #expected result
        expected_calories = 3580
        expected_deficit = expected_calories*0.8
        expected_gain = expected_calories*1.2

        #tests whether the expected result is equal to the actual result
        self.assertEqual(expected_calories, calories)
        self.assertEqual(expected_deficit, deficit)
        self.assertEqual(expected_gain, gain)


if __name__ == '__main__':
    unittest.main()