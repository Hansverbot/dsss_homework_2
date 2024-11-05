import unittest
from math_quiz import random_number, random_operator, create_function


class TestMathGame(unittest.TestCase):

    def test_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # TODO
        for _ in range(10):
             random_op=random_operator
             self.assertIn(random_op,['+','-','*'])
        

    def test_create_function(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),(3, 4, '*', '3 * 4', 12), (14,4,'-','14 - 4',10)
               ]
            

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                predicted_problem, predicted_answer=create_function(num1,num2,operator)
                self.assertEqual(predicted_problem,expected_problem)
                self.assertEqual(predicted_answer,expected_answer)
                # TODO
              

if __name__ == "__main__":
    unittest.main()
