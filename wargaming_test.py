def is_even(value):
    """
    + Handles floats (returns False for anythingnot equal to an integer)
    - Slower than bitwise
    """
    return value % 2 == 0


def is_even_bitwise(value):
    """
    + Faster than modulo-based
    (3400 ns vs 132400 ns for value = 3**100000, timed with time.perf_counter_ns())
    - Throws TypeError if received a float
    """
    return not value & 1


class OverwritingCircularBuffer:
    """
    + Best used in contexts where uninterrupted reading is desired
    - Overwriting leads to loss of the oldest unread data
    """
    def __init__(self, length):
        self.container = {}
        self.length = length
        self.start = 0
        self.end = 0
        self.elements = 0

    def push(self, element):
        if self.is_full():
            self.start = (self.start + 1) % self.length
        else:
            self.elements += 1
        self.container[self.end] = element
        self.end = (self.end + 1) % self.length

    def pop(self):
        if self.is_empty():
            return 0
        else:
            out = self.container[self.start]
            self.start = (self.start + 1) % self.length
            self.elements -= 1
            return out

    def is_full(self):
        return self.elements == self.length

    def is_empty(self):
        return self.elements == 0


class CircularBuffer:
    """
    + Best used in contexts where data integrity is valued over processing speed
    - Without overwriting, the writer is forced to wait for the reader to keep up
    """
    def __init__(self, length):
        self.container = {}
        self.length = length
        self.start = 0
        self.end = 0
        self.elements = 0

    def push(self, element):
        if self.is_full():
            self.overwrite_handler()
        else:
            self.elements += 1
            self.container[self.end] = element
            self.end = (self.end + 1) % self.length

    def pop(self):
        if self.is_empty():
            return 0
        else:
            out = self.container[self.start]
            self.start = (self.start + 1) % self.length
            self.elements -= 1
            return out

    def is_full(self):
        return self.elements == self.length

    def is_empty(self):
        return self.elements == 0

    def overwrite_handler(self):
        """
        Handle overwrite attempts as needed, such as by logging, warnings, etc.
        """
        pass


def merge_sort(array):
    """
    If not forced to implement the sort, use array.sort() instead for O(n*log(n))
    time efficiency or faster if array is already sorted.
    Otherwise, merge sort has O(n*log(n)) time efficiency in worst and average case.
    """
    if len(array) <= 1:
        return array
    left = array[:len(array) // 2]
    right = array[len(array) // 2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    out = []
    while left and right:
        if left[0] < right[0]:
            out.append(left.pop(0))
        else:
            out.append(right.pop(0))
    out.extend(left)
    out.extend(right)
    return out


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    b = [4, 6, 2, 7, 7, 3, 1, 9]
    a = merge_sort(a)
    b = merge_sort(b)
    print(a)
    print(b)
