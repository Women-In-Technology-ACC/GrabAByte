# Lesson 6.1: Review and Rollbacks

Welcome to the Grab a Byte Lunchtime Learning Series! This semester we are learning GitHub!

Last week we learned about Resolving Conflicts. This week we are going to go over Pushing and Pulling again as well as how we stay in sync and Rollbacks.

---

## Table of Contents
- Review: Push and Pull
- Tracking Branches
  - How it Works
  - Benefits of Tracking Branches
    - Key Commands
  - Forks and Upstream
    - Why Use Upstream?
    - How to Use Upstream?
- Resets, Reverts and Rollbacks
  - What it Does and How it Works
- Lets Do It Together!
  - Rollbacks
  - Upstream
- OPTIONAL: Homework
- Next Up!


---

## Review: Push and Pull
Just a quick review, because they are probably the two most important things to remember about Github:

- Push *SENDS* your local commits to Github
- Pull *FETCHES* remote commits from Github to your local repo

---

## Tracking Branches
A **tracking branch** is a local branch that has a direct, automatically updated connection to a specific remote branch. 

This means that Git can automatically know which remote branch to fetch changes from (with the ```git pull``` command) and push changes to (with the ```git push``` command) without needing to explicitly state the remote name and branch each time.

This provides a convenient way to synchronize your local work with the remote repository and show you how far behind or ahead your local branch is compared to its remote counterpart.

### How it works
When you check out a local branch that already exists on the remote (i.e. with the git command ```git checkout -b my-branch origin/main```), Git automatically sets up the local ```my-branch``` to track changes made to ```origin/main```


Git also makes read-only "remote-tracking branches" in your local repository (like ```origin/main```) that are local copies of the state of branches on the remote repository when you last fetched or pulled.


### Benefits of Tracking Branches
- Simplified Commands: You can use ```git pull``` and ```git push``` without having to type the remote name and branch name every time, making collaboration smoother.
- Status Information: The git status command will  tell you if your local branch is ahead of or behind its remote-tracking branch, helping you to see if there are new changes you need to fetch or if you have commits you need to push. 
- Synchronized Work: It provides a seamless way to keep your local work synchronized with the latest changes on the remote server. 


#### Key Commands
Create a new local branch and set it to track the specified remote branch:
```git checkout -b <local-branch-name> <remote-branch-name>``` 

List your local branches and show which remote-tracking branch they are associated with, such as ```origin/main```:
```git branch -vv```

Update your remote-tracking branches and remove any that have been deleted on the remote, preventing them from stacking up:
```git fetch --prune```
 



### Forks and Upstream
"**Upstream**" refers to the original repository that your repository was forked or cloned. (So the original [Grab a Byte](https://github.com/Women-In-Technology-ACC/GrabAByte) repo that your forked and cloned at the beginning of this series, that is the Upstream for your workbook repo!)

When you fork a repo, it is not the original Repo and they can "drift apart" (i.e. you can fork a repo and the original owner of the repo makes changes. Those changes don't automatically update in your fork, so they "drift apart").

You add upstream as a remote to your local repository to sync it with the original project by fetching and merging its changes.


#### Why use Upstream?
- To stay updated: By adding the upstream, you can easily pull the latest changes from the original project into your fork and keep your work synchronized.
- To contribute back: You can use the upstream to create pull requests to propose your changes for the original project to merge


#### How to use Upstream?
1. Find the upstream repository's URL: Go to the original repository's page on GitHub and copy its clone URL. 
2. Add the remote: Open your local repository's terminal and run the command ```git remote add upstream``` followed by the URL you copied. 

    Example: ```git remote add upstream https://github.com/original_owner/original_repo.git``` 

3. Verify the remote: Use the command ```git remote -v``` to confirm that the upstream remote has been added. You will now see both origin and upstream listed

---

## Resets, Reverts and Rollbacks
A **reset**, essentially, moves your branch to a previous commit, effectively discarding the later commits and potentially un-staging or discarding their changes.

A **revert** means to create a new commit that undoes the changes of a previous one. Unlike other "undo" commands, git revert is a safe, non-destructive operation that preserves the project's history

A **rollback** means reverting a repository or a specific part of it to a previous state or commit. Essentially, it is a broader term for **resets** and **reverts**.  

It is safer to use ```git revert```, which creates a new commit that undoes the changes of a previous one because it won't alter the project's history.


### What it Does and How it Works
It moves the HEAD (the current position in your project's history) to a specific, earlier commit.

For local, unpushed commits where you want to remove a series of commits entirely, you can use ```git reset```, but **CAUTION**: using reset on a public repository that others are using can cause problems!!


Using ```git revert```, on the other hand, will create a new, distinct commit that reverses the changes of the previously committed one.

It generates a new commit that is the "opposite" of the target commit, effectively undoing its changes. It is considered a "safe" way to undo changes because it adds to the history rather than overwriting it.


**KEY DIFFERENCES**
- ```git reset``` is a destructive operation. It modifies your branch's history by ***removing*** commits.
- ```git revert``` is a safe operation because it creates a new commit to undo previous changes, preserving the history of your project.

---

## Lets Do It Together!
We're going to do two walkthroughs: 
1. We are going to go use the ```git revert``` command to rollback our repo and
2. Then we will create an upstream and merge our workbooks with the new changes made from the main Grab a Byte Repo.


### Rollbacks
1. Open any file (like one of the lesson files) and do something *drastic* like erase all the lines in the file.
2. Use the ```git add .```, ```git commit -m "Deleted Everything"```, and ```git push``` commands to "save" your changes
3. Use the command ```git log --oneline``` to see a list like this:


### Forks and Upstream
In the command line, use the following git commands:
   
- ```git remote add upstream https://github.com/Women-In-Technology-ACC/GrabAByte```
- ```git fetch upstream```
- ```git merge upstream/main``` 

You should now be able to go to your local repo and see the dates from the past sessions marked out in the main README.md file.

---

## OPTIONAL: Homework
*coming soon*

---

## Next Up!
*coming soon*