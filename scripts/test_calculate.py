import unittest
import numpy as np
from scripts.calculate import calculate


class TestCalculate(unittest.TestCase):

    def test_calculate_valid_input(self):
        list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = calculate(list_data)

        expected_result = {
            'mean': [[4.0, 5.0, 6.0], [2.0, 5.0, 8.0], 5.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666],
                         6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178],
                                   [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[7, 8, 9], [3, 6, 9], 9],
            'min': [[1, 2, 3], [1, 4, 7], 1],
            'sum': [[12, 15, 18], [6, 15, 24], 45]
        }

        self.assertEqual(result, expected_result)

    def test_calculate_invalid_input_length(self):
        list_data = [1, 2, 3, 4, 5, 6, 7, 8]
        with self.assertRaises(ValueError):
            calculate(list_data)

    def test_calculate_empty_input(self):
        list_data = []
        with self.assertRaises(ValueError):
            calculate(list_data)

    def test_calculate_non_numeric_input(self):
        list_data = [1, 2, 3, 4, 'five', 6, 7, 8, 9]
        with self.assertRaises(TypeError):
            calculate(list_data)


if __name__ == '__main__':
    unittest.main()
