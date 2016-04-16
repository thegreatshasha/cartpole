from abstract import AbstractAgent
from ..datastructures.table import Table
from ..datastructures.ring_buffer import RingBuffer
from ..helpers.common import select_with_probability
import random

class NeuralLearner(AbstractAgent):
    """ Takes in a set of n+1 ranges as input, n for state variables and 1 for actions """
    def __init__(self, rngs, network):
        self.possible_actions = rngs[-1]

        """ Our machine learning model """
        self.network = network

        """ Pass these all in to make them tweakable """
        self.history_length = 4
        self.max_steps = 100
        self.max_epochs = 20
        self.batch_size = 32
        self.long_press_times = 1
        """ Disable this functionality initially """

        """ Q learning specific parameters """
        self.gamma = 0.9
        self.epsilon = 0.1
        #self.max_lives = 2
        self.update_frequency = 4

        """ The 4 parameters of our transition table """
        self.states = RingBuffer(shape=(self.max_steps, width, height))
        self.actions = RingBuffer(shape=(self.max_steps, 1))
        self.rewards = RingBuffer(shape=(self.max_steps, 1))
        self.terminals = RingBuffer(shape=(self.max_steps, 1))

        """ Accumulate statistics here """
        self.episode_sum = 0
        self.step = 0

    """ Store transition and do gradient descent on random minibatch """
    def update_Qvalue(self, pstate, action, nstate, reward, terminal):
        # Store this transition into the transition table
        self.states.push(pstate)
        self.actions.push(action)
        self.terminals.push(terminal)
        self.rewards.push(reward) # Should be made long press no support for long press right now

        # Sample a random minibatch and do gradient descent every update_frequency iterations
        if self.step % self.update_frequency == 0:
            x_batch, y_batch = self.__get_random_minibatch()
            self.__gradient_descent(x_batch, y_batch)

    """ Get the previous n states history and choose the best possible action """
    def choose_action(self, state):
        #Take the previous 4 observations
        history = self.__get_history(state)
        history_batch = np.array([state])
        prediction = model.predict(history_batch)[0]

        best_action = self.possible_actions[np.argmax(prediction)]
        random_action = random.choice(self.possible_actions)

        action = select_with_probability([random_action, best_action], [self.epsilon, 1-self.epsilon])
        #print "Step: %d, Epsilon: %f, Epoch: %d" % (self.step, EPSILON, epoch) What to do here?
        return best_action

    def __get_history(self, state):
        """ HACK!!!!! We are returning the same state 3 times. We should return the current + prev n states instead """
        prev_frames = [state]*3
        return np.array(prev_frames + [state])

    """ Anneal the greedy factor epsilon and fix it at 0.1 thereafter"""
    def __update_epsilon(self, step, total):
        self.epsilon = max((self.max_steps - float(self.step))/self.max_steps, 0.1)
        self.step += 1

    """ Do the actual gradient descent part """
    def __gradient_descent(self, x_batch, y_batch):
        if self.states.length >= self.batch_size:
            self.network.fit(x_batch, y_batch, batch_size=self.batch_size, nb_epoch=1)

    """ Converts -ve indices in ring buffer to +ve. Should probably be moved to ring buffer """
    def __transformed(index, bottom, length):
        return (index - bottom) % length

    """ Gets the neural net output duh! """
    def __get_network_output(state):
        history_batch = np.array([state])
        prediction = model.predict(history_batch)[0]
        return prediction

    """ Sample a random minibatch from the episodic memory and return it """
    def __get_random_minibatch(self):
        X_batch = []
        Y_batch = []
        indexes = images.indexes()

        while len(X_batch) < self.batch_size:
            random_index = random.choice(indexes)
            next_index = (random_index+1) % self.states.length
            # Transformed index
            transformed_index = self.__transformed(random_index, self.states.bottom, self.states.length)

            # If the transformed index is not within the necessary range
            if transformed_index < self.history_length - 1 or transformed_index == self.__transformed(self.states.top - 1, self.states.bottom, self.states.length):
                continue

            left = random_index - self.history_length + 1

            state1 = self.states.get(left, random_index+1)#images[left:random_index+1]
            state2 = self.states.get(left+1, random_index+2)

            # If the first state is terminal, it's the end of an episode and transitioning to an episode doesn't make sense
            if self.terminals[random_index]:
                continue

            output1 = self.__get_network_output(state1)
            output2 = self.__get_network_output(state2)

            X = state1
            Y = np.copy(output1)

            action_index = np.argmax(legal_actions==actions[random_index])

            # If the subsquent state is terminal, Q_2_a is zero since it's the teminal step
            #print "Reward %d" % rewards[random_index]
            if terminals[next_index]:
                Y[action_index] = rewards[random_index]
            else:
                Q_2_a = np.max(output2)
                #print "Q2a: %d" % Q_2_a
                Y[action_index] = rewards[random_index] + GAMMA * Q_2_a

            X_batch.append(X)
            Y_batch.append(Y)

        return np.array(X_batch), np.array(Y_batch)
