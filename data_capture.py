from typing import List


class Stats:
    def __init__(self, values: List[int], reversed_values: List[int]):
        self.values = values
        self.reversed_values = reversed_values

    def less(self, number: int) -> int:
        """Query how many numbers in the collection are less than a given value."""
        if number < 1 or len(self.values) == 0:
            print('Error: `number` should be greater than zero and there should be data in `values`.')
            return -1

        return self.values[number - 1]

    def greater(self, number: int) -> int:
        """Query how many numbers in the collection are greater than a given value."""
        if number >= 10000:
            return 0

        return self.reversed_values[number + 1]

    def between(self, low: int, high: int) -> int:
        """Query how many numbers in the collection are within a specified range."""

        if len(self.values) == 0:
            print('Error: There is no data in `values`.')
            return -1

        if low > high:
            print('Error: `low` should be lower than `high`.')
            return -1

        if low < 1 or high < 1:
            print('Error: `low` and `high` should be greater than zero.')
            return -1

        return self.values[high] - self.values[low - 1]


class DataCapture:
    def __init__(self, max_amount = 1000) -> None:
        self.max_amount = max_amount
        self.elements = [0] * self.max_amount  # Creating empty list of zeros

    def add(self, number: int) -> None:
        """Add a number to the collection."""
        self.elements[number] += 1

    def build_stats(self) -> Stats:
        self.sum = [0] * self.max_amount
        self.sum_reversed = [0] * self.max_amount

        for idx, val in enumerate(self.elements):
            reversed_current = self.max_amount - 1 - idx
            if idx == 0:
                self.sum[idx] = val
                self.sum_reversed[reversed_current] = self.elements[reversed_current]
            else:
                self.sum[idx] = self.sum[idx - 1] + val
                self.sum_reversed[reversed_current] = self.sum_reversed[reversed_current + 1] + self.elements[reversed_current]

        return Stats(self.sum, self.sum_reversed)
