import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt

data = pd.DataFrame(
{
  "name":{ 'Yutaro', 'Koki', 'Ayumi', 'Manami', 'Daichi', 'Tomoya', 'Rika', 'Yui', 'Kenta', 'Mariko'},
  'birth_year': {1997, 1995, 1993, 1998, 1995, 1996, 1989, 1988, 1985, 1991},
  'height(cm)' : {175, 183, 162, 158, 172, 164, 168, 171, 167, 165},
  'weight' : {57, 70, 46, 39, 70, 58, 48, 49, 67, 51},
  'sex' : {'M', 'M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'F'}
},index= [1,2,3,4,5,6,7,8,9
])

data

