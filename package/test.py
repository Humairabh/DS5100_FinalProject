from die import Die
from die import Game
import unittest
import numpy as np
import pandas as pd
import random
from random import choices
from itertools import combinations
from itertools import combinations_with_replacement

class DieTestCase(unittest.TestCase):
        
    def test_change_weight(self):
        # test if change_weight() method successfully changes the
        # weight of a face in the N attribute of Die class
        
        # Create die instance, changing the weight of face 'a'
        narray = np.array(['a', 'b', 'c'])
        attempt = Die(narray)
        attempt.change_weight('a',10)
        expected = 10.0
        # unittest.TestCase brings in the assertEqual() method
        self.assertEqual(attempt._dfpriv.weights.values[0], expected)

    def test_roll_die(self):        
        # test if roll_die() method successfully rolls the die "nrolls" number of times
        
        # Create die instance, rolling the die 3 times
        narray = ['a','b','c']
        attempt = Die(narray)
        attempt.roll_die(3)
        
        # Test
        expected = 3
        # unittest.TestCase brings in the assertEqual() method
        self.assertEqual(len(attempt.roll_die(3)), expected)        

    
    
class GameTestCase(unittest.TestCase):
        
    def test_play(self):
        #test if the result of the play saves to 
        #a private dataframe of shape 4 rolls by 2 dice.
        
        narray = ['a','b','c']
        attempt = Die(narray)        
        uhhh = Game([attempt,attempt])
        uhhh.play(4)
        expected = (4,2)
        
        self.assertEqual(uhhh._playdf.shape, expected)

    #def test_roll_die(self, nrolls=1):

        #self.assertEqual(len(attempt.roll_die(3)), expected)        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)