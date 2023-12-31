from typing import Optional, List


class Stats:
    def __init__(self, values: List[int]):
        self.values = values
        self.max_amount = len(self.values)

    def _validate(self, number: int, high: Optional[int] = None) -> bool:
        """Perform basic validations."""

        if len(self.values) == 0:
            print('Error: It seems like there is no data for statistics.')
            return False

        if number < 1 or number > self.max_amount or (high != None and high > self.max_amount):
            print(f"Error: numbers should be in the range (0 - {self.max_amount})")
            return False

        if high != None:  # Range validation.
            if number > high:
                print('Error: `low` should be lower than `high`.')
                return False

            if high < 1:
                print('Error: `low` and `high` should be greater than zero.')

        return True

    def less(self, number: int) -> int:
        """Query how many numbers in the collection are less than a given value."""

        return self.values[number - 1] if self._validate(number) else -1

    def greater(self, number: int) -> int:
        """Query how many numbers in the collection are greater than a given value."""

        return self.values[self.max_amount - 1] - self.values[number] if self._validate(number) else -1

    def between(self, low: int, high: int) -> int:
        """Query how many numbers in the collection are within a specified range."""

        return self.values[high] - self.values[low - 1] if self._validate(low, high) else -1


class DataCapture:
    def __init__(self, max_amount = 1000) -> None:
        assert max_amount >= 0, "Only positive numbers"
        self.max_amount = max_amount
        self.elements = [0] * self.max_amount  # Creating empty list of zeros

    def add(self, number: int) -> bool:
        """Add a number to the collection."""
        if 0 <= number <= self.max_amount:
            self.elements[number] += 1
            return True
        else:
            print(f"Error: `number` should be in the range (0 - {self.max_amount})")
            return False

    def build_stats(self) -> Stats:
        sum = [0] * self.max_amount

        for idx, val in enumerate(self.elements):
            if idx == 0:
                sum[idx] = val
            else:
                sum[idx] = sum[idx - 1] + val

        return Stats(sum)
