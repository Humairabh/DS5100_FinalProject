from die import Die
from die import Game
from die import Analyzer
import unittest
import numpy as np
import pandas as pd
import random
from random import choices
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import groupby

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
        dicce = [attempt,attempt]
        uhhh = Game(dicce)
        uhhh.play(4)
        expected = (4,2)
        
        self.assertEqual(uhhh._playdf.shape, expected)

    def test_show(self):
        #test if the length of a narrow df is proportional to the length of a wide df
        #based on the # of Die
        
        narray = ['a','b','c']
        attempt = Die(narray)  
        dicce = [attempt,attempt]
        uhhh = Game(dicce)
        uhhh.play(4)
        narrow = len(uhhh.show("narrow"))
        wide = len(uhhh.show("wide"))
        
        self.assertEqual(narrow/len(dicce), wide)  

        
class AnalyzerTestCase(unittest.TestCase):
        
    def test_face_count(self):
        #test if the dataframe has an index of the roll number and face values as columns 
        #(i.e. it is in wide format)
        
        narray = ['a','b','c']
        attempt = Die(narray)  
        dicce = [attempt,attempt]
        uhhh = Game(dicce)
        uhhh.play(4)
        uh1 = Analyzer(uhhh)
        uh1.face_count()
        uh1.fc
        
        self.assertTrue(uh1.fc.columns.name=='Face')
        
    def test_jackpot(self):
        #test if returns an integer for the number times to the user.
        
        
        narray = ['a','b','c']
        attempt = Die(narray)  
        dicce = [attempt,attempt]
        uhhh = Game(dicce)
        uhhh.play(4)
        uh1 = Analyzer(uhhh)
        uh1.jackpot()
        
        self.assertTrue(type(uh1.jackpot())==int)
        self.assertTrue(uh1.jackpotdf.index.name=='rollNumber')

    def test_combos(self):
        #test method to compute the distinct combinations of faces rolled
        #along with their counts
        
        
        narray = ['a','b','c']
        attempt = Die(narray)  
        dicce = [attempt,attempt]
        uhhh = Game(dicce)
        uhhh.play(4)
        uh1 = Analyzer(uhhh)
        end = uh1.combo()
        
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main(verbosity=3)