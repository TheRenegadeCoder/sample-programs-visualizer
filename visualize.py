import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("git_data.csv" , index_col=0, parse_dates=["date"])

# Plot language changes
changes = df[df.change_type.isin(["ADD", "DELETE"])]
changes = changes.replace(["ADD", "DELETE"], [1, -1])
changes = changes.pivot_table(fill_value=0, aggfunc=sum, index="date", columns="language", values="change_type").cumsum()
changes.plot()
print(changes)

# Plot raw line changes
df.plot(x="date", y=["added", "removed"])

# Show the plots
plt.show()
