"""
A manager takes a game and one or more agents and runs the experiment. It also accumulates and prints any statistics
Manager classes should be really short and never more than 100 lines of code
Managers allow you to conduct complex experiments where you can pit one agent against another
Override from manager for maximum reuse as much as possible
"""
import pygame
class BaseManager:
    """ Take the game and the agent(s) as input. Agents are isomorphic so everything remains the same """
    def __init__(self, game, agent):
        self.game = game
        self.agent = agent
        self.font=pygame.font.Font(None,30)

        """ TODO: Add plotting class here """
        #self.plotter = Plotter()

    def run(self, steps, epochs):
        """ Run the update for however many steps etc you want """
        raise NotImplementedError()

    def long_press(self, action):
        terminal = False
        reward = 0
        for i in range(self.agent.long_press_times):
            r, t = self.game.act(action)
            reward += r
            terminal = terminal and t
        return reward, terminal

    def update(self):
        """ Run a single update step """
        
        prev_state = self.game.get_state()
        action = self.agent.choose_action(prev_state) # Decide best action according to the agent
        scoretext=self.font.render("Velocity: [%f-%f], Action: [%d]" % (self.game.agent['vel'][0], self.game.agent['vel'][1],action), 1,(255,255,255))
        self.game.screen.blit(scoretext, (250, 250))
        reward, terminal = self.long_press(action) # Execute that action
        next_state = self.game.get_state() # Get next state
        self.agent.update_Qvalue(prev_state, action, next_state, reward, terminal)

    def visualize(self):
        raise NotImplementedError()
