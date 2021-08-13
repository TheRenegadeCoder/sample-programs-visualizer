import subete
import pandas as pd
import matplotlib.pyplot as plt

repo = subete.load()

data = {}
data["language"] = [lang for lang in repo.language_collections().keys()]
data["total_programs"] = [lang.total_programs() for lang in repo.language_collections().values()]
data["total_size"] = [lang.total_size() for lang in repo.language_collections().values()]
data["total_line_count"] = [lang.total_line_count() for lang in repo.language_collections().values()]

df = pd.DataFrame(data)#
df = df.set_index("language")

df["average_size"] = df["total_size"] / df["total_programs"]

filtered = df[df["total_programs"] > 5]

print(filtered)

ax = filtered.plot.scatter(x="total_programs", y="total_size")
for idx, row in filtered.iterrows(): 
    plt.text(row['total_programs'], row['total_size'], idx)

filtered.sort_values("average_size").plot.bar(y="average_size")


plt.show()
