import numpy as np
import math as m

class Table:

    def __init__(self, ranges, values=[]):
        # Ranges is an n+1 array, n dimensions for states and last for actions
        self.ranges = ranges

        # Tweak this to initialize with n+1 dimensions +1 for actions array, actions array will be discretized as well
        if not len(values):
            values = np.random.randn(rang.shape[0]-1)
        self.values = values

    def find_value_index(self, val, rng):
        index = np.digitize(val, rng) - 1
        # Clipping all values between
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

# Testing by trying to access various states
def test_get(inp, out):
    vals = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]])
    rngs = [np.arange(-4, 4+2+2, 2), np.arange(-3, -1+1+1, 1)]
    tb = Table(ranges=rngs, values=vals)
    assert(tb.get(inp)==out), "%f==%f?"%(tb.get(inp), out)
    return True

def unit_tests():
    # Input is state_value, action_value
    inputs = [[-10, -10], [-2.5, 1.5], [0.5, 1.9], [100, 2]]
    outputs = [1, 3, 9, 15]
    [test_get(inp, out) for inp, out in zip(inputs, outputs)]

if __name__ == "__main__":
    unit_tests()
