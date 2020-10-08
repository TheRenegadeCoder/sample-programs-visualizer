from pydriller import RepositoryMining
repo = RepositoryMining(path_to_repo="https://github.com/TheRenegadeCoder/sample-programs.git")
for commit in repo.traverse_commits():
    print('Hash {}, author {}'.format(commit.hash, commit.author.name))
