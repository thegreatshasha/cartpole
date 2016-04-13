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

    """ Apply physics here """
    def physics(self, action):
        raise NotImplementedError()

    """ Update the game state """
    def update(self):
        prev_state = self.get_state()
        action = self.agent.choose_action(prev_state) # Decide best action according to the agent
        reward, terminal = self.physics(action) # Execute that action
        next_state = self.get_state() # Get next state
        self.agent.update_Qvalue(prev_state, action, next_state, reward, terminal)

    """ Run the game loop and make the agent play """
    def run(self):
        raise NotImplementedError()
