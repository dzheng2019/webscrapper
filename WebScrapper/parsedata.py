from pprint import pprint
import json
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_json('datafiles/malData3.json')
print(data)
ax = plt.gca()

data.plot(kind='line',x= 'num',y='score',color='red',ax=ax)

plt.show()
