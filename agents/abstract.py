class AbstractAgent:
    """ Takes in a set of n+1 ranges as input, n for state variables and 1 for actions """
    def __init__(self, rngs):
        raise("Not implemented!")

    """ Update the qvalue based on the previous state, action """
    def update_Qvalue(self, pstate, action, nstate, reward):
        raise("Not implemented!")

    """ Choose the best action according for the current state """
    def choose_action(self, state):
        raise("Not implemented!")

    """ Get reward for a prev_state, action, next_state transition """
    def get_reward(self, prev_state, next_state, action):
        raise("Not implemented!")
