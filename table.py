import numpy as np
import math as m

class Table:

    def __init__(self, ranges, values=[]):
        # Ranges is an n+1 array, n dimensions for state values and last for action values
        self.ranges = ranges

        # If the user has not provided an intitialization for the table
        if not len(values):
            dims = tuple([r.shape[0]-1 for r in ranges])
            values = np.random.random_sample(size=dims)

        self.values = values

    def find_value_index(self, val, rng):
        # Binary search of val in list rng
        index = np.digitize(val, rng) - 1

        # Clipping all values between a min and max
        if index<0:
            index = 0
        if index>len(rng) - 2:
            index = len(rng) - 2
        return index

    def find_indices(self, vals):
        indices = []

        for idx, val in enumerate(vals):
            id_f = self.find_value_index(val, self.ranges[idx])
            indices.append(id_f)

        return tuple(indices)

    def get(self, vals):
        return self.values[self.find_indices(vals)]

    def set(self, vals, new_value):
        self.values[self.find_indices(vals)] = new_value



def unit_tests():
    # Define the constants
    vals = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]])

    # State (1d) can go from -4 to +4, action can go from -3 to -1, all other values
    rngs = [np.arange(-4, 4+2+2, 2), np.arange(-3, -1+1+1, 1)]
    tb = Table(ranges=rngs, values=vals)

    # Input is state_value, action_value
    inputs = [[-10, -10], [-2.5, 1.5], [0.5, 1.9], [100, 2]]
    outputs = [1, 3, 9, 15]

    for inp, out in zip(inputs, outputs):
        # Test access
        assert(tb.get(inp)==out), "%f==%f?"%(tb.get(inp), out)

    # Test without initializing vals
    tb = Table(ranges=rngs)

    for inp, out in zip(inputs, outputs):
        # Test that we don't get these values if we intialize with random weights
        assert(not tb.get(inp)==out), "%f==%f?"%(tb.get(inp), out)

if __name__ == "__main__":
    unit_tests()
