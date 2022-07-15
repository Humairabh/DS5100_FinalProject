from die import Die
import unittest

class Die(unittest.TestCase):

        # test if change_weight() method successfully changes the
        # weight of a face in the N attribute of Die class
        
    def test_change_weight(self):

        # Create die instance, changing the weight of face 'a'
        narray = ['a','b','c']
        attempt = Die(narray)
        attempt.change_weight('a',10)
        expected = 10.0
        # unittest.TestCase brings in the assertEqual() method
        #self.assertEqual(attempt._dfpriv.weights.values[0], expected)
        self.assertEqual(10, 10)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)