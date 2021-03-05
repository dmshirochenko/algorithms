#!/usr/bin/env python3
import math
import random
import time
import unittest
import sys
import os

# import quicksort_asc from package dir above
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from sorting_algorithms.quicksort import quicksort_asc

def binary_search(checked_list, element_to_check):
    is_element_found = False

    # sort given list
    sorted_checked_list = quicksort_asc(checked_list)

    left, right = 0, len(sorted_checked_list)
    diff_right_left = -1

    while (diff_right_left != 1):

        diff_right_left = right - left
        mid_point_index = (right + left) // 2

        # go to check next part on left side
        if (sorted_checked_list[mid_point_index] > element_to_check):
            right = mid_point_index
        # go to check next part on right side
        elif(sorted_checked_list[mid_point_index] < element_to_check):
            left = mid_point_index
        elif(sorted_checked_list[mid_point_index] == element_to_check):
            is_element_found = True
            break

    return is_element_found


# liniear search to check binary
def linear_search(checked_list, element_to_check):
    for item in checked_list:
        if item == element_to_check:
            return True
    return False


class SmokeBinarySearchTest(unittest.TestCase):
    """
    It will be smoke tests for BinarySearch, which will just check basic scenarions
    and will not cover any corner cases and exception checks
    """

    def test_positive_odd_list(self):
        with self.subTest(checked_list=[5, 2, 3, 6, 8], element_to_check=5):
            checked_list = [5, 2, 3, 6, 8]
            element_to_check = 5
            self.assertEqual(binary_search(checked_list, element_to_check), True)

        with self.subTest(checked_list=[5, 2, 3, 6, 8], element_to_check=2):
            checked_list = [5, 2, 3, 6, 8]
            element_to_check = 2
            self.assertEqual(binary_search(checked_list, element_to_check), True)

        with self.subTest(checked_list=[5, 2, 3, 6, 8], element_to_check=3):
            checked_list = [5, 2, 3, 6, 8]
            element_to_check = 3
            self.assertEqual(binary_search(checked_list, element_to_check), True)

        with self.subTest(checked_list=[5, 2, 3, 6, 8], element_to_check=6):
            checked_list = [5, 2, 3, 6, 8]
            element_to_check = 6
            self.assertEqual(binary_search(checked_list, element_to_check), True)

        with self.subTest(checked_list=[5, 2, 3, 6, 8], element_to_check=8):
            checked_list = [5, 2, 3, 6, 8]
            element_to_check = 8
            self.assertEqual(binary_search(checked_list, element_to_check), True)


    def test_positive_even_list(self):
        with self.subTest(checked_list=[7, 8, 1, 9], element_to_check=7):
            checked_list = [7, 8, 1, 9]
            element_to_check = 7
            self.assertEqual(binary_search(checked_list, element_to_check), True)

        with self.subTest(checked_list=[7, 8, 1, 9], element_to_check=8):
            checked_list = [7, 8, 1, 9]
            element_to_check = 8
            self.assertEqual(binary_search(checked_list, element_to_check), True)

        with self.subTest(checked_list=[7, 8, 1, 9], element_to_check=1):
            checked_list = [7, 8, 1, 9]
            element_to_check = 1
            self.assertEqual(binary_search( checked_list, element_to_check), True)

        with self.subTest(checked_list=[7, 8, 1, 9], element_to_check=9):
            checked_list = [7, 8, 1, 9]
            element_to_check = 9
            self.assertEqual(binary_search(checked_list, element_to_check), True)


    def test_negative_odd_list(self):
        with self.subTest(checked_list=[5, 2, 3, 6, 8], element_to_check=1):
            checked_list = [5, 2, 3, 6, 8]
            element_to_check = 1
            self.assertEqual(binary_search(checked_list, element_to_check), False)
        with self.subTest(checked_list=[5, 2, 3, 6, 8], element_to_check=10):
            checked_list = [5, 2, 3, 6, 8]
            element_to_check = 10
            self.assertEqual(binary_search(checked_list, element_to_check), False)


    def test_negative_even_list(self):
        with self.subTest(checked_list=[7, 8, 1, 9], element_to_check=0):
            checked_list = [7, 8, 1, 9]
            element_to_check = 0
            self.assertEqual(binary_search(checked_list, element_to_check), False)
        with self.subTest(checked_list=[7, 8, 1, 9], element_to_check=10):
            checked_list = [7, 8, 1, 9]
            element_to_check = 10
            self.assertEqual(binary_search(checked_list, element_to_check), False)


    def test_with_negative_numbers(self):
        with self.subTest(checked_list=[-5, -2, -3, -6, -8], element_to_check=-5):
            checked_list = [-5, -2, -3, -6, -8]
            element_to_check = -5
            self.assertEqual(binary_search(checked_list, element_to_check), True)

        with self.subTest(checked_list=[-5, -2, -3, -6, -8], element_to_check=5):
            checked_list = [-5, -2, -3, -6, -8]
            element_to_check = 5
            self.assertEqual(binary_search(checked_list, element_to_check), False)

        with self.subTest(checked_list=[-5, 2, 3, 6, 8], element_to_check=2):
            checked_list = [-5, 2, 3, 6, 8]
            element_to_check = 2
            self.assertEqual(binary_search(checked_list, element_to_check), True)


    def test_random_compared_with_linear(self):
        checked_list = [random.randint(1, 999) for _ in range(100)]
        element_to_check = random.randint(1, 999)

        self.assertEqual(binary_search(checked_list, element_to_check),
                         linear_search(checked_list, element_to_check))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SmokeBinarySearchTest('test_positive_odd_list'))
    suite.addTest(SmokeBinarySearchTest('test_positive_even_list'))
    suite.addTest(SmokeBinarySearchTest('test_negative_odd_list'))
    suite.addTest(SmokeBinarySearchTest('test_negative_even_list'))
    suite.addTest(SmokeBinarySearchTest('test_with_negative_numbers'))
    suite.addTest(SmokeBinarySearchTest('test_random_compared_with_linear'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

    # time complexity check
    for i in [10_000, 100_000, 1_000_000, 10_000_000]:
        checked_list = [random.randint(1, 999) for _ in range(i)]
        element_to_check = random.randint(1, 999)

        timer_start = time.perf_counter()
        binary_search(checked_list, element_to_check)
        print('Binary search(with list sorting). Time to find in {0} elemets = {1}'.format(
            i, time.perf_counter() - timer_start))

        timer_start = time.perf_counter()
        linear_search(checked_list, element_to_check)
        print('Linear Search. Time to find in {0} elemets = {1}\n'.format(
            i, time.perf_counter() - timer_start))
