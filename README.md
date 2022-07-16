# DS5100_FinalProject

Title:    Final Project <br />
Author:   Humaira Halim <br />
Date:     July 15, 2022 <br />
Comment:  In this project I will write, package, and publish a Python module and accompanying files. <br /> 
          The project will implement a simple Monte Carlo simulator using a set of related classes.

# Synopsis

To Install: <br />
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

### Create Die
narray = np.array(['a', 'b', 'c']) <br />
attempt = Die(narray) <br />

### Change weight
attempt.change_weight('a',10) <br />
attempt.W #can see the weight has changed <br />

### Roll Die 
attempt.roll_die(3) <br />



