from pprint import pprint
import json
import matplotlib.pyplot as plt
import pandas as pd

with open('malData.json') as f:
    jsonData = json.load(f)

data = pd.read_json('malData.json')
data['num'] = numpy.arange(len(data))
print(data)
ax = plt.gca()

data.plot(kind='line',x= 'num',y='score',color='red',ax=ax)

plt.show()
