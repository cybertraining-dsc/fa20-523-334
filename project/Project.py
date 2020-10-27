import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
db = pd.read_csv("API_IT.CEL.SETS.P2_DS2_en_csv_v2_1563234.csv")
db = db.fillna(0)
years = list(db.columns[4:65])
print(years)
db.set_index("Country Name",inplace= True)
aw = db.loc[["Arab World"],years]
print(aw.values)
print(length())
plt.figure()
plt.plot(years, aw.values)
plt.show()
for country in db.index:
    pass
