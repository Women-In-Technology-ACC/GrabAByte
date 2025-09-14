# Lesson 5.1: Resolving Conflicts

Welcome to the Grab a Byte Lunchtime Learning Series! This semester we are learning GitHub!

Last week we continued learning Collaboration Basics. This week we are going to go over Resolving Merge Conflicts.

---

## Table of Contents
- Merge Conflicts
  - How Do They Happen?
- Lets Create a Conflict
  - Git Conflict Markers
- Resolving the Conflicts
- Tips to Avoid Conflicts
- OPTIONAL: Homework
- Next Up!


---

## Merge Conflicts
A merge conflict happens when Git is unable to automatically reconcile differences between changes made on two different branches that are being merged.

When a merge conflict happens, Git pauses the merging process and flags the conflicted files for manual review. The reviewer must then decided how to resolve the discrepancies.



### How Do They Happen?
- Same lines edited differently
  - Two or more developers modify the exact same lines within the same file in different ways on separate branches
- File deletion vs. modification
  - One branch deletes a file, while another branch modifies the same file.
- Conflicting file structure changes:
  - Changes in one branch alter the file structure or relationships in a what that conflicts with changes made in another branch

---

## Lets Create a Conflict
...on purpose!


1. Create a new branch called "conflict-branch"
2. Go to your main branch. 
3. Go to this file (5-ResolvingConflicts.md) and go to the spot below these instructions labeled "CONFLICT HERE".
4. Write this line: "This is the conflict from the main branch" 
5. Commit and Push
6. Go to the conflict-branch and go to this file (5-ResolvingConflicts.md) and go to the spot below these instructions labeled "CONFLICT HERE"
6. Write this line: "This is the conflict from the conflict-branch"
7. Commit and Push
8. Create a Pull Request and see the conflict appear. Observe how it looks.

#### CONFLICT HERE

⸻

### Git Conflict Markers
9. Click on the Resolve Conflicts button
10. It should look something like this:

```
<<<<<<< conflict-branch
This is the conflict from the conflict-branch
=======
This is the conflict front the main branch
>>>>>>> main
```

---

## Resolving the Conflicts
It acts as a text editor so you literally can edit the text and save.

Lets remove these lines:
```
<<<<<<< conflict-branch
=======
>>>>>>> main
```

and keep the rest so it looks like this:
```
This is the conflict from the conflict-branch
This is the conflict front the main branch
```

Click on the "Mark as resolved" button when done and then on the green "Commit merge" button after that.


It should take you back to the Pull Request. Since we are done, lets go ahead and click on the "Merge pull requests"

---

## Tips to Avoid Conflicts
- Pull often before making changes and always pull first thing in the morning and first thing coming back from lunch when working on big teams!
- Communicate with team about which files are being worked on
- Work on smaller branches/features
- Use code reviews to catch overlap early!


---

## OPTIONAL: Homework
Switch between your main branch and conflict-branch making different answers to the questions below and then do a Pull Request and handle the merge conflict.


1.	If you had a personal robot assistant, what’s the first chore you’d make it do for you?


**ANSWER**:



2.	Would you rather fight one horse-sized duck 🦆 or 100 duck-sized horses 🐴?


**ANSWER**:



3.	What’s your “comfort food” that instantly makes a bad day better?


**ANSWER**:



4.	If you could download one skill into your brain Matrix-style, what would it be?


**ANSWER**:



5.	What’s your favorite way to celebrate a small win? (cake, naps, dance party, other?) 🎉


**ANSWER**:




---

## Next Up!
Next week we will go more in dept with pushing, pulling, and staying in sync! We'll also look at how we would revert to a previous commit if we need to!