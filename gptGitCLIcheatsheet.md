## 🛠️ Git CLI Cheat Sheet for Collaborative Projects

### 🔧 Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 📦 Clone a Project
```bash
git clone <repo-url>
```

### 🔀 Branching
```bash
git branch <branch-name>         # Create a new branch
git checkout <branch-name>       # Switch to a branch
git checkout -b <branch-name>    # Create and switch
```

### 📥 Get Latest Changes
```bash
git fetch                        # Get updates from remote (no merge)
git pull                         # Get and merge changes from current remote branch
```

### 💾 Making Changes
```bash
git status                       # Show changed files
git add <file>                   # Stage a file
git add .                        # Stage all changes
git commit -m "Message"          # Commit staged changes
```

### 📤 Push Changes
```bash
git push                         # Push current branch to origin
git push -u origin <branch>      # Push and track new branch
```

### 🔃 Merging & Conflicts
```bash
git merge <branch>               # Merge into current branch
# If conflict:
# - Manually resolve files
# - Then:
git add <resolved-file>
git commit
```

### ⏪ Undo & Reset
```bash
git restore <file>              # Discard local changes
git reset --soft HEAD~1         # Undo last commit, keep changes staged
git reset --hard HEAD~1         # Undo last commit, discard changes
```

### 🧹 Clean Up
```bash
git branch -d <branch>          # Delete local branch (merged)
git branch -D <branch>          # Force delete local branch
git push origin --delete <branch> # Delete remote branch
```

### 📌 Stashing (Temporary Shelve Changes)
```bash
git stash                       # Save uncommitted changes
git stash pop                   # Reapply stashed changes
```

### 🕵️ Check History & Diffs
```bash
git log                         # View commit history
git log --oneline --graph       # Compact view
git diff                        # Show unstaged changes
git diff --staged               # Show staged changes
```
