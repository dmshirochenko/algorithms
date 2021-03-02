#!/usr/bin/env python3
import math
import random
import time
import unittest


def insertion_sort_asc(items_to_sort):
    for i in range(1, len(items_to_sort)):
        current_element = items_to_sort[i]
        position_to_check = i - 1
        #while will stop when we will find new place for current element
        while (position_to_check >= 0 and current_element < items_to_sort[position_to_check]):
            items_to_sort[position_to_check + 1] = items_to_sort[position_to_check]
            position_to_check -= 1

        items_to_sort[position_to_check + 1] = current_element

    return items_to_sort

class SmokeSortTest(unittest.TestCase):
    """
    It will be smoke tests for sorting algorithm, which will just check basic scenarions
    and will not cover any corner cases and exception checks
    """
    def test_negative_numbers_array(self):
        with self.subTest(items_to_sort = [-9, -3, -5, -7, -9]):
            self.assertEqual(insertion_sort_asc([-9, -3, -5, -7, -9]), [-9, -9, -7, -5, -3])
        with self.subTest(items_to_sort=[-9, 3, 5, 7, -9]):
            self.assertEqual(insertion_sort_asc([-9, 3, 5, 7, -9]), [-9, -9, 3, 5, 7])

    def test_all_zeros(self):
        self.assertEqual(insertion_sort_asc([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_all_possitive(self):
        with self.subTest(items_to_sort=[4, 6, 7, 1, 3]):
            self.assertEqual(insertion_sort_asc([4, 6, 7, 1, 3]), [1, 3, 4, 6, 7])
        with self.subTest(items_to_sort=[0, 6, 7, 1, 0]):
            self.assertEqual(insertion_sort_asc([0, 6, 7, 1, 0]), [0, 0, 1, 6, 7])

    def test_already_sorted(self):
        with self.subTest(items_to_sort=[1, 2, 3, 4, 5]):
            self.assertEqual(insertion_sort_asc([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        with self.subTest(items_to_sort=[5, 4, 3, 2, 1]):
            self.assertEqual(insertion_sort_asc([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_hundred_elemets_againts_default_sort(self):
        items_to_sort = [random.randint(1, 999) for _ in range(100)]
        self.assertEqual(insertion_sort_asc(items_to_sort.copy()), sorted(items_to_sort))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SmokeSortTest('test_negative_numbers_array'))
    suite.addTest(SmokeSortTest('test_all_zeros'))
    suite.addTest(SmokeSortTest('test_all_possitive'))
    suite.addTest(SmokeSortTest('test_already_sorted'))
    suite.addTest(SmokeSortTest('test_hundred_elemets_againts_default_sort'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

    for i in [100, 1000, 10_000]:
        items_to_sort = [random.randint(1, 999) for _ in range(i)]
        timer_start = time.perf_counter()
        insertion_sort_asc(items_to_sort)
        print('Time to sort {0} elemets = {1}'.format(i, time.perf_counter() - timer_start))
