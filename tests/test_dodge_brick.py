import unittest
from games/dodge_brick import GameManager, RandomAgent
from dodge_brick import QLearningAgent

class TestStringMethods(unittest.TestCase):

    def test_uppercase(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_random_agent(self):
        # game should take agent as a parameter
        gm = GameManager(player=agent)
    	gm.add_object({
    		'dimensions': (1,3,1,1),
    		'type': 'player',
    		'color': COLORS['blue']
    	})
    	gm.add_object({
    		'dimensions': (0,1,1,1),
    		'type': 'enemy',
    		'color': COLORS['red']
    	})
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
