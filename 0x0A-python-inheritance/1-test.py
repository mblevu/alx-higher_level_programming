#!/usr/bin/python3
from unittest import TestCase

# Tests that print_sorted() works correctly with a list of integers in ascending order
def test_print_sorted_with_integers_ascending(self):
    my_list = MyList([1, 2, 3, 4, 5])
    my_list.print_sorted()
    self.assertEqual(my_list, [1, 2, 3, 4, 5])

# Tests that print_sorted() works correctly with a list of integers in descending order
def test_print_sorted_with_integers_descending(self):
    my_list = MyList([5, 4, 3, 2, 1])
    my_list.print_sorted()
    self.assertEqual(my_list, [1, 2, 3, 4, 5])

# Tests that print_sorted() works correctly with a list of strings in ascending order
def test_print_sorted_with_strings_ascending(self):
    my_list = MyList(['apple', 'banana', 'cherry', 'date'])
    my_list.print_sorted()
    self.assertEqual(my_list, ['apple', 'banana', 'cherry', 'date'])

# Tests that print_sorted() works correctly with a list of strings in descending order
def test_print_sorted_with_strings_descending(self):
    my_list = MyList(['date', 'cherry', 'banana', 'apple'])
    my_list.print_sorted()
    self.assertEqual(my_list, ['apple', 'banana', 'cherry', 'date'])

# Tests that print_sorted() works correctly with an empty list
def test_print_sorted_with_empty_list(self):
    my_list = MyList([])
    my_list.print_sorted()
    self.assertEqual(my_list, [])

# Tests that print_sorted() works correctly with a list containing duplicate elements
def test_print_sorted_with_duplicate_elements(self):
    my_list = MyList([3, 2, 1, 2, 3])
    my_list.print_sorted()
    self.assertEqual(my_list, [1, 2, 2, 3, 3])