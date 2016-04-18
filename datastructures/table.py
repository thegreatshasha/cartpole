import numpy as np
import math as m
import pdb

class Table:
    # Define a state table indexed not by indices but by state values. Binary search used for finding matching state

    def __init__(self, ranges, values=[]):
        # Ranges is an n+1 array, n dimensions for state values and last for action values
        self.ranges = ranges

        # If the user has not provided an intitialization for the table
        if not len(values):
            dims = tuple([r.shape[0]-1 for r in ranges])
            #values = np.zeros(dims)
            
            pdb.set_trace()
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

    # Retrieve an item
    def __getitem__(self, vals):
        return self.values[self.find_indices(vals)]

    # Set an item
    def __setitem__(self, vals, new_value):
        self.values[self.find_indices(vals)] = new_value

    # Returns action corresponding to maximum value
    def max_action(self, state):
        idx = np.argmax(self[state])
        return self.ranges[-1][idx]


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
        assert(tb[inp]==out), "%f==%f?"%(tb[inp], out)

    # Test to test that we get best action corresponding to Q value
    assert(tb.max_action([100])==-1), "%f==%f?"%(tb.max_dim([100]), -1)

    # Test without initializing vals
    tb = Table(ranges=rngs)

    for inp, out in zip(inputs, outputs):
        # Test that we don't get these values if we intialize with random weights
        assert(not tb[inp]==out), "%f==%f?"%(tb[inp], out)

if __name__ == "__main__":
    unit_tests()