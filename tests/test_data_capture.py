from unittest import TestCase

from data_capture import DataCapture

class TestDataCapture(TestCase):
    def test_less(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()

        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.less(3), 0)
        self.assertEqual(stats.less(2), 0)

    def test_greater(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()

        self.assertEqual(stats.greater(4), 2)
        self.assertEqual(stats.greater(9), 0)
        self.assertEqual(stats.greater(3), 3)
        self.assertEqual(stats.greater(1), 5)
        self.assertEqual(stats.greater(10), 0)

    def test_between(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(9)
        capture.add(3)
        capture.add(4)
        capture.add(6)
        stats = capture.build_stats()

        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.between(3, 3), 2)
        self.assertEqual(stats.between(3, 4), 3)
        self.assertEqual(stats.between(4, 6), 2)
        self.assertEqual(stats.between(6, 9), 2)
        self.assertEqual(stats.between(9, 20), 1)
        self.assertEqual(stats.between(10, 15), 0)

    def test_empty_capture(self):
        capture = DataCapture()
        stats = capture.build_stats()

        self.assertEqual(stats.less(4), 0)
        self.assertEqual(stats.between(3, 6), 0)
        self.assertEqual(stats.greater(4), 0)

    def test_repeated_numbers(self):
        capture = DataCapture()
        capture.add(3)
        capture.add(3)
        capture.add(3)
        stats = capture.build_stats()

        self.assertEqual(stats.less(4), 3)
        self.assertEqual(stats.between(2, 5), 3)
        self.assertEqual(stats.greater(5), 0)
