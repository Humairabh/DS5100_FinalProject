import numpy as np
import pandas as pd
import random
from random import choices
from itertools import combinations
from itertools import combinations_with_replacement

class Die:
    """
    A class used to represent a Die. A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 

    ...

    Attributes
    ----------
    N : array
        an array of sides, or “faces” for the Die
    W : array
        an array of weights corresponding the the array of faces, defaults to 1.0 for each face
        
    Methods
    -------
    __init__
        Takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers.
        Internally initializes the weights to 1.0 for each face.
        Saves both faces and weights into a private dataframe that is to be shared by the other methods.
    
    change_weight(self, face, new_weight) 
        A method to change the weight of a single side
        
    roll_die(self, nrolls=1)
        A method to roll the die one or more times. Defaults to 1 roll
    """
    
    def __init__(self, N, W=1.0):
        
        """
        Parameters
        ----------
        N : array
            an array of sides, or “faces” for the Die
        W : array
            an array of weights corresponding the the array of faces, 
            defaults to 1.0 for each face but can be changed after the object is created.
        """
        
        self.N = N
        self.W = np.ones(len(N))
        self._dfpriv = pd.DataFrame({'faces': self.N, 'weights': self.W})
        

    

    def change_weight(self, face, new_weight):
        
        """A method to change the weight of a single side.

            Checks to see if the face passed is valid; is it in the array of weights?
            Checks to see if the weight is valid; is it a float? Can it be converted to one?
            
            Parameters
            ----------
            face : str or int 
                the face value to be changed
            new_weight : float
                the new weight
        """
        try: 
            new_weight = float(new_weight)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
        if face in self._dfpriv.faces.values:
            self._dfpriv.loc[self._dfpriv.faces == face, "weights"] = new_weight
        
        
    def roll_die(self, nrolls=1):
        
        """A method to roll the die one or more times. Returns a list of outcomes

            If the arguement "nrolls" is not passed in, defaults to 1 
            
            Parameters
            ----------
            nrolls : int, optional
                how many times the die is to be rolled (default is 1)
        """
        
        result = choices(self.N, self.W,
              k=nrolls)
        return pd.Series(result)
    
    
    
    
    
class Game:
    """
    A class used to represent a Game. A game consists of rolling of one or more dice of the same kind one or more times. 
    The class keeps the results of its most recent play. 

    ...

    Attributes
    ----------
    dice : array
        a list of already instantiated similar Die objects

        
    Methods
    -------
    __init__
        Takes a single parameter, a list of already instantiated similar Die objects.
        
    play(self, nrolls)
        Takes a parameter to specify how many times the dice should be rolled.
        Saves the result of the play to a private dataframe of shape N rolls by M dice which can be accessed with show()
        
    show(self, show='wide')
        A method to pass the private play() dataframe to the user. Defaults to a wide dataframe
    """
    def __init__(self, dice):

        """
        Parameters
        ----------
        dice : array
            an array of already instantiated similar Die objects

        """
        self.dice = dice
    
    def play(self,nrolls):

        """A method which takes a number of times to roll the dice 

            Saves the result of the play to a private dataframe of shape N rolls by M dice.
        
            Parameters
            ----------
            nrolls : int
                the number of times to roll the dice 
        """        
        
        self._playdf = pd.DataFrame({'Roll #': range(0+1, len(self.dice[0].N)+1)}).set_index('Roll #')
        for x in range(len(self.dice)):
            self._playdf["Die"+str(x+1)] = self.dice[x].roll_die(nrolls+1)
    
    
        
    def show(self, show='wide'):

        """A method to show the user the results of the most recent play

            Passes the private dataframe to the user
        
            Parameters
            ----------
            show : 'wide' or 'narrow'
                choice to display dataframe in wide or narrow format (defaults to 'wide' form)
        """  
        
        if show=='wide':
            return self._playdf
        if show=='narrow':
            return self._playdf.unstack()

        
        
        
        
        
class Analyzer:
    """
    A class which takes the results of a single game and computes various descriptive statistical properties about it. 
    These properties results are available as attributes of an Analyzer object. 

    ...

    Attributes
    ----------
    game : game object
        an object of class Game

        
    Methods
    -------
    __init__
        Takes a game object as its input parameter. 
        At initialization time, it also infers the data type of the die faces used
        
    jackpot(self)
        A method to compute how many times the game resulted in all faces being identical
        
    combo(self, show='wide')
        A method to compute the distinct combinations of faces rolled, along with their counts
    """    
    
    def __init__(self, game):

        """
        Parameters
        ----------
        game : game object
            an object of class Game

        """
        self.game = game

    def face_count(self):

        """A method to compute how many times the game resulted in all faces being identical

            Returns an integer for the number times to the user.
            Stores the results as a dataframe of jackpot results in a public attribute .jackpotdf
        
            Parameters
            ----------
            analyzer : Analyzer object
                object of class Analyzer
        """  
    
        self.fc = self.game.show().apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        self.fc.columns.name = "Face"
    
    def jackpot(self):

        """A method to compute how many times the game resulted in all faces being identical

            Returns an integer for the number times to the user.
            Stores the results as a dataframe of jackpot results in a public attribute .jackpotdf
        
            Parameters
            ----------
            analyzer : Analyzer object
                object of class Analyzer
        """  

        df=self.game.show("wide")
        jackpot_number = len(df[df.nunique(axis=1)==1])
        self.jackpotdf = df[df.nunique(axis=1)==1]
        
        return jackpot_number
    

    def combo(self):

        """A method to compute the distinct combinations of faces rolled, along with their counts
        
            Stores the results as a dataframe in a public attribute.
        
            Parameters
            ----------
            analyzer : Analyzer object
                object of class Analyzer
        """  
        self.fc = self.game.show().apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        self.fc.columns.name = "Face"
        
        comb = list(combinations_with_replacement(self.fc.columns.tolist(), len(self.game.dice)))

        return comb
        
