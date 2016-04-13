# Abstract class of a game

class AbstractGame:

    """ Takes in config hash and player object and initializes everything """
    def __init__(self, config, player):
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

    """ Apply physics here """
    def physics(self):
        raise NotImplementedError()

    """ Update the game state """
    def update(self):
        prev_state = self.get_state()
        action = self.player.choose_action(prev_state) # Decide best action according to the agent
        self.update(action) # Execute that action
        next_state = self.get_state() # Get next state
        reward = self.player.get_reward(prev_state, next_state, action)
        self.player.update_Qvalue(prev_state, action, next_state, reward)
        self.draw()

    """ Run the game loop and make the agent play """
    def run(self):
        raise NotImplementedError()
