# Lesson 4.1: Collaboration Basics I

Welcome to the Grab a Byte Lunchtime Learning Series! This semester we are learning GitHub!

Last week we learned Collaboration Basics like branching, merging, fetching and pulling.

This week we are going to go over some more Collaboration Basics.

---

## Table of Contents
- Pull Requests
  - When/Why to do Them
- Code Reviews
- Collaborators vs Reviewers
- Lets Do It Together!
- OPTIONAL: Homework
- Next Up!


---

## Pull Requests
In GitHub, Pull Requests (sometimes abbreviated to just "PR"), is a proposal to merge changes from one branch (the source branch) to another (the target branch, often the main branch).

I know what you are thinking: *Wait, Rikki...didn't we do this last week?*

Yes.

Kind of.

We absolutely did, but we didn't go into detail. Today we are going into detail!

Last week we did it very fast. In the real world the process can go much slower. 

Last week we: 
- created a new branch
- made changes to that branch and committed them
- switched to the main branch
- fetched and pulled the new branch, merging it with the main branch.

In the real world you would pause at the "pulled the new branch" part and just do a pull request instead of a pull. This opens the floor for enhanced collaboration because with a pull request, all collaborators can review and discuss the proposed set of changes before they integrate the changes into the main codebase. 


### When/Why to do Them?
So, when *should* you open a PR?
  - When your feature or fix is complete
  - When you want feedback or approval
  - Even solo developers open PRs to track history


---

## Code Reviews
One of the most collaborative things you will do in the tech world are Code Reviews.

Code Reviews are opportunities for teammates to give feedback, suggest improvements, catch bugs, etc.

Teammates cna then "approve" or "request changes" be made tot he code to help improve code quality and shared understanding.

---

## Collaborators vs Reviewers
So, who can do what? What are the permissions?

| ROLE | Can Edit Repo | Can Review PRs | Can Merge |
|------|---------------|----------------|-----------|
| Owner | ✅ | ✅ | ✅ |
| Collaborator | ✅ | ✅ | ✅ | 
| Reviewer Only | ❌ | ✅ | ❌ |


You can add Collaborators via the **Repo Settings > Collaborators**
You can add Reviewers via the PR Sidebar

---

## Lets Do It Together!
1. Open your command line and make sure you are in your project folder (remember to use ```cd``` to move around)
2. From the command line, type the command ```git branch math-problem``` to create a new branch called "math-problem".
3. Switch to your new branch by using the command ```git checkout math-problem```
4. Make a small change to this file 
    - ANSWER THIS: What is 3 x 7 = ?
5. Enter the ```git status``` command to check that this file needs to be added.
6. Enter the command ```git add .```, which adds all files that have been modified to the staging area
7. Commit the file you just added (remember to use the command ```git commit -m``` and add your message).
8. Then push them via the ```git push``` command.
9. Open this github repo in your browser, make sure you are logged in
10. Click on the "Pull Requests" Tab (Third from the left)
11. Click on the "New Pull Request" Button
12. You will see two drop downs, one for "base" make sure that is set to main and one for "compare", this should be the new branch (the one we named "math-problem")
13. The page should show a list of all differences between the two branches. When you are ready, click "Create Pull Request"
14. You now can enter a title and description for this pull request. Be clear and simple in the title like you would the messages you add when pushing, you can add more detail to the description.
15. Before you press the button to create the pull request, look at the right menu options:
    - **Reviewers** - click the gear icon to add reviewers
    - **Assignees** - click the gear icon to add assignees ( you can assign yourself )
    - **Labels** - click the gear icon to add labels like: bug, documentation, duplicate, enhancement, good first issue, help wanted, invalid, question, wontfix, or even edit or add labels
    - **Projects** - click the gear icon to add Projects (we will cover projects later)
    - **Milestones** - click the gear icon to add Milestones (we will cover Milestones later)
    - **Development** - use "closing keyword" in the description to automatically close issues (we will cover Issues later)
16. There is a drop down button "Create Pull Request" you can see there are two options:
    1.  Create Pull Request - Open a pull request that is ready for review
    2.  Create Draft Pull Request - Cannot be merged until marked ready for review
17. Click "Create Pull Request" and it will take you to the review page. This is where you would stop in a collaborative environment and let your team/managers handle reviewing your changes and determining if they should be combined with the main branch. You should see a "Add a comment" box at the bottom where you can add messages to communicate with your team/managers.
    - Add a few comments now (they can be whatever)
    - Scroll up the page and see where the comment ended up
    - Click to add an emoji and click on the ```...``` to see what addition options there are
19. Because we are our managers for this we are going to go ahead and finish the pull request. This is when we would check the commits made and the files changed and decide that we want to add this to our main branch. 
20. The "Merge pull request" button has a drop down option with the following options:
    1.  Create a merge commit - All commits from this branch will be added to the base branch via a merge commit
    2.  Squash and merge - The 1 commit from this branch will be added to the base branch.
    3.  Rebase and merge - The 1 commit from this branch will be rebased and added to the base branch.
21. Click "Create a merge commit" and click the "Merge pull request" button.
22. Make whatever changes you need to make to the automated commit message and extended descriptions
23. Click "Confirm merge" when done.


---

## OPTIONAL: Homework
1. Exchange Github's profile links with people in WIT (you can add them on Discord or, if you want, you can add me! [https://github.com/rikkitomikoehrhart](https://github.com/rikkitomikoehrhart))
2. Add your friend as a collaborator on your Grab a Byte Repo (via the **Settings > Collaborators**)
3. Create a new branch called "hello-friend"
4. Add a new hello-friend.md file and say hello to your friend
5. Create a pull request and add your friend as a Reviewer and yourself as an assignee
6. Add a comment thanking your friend for their help and then wait for them to complete the request ( or if you are the reviewer for someone else's repo - make a comment telling them hello and confirm the merge!)


---

## Next Up!
Next week we will talk cover resolving merge conflicts! See you then!!

