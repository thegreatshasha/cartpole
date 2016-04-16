from base import BaseManager
from ..agents.neural import NeuralLearner

class GameManager(BaseManager):

    def run(self):
        for epoch in self.epochs:
            for step in self.steps:
                self.update()


if __name__ == "__main__":
    """ Choose game """
    game = DodgeBrick({'size': (4,4)})

    """ Neural network for agent """

    """ Choose agent """
    agent = Agent(game.get_ranges(), network)

    """ Initialize manager and run experiment """
    manager = GameManager(game, agent)
