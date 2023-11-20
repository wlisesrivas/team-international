# Technical Challenge

## Overview

The DataCapture module is designed to efficiently capture and query statistics about a collection of numbers.

## Features

- `add(num)`: Add a number to the collection.
- `less(value)`: Query how many numbers in the collection are less than a given value.
- `greater(value)`: Query how many numbers in the collection are greater than a given value.
- `between(low, high)`: Query how many numbers in the collection are within a specified range.

## Usage

```python
from data_capture import DataCapture

# Initialize the DataCapture object
capture = DataCapture()

# Add numbers to the collection
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

# Build statistics object
stats = capture.build_stats()

# Query statistics
print(stats.less(4))       # should return 2
print(stats.between(3, 6))  # should return 4
print(stats.greater(4))     # should return 2
```

### Requirements
Python 3.6 and above

## Installation
Clone the repository and use the module in your Python project.
```bash
git clone https://github.com/wlisesrivas/team-international.git
cd team-international
```

## Testing
Run the provided unit tests to ensure the correctness of the implementation.

```bash
python -m unittest
```