from pydriller import RepositoryMining
import pandas as pd

date = []
file = []
change_type = []
lines_added = []
lines_removed = []
repo = RepositoryMining(path_to_repo="https://github.com/TheRenegadeCoder/sample-programs.git")
for commit in repo.traverse_commits():
    for modification in commit.modifications:
        date.append(commit.committer_date)
        file.append(modification.filename)
        change_type.append(modification.change_type.name)
        lines_added.append(modification.added)
        lines_removed.append(modification.removed)

df = pd.DataFrame(
    data={
        "date": date,
        "file": file,
        "change_type": change_type,
        "added": lines_added,
        "removed": lines_removed
    }
)

df.to_csv("git_data.csv")
