import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("git_data.csv" , index_col=0, parse_dates=["date"])

df.plot(x="date", y=["added", "removed"])
plt.show()
