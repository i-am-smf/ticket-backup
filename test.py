import git
import os

os.system("git add .")
os.system("git commit -m 'backup'")

# git.Commit("https://github.com/i-am-smf/ticket-backup.git",message="backup")

git.Git('i-am-smf/').push(f"https://github.com/i-am-smf/ticket-backup.git")
