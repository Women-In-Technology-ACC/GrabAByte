# Lesson 3.1: Collaboration Basics I

Welcome to the Grab a Byte Lunchtime Learning Series! This semester we are learning GitHub!

Last week we learned basic Git commands ```status```, ```add```, ```commit```, and ```push``` as well as best practices for commit messages and some example workflows. 

This week we are going to go over some Collaboration Basics

---

## Table of Contents
- What Collaboration?
- Branches
  - main vs master
  - Branch Commands
- Merges
  - Merge Commands
- Fetch vs Pull
- Lets Do It Together!
- OPTIONAL: Homework
- Next Up!


---

## What Collaboration?
Just like collaboration on a group project (is supposed to be) in the real world, you can collaborate with a group on a project in GitHub. 

This means that multiple people can work on the same codebase in the same repo at once! 

Members working on the same repo can avoid overwriting each others work by using branches and pull requests.

---


## Branches
**Branches** are separate versions of a project, allowing developers to work on different features or bug fixes without affecting the main, stable code. 

Each repository has a default branch (the default is main, but older repos might have a default called master, which we well cover below).

Think of branches like "drafts" of your project, or "development environments" where your main branch is your "production environment". Making edits to your branch does not effect other branches, until you merge them (which we will talk about later).


### main vs master
Before October 2020, the default branch was named "master" but in late 2020, GitHub wanted to start using more inclusive language so they changed the default name from master to main. 

If you ever need to rename your default branch, use the commands:
```
git branch -m master main
git push -u origin main
```

### Branch Commands
- ```git branch``` - lists all branches in your local repo
- ```git branch <branch-name>``` - creates a branch, replace ```<branch-name>``` with the name of the branch you want
- ```git branch <branch-name>``` - switches to ```<branch-name>``` branch
- ```git checkout -b <branch-name>``` - creates ```<branch-name>``` branch and switches to it immediately
- ```git push origin <branch-name>``` - pushes your local branch to GitHub
- ```git pull origin <branch-name>``` - pulls the latest version of that branch from GitHub


---


## Merges
In GitHub, a **merge** refers to the process of combining changes from one branch (like a feature branch) to another branch (usually the main branch).

Sometimes, when merging, Git may encounter merge conflicts. These occur when teh same lines of code in the same file have been modified in both branches. You have three options:

  1. Accept the other programmer's code
  2. Overwrite their code with yours
  3. Manually resolve each conflict
  
This will need to be done before the merge can be completed.

The result of a successful merge is a unified history on the main branch, incorporating all the changes from the merged branch.

### Merge Commands
- ```git merge <branch-name>``` - merges ```<branch-name>``` into your current branch (i.e. you are in the main branch and you call ```git merge add-feature``` it merges the add-feature branch into the main)
- ```git branch -d <branch-name>``` - deletes a branch locally after it's been merged
- ```git pull``` - pulls the latest changes from the remote repo and merges them into your current local branch
- ```git fetch``` - fetches the latest changes from GitHub but doesn't merge them yet --- use this when you want ot see what's new before deciding to merge
- ```git log --merge``` - shows commits that are causing a merge conflict


---


## Fetch vs Pull
*coming soon*

---


## Lets Do It Together!
*coming soon*

---


## OPTIONAL: Homework
*coming soon*

---


## Next Up!
*coming soon*