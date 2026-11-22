# Git mini exercise

Branch: `main`.

## 1. setup

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list
```

## 2. first repository

```bash
mkdir my-first-repo && cd my-first-repo
git init -b main
touch readme.txt
```

## 3. first commit

```bash
git status
git add readme.txt
git commit -m "Add readme file"
git log
```

## 4. make a change

```bash
echo "second line" >> readme.txt
git add readme.txt
git commit -m "Add a second line to readme"
```

## 5. look around

`git diff` shows unstaged changes. After `git add`, use `git diff --staged`.
`git log --oneline` shows one line per commit.

## 6. branches

```bash
git branch
git branch feature-script
git switch feature-script
git switch -c dev
git branch --show-current
```

## 7. script on a branch

On `feature-script`:

```bash
chmod +x install.sh
git add install.sh
git commit -m "Add install script"
```

## 8. merge

```bash
git switch main
ls
git merge feature-script
git log --oneline
git branch -d feature-script
```

No merge commit: `main` had not moved, so Git fast-forwards.

## 9. push

Create an empty repo on GitHub, without a README.

```bash
git remote add origin https://github.com/<user>/my-first-repo.git
git push -u origin main
```

## 10. delete and clone

```bash
cd ..
rm -rf my-first-repo
git clone https://github.com/<user>/my-first-repo.git
```

## 11. full workflow

```bash
mkdir bash-installer && cd bash-installer
git init -b main
echo "# bash-installer" > README.md
git add README.md && git commit -m "Add README"
git switch -c feature-install
cp ../my-first-repo/install.sh .
git add install.sh && git commit -m "Add install script"
git switch main
git merge feature-install
git branch -d feature-install
git remote add origin https://github.com/<user>/bash-installer.git
git push -u origin main
```

## Reflection questions

1. Version control keeps every version and lets you go back after a mistake.
2. Staging chooses what goes into the next commit.
3. Commit when one logical change works.
4. `init` creates a new repo, `clone` copies an existing one with its history.
5. Good messages say what changed and why.
6. Branches let you work without touching `main`.
7. Use a branch for a feature, a fix or an experiment.
