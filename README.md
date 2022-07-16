# DS5100_FinalProject

Title:    Final Project <br />
Author:   Humaira Halim <br />
Date:     July 15, 2022 <br />
Comment:  In this project I will write, package, and publish a Python module and accompanying files. <br /> 
          The project will implement a simple Monte Carlo simulator using a set of related classes.

## To Install: <br />

git clone https://github.com/Humairabh/DS5100_FinalProject.git <br />
!pip install "path to local file"  <br />
          
## To Import: <br />

from die import Die <br />
from die import Game <br />
from die import Analyzer <br />
import numpy as np <br />
import pandas as pd <br />
import random <br />
from random import choices <br />
from itertools import combinations_with_replacement <br />
from itertools import groupby <br />

## Code sample to use Die object: <br />

#### Create Die object
narray = np.array(['a', 'b', 'c']) <br />
attempt = Die(narray) <br />

#### Change weight
attempt.change_weight('a',10) <br />
attempt.W #can see the weight has changed <br />

#### Roll Die 
attempt.roll_die(3) <br />


## Code sample to use Game object: <br />

#### Create Game object <br />
mygame = Game([attempt,attempt]) #using two Die objects <br />

#### Play a game <br />
type(mygame.play(4)) #roll each Die 4 times <br />

#### Show the dataframe of results <br />
len(mygame.show("narrow")) #show the Game outcome in a narrow dataframe format <br />

## Code sample to use Analyzer object: <br />

#### Create Analyzer object <br />
analyze_game = Analyzer(mygame) <br />

#### Return face count <br />
analyze_game.face_count() <br />
analyze_game.fc <br />

#### Return the number of jackpots <br />
analyze_game.jackpot()<br />

#### Return the number of jackpots <br />
analyze_game.combo()<br />

## Die Object Documentation:

class Die: <br />
    """ <br />
    A class used to represent a Die. A die has N sides, or "faces", and W weights, and can be rolled to select a face. <br />
<br />
    ... <br />
<br />
    Attributes <br />
    ---------- <br />
    N : array <br />
        an array of sides, or "faces" for the Die <br />
    W : array <br />
        an array of weights corresponding the the array of faces, defaults to 1.0 for each face <br />
      <br />  
    Methods <br />
    ------- <br />
    __init__ <br />
        Takes an array of faces as an argument. The array's data type (dtype) may be strings or numbers. <br />
        Internally initializes the weights to 1.0 for each face. <br />
        Saves both faces and weights into a private dataframe that is to be shared by the other methods. <br />
     <br />
    change_weight(self, face, new_weight) <br />
        A method to change the weight of a single side <br />
        <br />
    roll_die(self, nrolls=1) <br />
        A method to roll the die one or more times. Defaults to 1 roll <br />
    """ <br />

## Game Object Documentation: <br />
 <br />
    """  <br />
    A class used to represent a Game. A game consists of rolling of one or more dice of the same kind one or more times.  <br />
    The class keeps the results of its most recent play.   <br />
 <br />
    ...  <br />
 <br />
    Attributes  <br />
    ----------  <br />
    dice : array  <br />
        a list of already instantiated similar Die objects  <br />
 <br />
    Methods  <br />
    -------  <br />
    __init__  <br />
        Takes a single parameter, a list of already instantiated similar Die objects.  <br />
 <br />        
    play(self, nrolls)  <br />
        Takes a parameter to specify how many times the dice should be rolled.  <br />
        Saves the result of the play to a private dataframe of shape N rolls by M dice which can be accessed with show()  <br />
 <br />        
    show(self, show='wide')  <br /> 
        A method to pass the private play() dataframe to the user. Defaults to a wide dataframe  <br />
    """  <br />

## Analyzer Object Documentation: <br />
    """ <br />
    A class which takes the results of a single game and computes various descriptive statistical properties about it.  <br />
    These properties results are available as attributes of an Analyzer object. <br />
<br />
    ... <br />
<br />
    Attributes <br />
    ---------- <br />
    game : game object <br />
        an object of class Game <br />
<br />        
    Methods <br />
    ------- <br />
    __init__ <br />
        Takes a game object as its input parameter. <br />
        At initialization time, it also infers the data type of the die faces used <br />
<br />        
    jackpot(self) <br />
        A method to compute how many times the game resulted in all faces being identical <br />
<br />        
    combo(self, show='wide') <br />
        A method to compute the distinct combinations of faces rolled, along with their counts <br />
    """  <br />




