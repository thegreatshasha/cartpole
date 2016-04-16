# Abstract class of a game

class AbstractGame:

    """ Takes in config hash and player object and initializes everything """
    def __init__(self, config, Agent):
        raise NotImplementedError()

    """ Returns the current state as a list of n  """
    def get_state(self):
        raise NotImplementedError()

    """ Return ranges for each n state_variable and 1 more for the state variable"""
    def get_ranges(self):
        raise NotImplementedError()

    """ Draw something to the screen """
    def draw(self):
        raise NotImplementedError()

    """ Execute the action and return reward """
    def act(self, action):
        raise NotImplementedError()
