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

## Die object Documentation:

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




