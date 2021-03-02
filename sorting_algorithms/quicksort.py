#!/usr/bin/env python3
import math
import random
import time
import unittest


def quicksort_asc(items_to_sort):
    if len(items_to_sort) <= 1:
        return items_to_sort

    left = []
    equal = []
    right = []

    pivot_element = random.choice(items_to_sort) #choosing pivot elemet

    for item in items_to_sort:
        if item < pivot_element:
            left.append(item) #store elements that are less than pivot
        elif item > pivot_element:
            right.append(item) #store elements that are greater than pivot
        elif item == pivot_element:
            equal.append(item) #store elements that are equal than pivot

    return quicksort_asc(left) + equal + quicksort_asc(right)


class SmokeSortTest(unittest.TestCase):
    """
    It will be smoke tests for sorting algorithm, which will just check basic scenarions
    and will not cover any corner cases and exception checks
    """
    def test_negative_numbers_array(self):
        with self.subTest(items_to_sort = [-9, -3, -5, -7, -9]):
            self.assertEqual(quicksort_asc([-9, -3, -5, -7, -9]), [-9, -9, -7, -5, -3])
        with self.subTest(items_to_sort=[-9, 3, 5, 7, -9]):
            self.assertEqual(quicksort_asc([-9, 3, 5, 7, -9]), [-9, -9, 3, 5, 7])

    def test_all_zeros(self):
        self.assertEqual(quicksort_asc([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_all_possitive(self):
        with self.subTest(items_to_sort=[4, 6, 7, 1, 3]):
            self.assertEqual(quicksort_asc([4, 6, 7, 1, 3]), [1, 3, 4, 6, 7])
        with self.subTest(items_to_sort=[0, 6, 7, 1, 0]):
            self.assertEqual(quicksort_asc([0, 6, 7, 1, 0]), [0, 0, 1, 6, 7])

    def test_already_sorted(self):
        with self.subTest(items_to_sort=[1, 2, 3, 4, 5]):
            self.assertEqual(quicksort_asc([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        with self.subTest(items_to_sort=[5, 4, 3, 2, 1]):
            self.assertEqual(quicksort_asc([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_hundred_elemets_againts_default_sort(self):
        items_to_sort = [random.randint(1, 999) for _ in range(100)]
        self.assertEqual(quicksort_asc(items_to_sort.copy()), sorted(items_to_sort))


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

    #time complexity check
    for i in [100, 1000, 10_000, 100_000, 1_000_000, 10_000_000]:
        items_to_sort = [random.randint(1, 999) for _ in range(i)]
        timer_start = time.perf_counter()
        quicksort_asc(items_to_sort)
        print('Time to sort {0} elemets = {1}'.format(i, time.perf_counter() - timer_start))
