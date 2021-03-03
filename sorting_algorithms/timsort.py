#!/usr/bin/env python3
import math
import random
import time
import unittest


def insertion_sort_asc(items_to_sort, left=0, right=None):
    if right is None:
        right = len(items_to_sort) - 1

    for i in range(left + 1, right + 1):  # sort given subsections
        current_element = items_to_sort[i]
        position_to_check = i - 1

        # while will stop when we will find new place for current element
        while (position_to_check >= left and current_element < items_to_sort[position_to_check]):
            items_to_sort[position_to_check +
                          1] = items_to_sort[position_to_check]
            position_to_check -= 1

        items_to_sort[position_to_check + 1] = current_element

    return items_to_sort


def merging_lists(left, right):
    inf_number = math.inf
    left.append(inf_number)  # adding inf number to end of left list
    right.append(inf_number)  # adding inf number to end of right list

    merged_list = []
    left_index, right_index = 0, 0

    while True:
        # quit when both left and right lists will hit added before inf number
        if (left[left_index] == math.inf) and (right[right_index] == math.inf):
            break
        # choose the smalles element from both lists
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    return merged_list


def timsort_asc(items_to_sort):
    block_size = 128

    for i in range(0, len(items_to_sort), block_size):
        insertion_sort_asc(items_to_sort, i, min((i + block_size - 1), len(items_to_sort) - 1)) #min function will check end of the list
    #merging sorter blocks together
    size = block_size
    while size < len(items_to_sort):
        for start in range(0, len(items_to_sort), size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (len(items_to_sort) - 1))

            merged_array = merging_lists(
                items_to_sort[start: midpoint + 1],
                items_to_sort[midpoint + 1: end + 1])

            items_to_sort[start:start + len(merged_array)] = merged_array

        size *= 2

    return items_to_sort


class SmokeSortTest(unittest.TestCase):
    """
    It will be smoke tests for sorting algorithm, which will just check basic scenarions
    and will not cover any corner cases and exception checks
    """

    def test_negative_numbers_array(self):
        with self.subTest(items_to_sort=[-9, -3, -5, -7, -9]):
            self.assertEqual(timsort_asc([-9, -3, -5, -7, -9]), [-9, -9, -7, -5, -3])
        with self.subTest(items_to_sort=[-9, 3, 5, 7, -9]):
            self.assertEqual(timsort_asc([-9, 3, 5, 7, -9]), [-9, -9, 3, 5, 7])

    def test_all_zeros(self):
        self.assertEqual(timsort_asc([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_all_possitive(self):
        with self.subTest(items_to_sort=[4, 6, 7, 1, 3]):
            self.assertEqual(timsort_asc([4, 6, 7, 1, 3]), [1, 3, 4, 6, 7])
        with self.subTest(items_to_sort=[0, 6, 7, 1, 0]):
            self.assertEqual(timsort_asc([0, 6, 7, 1, 0]), [0, 0, 1, 6, 7])

    def test_already_sorted(self):
        with self.subTest(items_to_sort=[1, 2, 3, 4, 5]):
            self.assertEqual(timsort_asc([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        with self.subTest(items_to_sort=[5, 4, 3, 2, 1]):
            self.assertEqual(timsort_asc([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_hundred_elemets_againts_default_sort(self):
        items_to_sort = [random.randint(1, 999) for _ in range(100)]

        self.assertEqual(timsort_asc(items_to_sort.copy()),
                         sorted(items_to_sort))


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
        timsort_asc(items_to_sort)
        print('Time to sort {0} elemets = {1}'.format(i, time.perf_counter() - timer_start))
