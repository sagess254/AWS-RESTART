import pandas as pd

data = [104, 102, 103, 200, 202]
series = pd.Series(data, index=["A", 'B', "C", "D", "E"])

print(series[series < 200])
