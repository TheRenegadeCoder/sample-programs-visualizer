from pydriller import RepositoryMining
import pandas as pd

date = []
file = []
lines_added = []
lines_removed = []
repo = RepositoryMining(path_to_repo="https://github.com/TheRenegadeCoder/sample-programs.git")
for commit in repo.traverse_commits():
    for modification in commit.modifications:
        date.append(commit.committer_date)
        file.append(modification.filename)
        lines_added.append(modification.added)
        lines_removed.append(modification.removed)

df = pd.DataFrame(data={"date": date, "file": file})
print(df)
