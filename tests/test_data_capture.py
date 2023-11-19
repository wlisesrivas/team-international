from unittest import TestCase

from data_capture import DataCapture

class TestDataCapture(TestCase):
    def test_basic_operations(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()

        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.greater(4), 2)

    def test_empty_capture(self):
        capture = DataCapture()
        stats = capture.build_stats()

        self.assertEqual(stats.less(4), 0)
        self.assertEqual(stats.between(3, 6), 0)
        self.assertEqual(stats.greater(4), 0)

    def test_negative_numbers(self):
        capture = DataCapture()
        capture.add(-2)
        capture.add(5)
        capture.add(-1)
        capture.add(3)
        stats = capture.build_stats()

        self.assertEqual(stats.less(0), 2)
        self.assertEqual(stats.between(-3, 3), 4)
        self.assertEqual(stats.greater(0), 2)

    def test_repeated_numbers(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(3)
        capture.add(3)
        stats = capture.build_stats()

        self.assertEqual(stats.less(4), 3)
        self.assertEqual(stats.between(2, 5), 3)
        self.assertEqual(stats.greater(2), 0)
