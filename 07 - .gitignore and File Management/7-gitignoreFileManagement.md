# Lesson 7.1: .gitignore and File Management

Welcome to the Grab a Byte Lunchtime Learning Series! This semester we are learning GitHub!

Last week we had a quick review of Pushing and Pull and learned about Upstreams and Rollbacks. This week we are going to learn about the .gitignore File as well as File Management

---

## Table of Contents
- What is a .gitignore File?
  - Purpose of a .gitignore File
- What Files Should You Ignore
- How a .gitignore File Works
- How to Use a .gitignore File
- Difference Between Tracked, Untracked, and Ignored Files
- Best Practices
- OPTIONAL: Homework
- Next Up!

---

## What is a .gitignore File?
A ***.gitignore*** file is a plain text file used in Git repositories to specify intentionally untracked files that ***git*** should ***ignore***.

What this means is that Git will not include these files in commits, nor will it show them as "untracked" when using commands like ```git status```.


### Purpose of a .gitignore File

**It Makes a Clean Repo:**

Prevents temporary files, build artifacts, and IDE-specific files from being tracked, keeping the repository cleaner and more focused on the code you want to share.


**Keeps Secrets Secret!:**

Ensured sensitive information like API keys, secrets, or local configuration files are kept secrets and not committed for the world to see!


**Improved Performance**

By ignoring large, frequently changing files (like libraries and packages) that don't need version control, Git operations can be faster and the repository size smaller.

---

## What Files Should You Ignore?
So, what files should you add to your .gitignore?

  - System files (like ```.DS_Store```, ```Thumbs.db```)
  - IDE/editor files (```.vscode/```, ```.idea/```, ```*.swp```)
  - Build outputs (```/dist```, ```/bin```, ```/obj```)
  - Logs (```*.log```)
  - Secrets (```.env```, **API keys**, **passwords**)

There are tons of .gitignore files out there. You can always Google for a template for the type of project you are doing and see what they suggest!

**NOTE**: Mac users! Mac does add a couple of random files every now and then, its smart to use a Mac .gitignore template to start each of your projects!

---

## How a .gitignore File Works
The .gitignore file contains patterns that match files or directories that git *will* ignore when you commit your project.

These patterns can be specific filenames, wildcards, or directory names. The file is typically placed in the root directory of the repository, but multiple .gitignore files can exist in subdirectories to apply different rules to specific parts of the project.

---

## How to Use a .gitignore File
Create a .gitignore file in your project.

Note how it starts with a period (.) and doesn't have a period (.) + file extension (like .md, .py, etc.) at the end. The file name is specific, if it is misspelled or the punctuation is wrong, it will not work. The same goes for the file patterns that you put in the file.

In the file, you use ```#``` to mark comments like such:

```# This is a comment line```

You use ```*``` as a wildcard character, which is a special symbol used to represent one or more characters in a file or directory name. This allows you to do pattern matching to specify which files or directories should be ignored by Git.


**For Example:**

Say you have a bunch of files like this:
```
unfinished.txt
unimportant.txt
undone.txt
under_construction.txt
finished.txt
important.txt
done.txt
constructed.txt
```
And you want to ignore them but not all the files in the folder, just all the ones that start with "```un```". 

You'd use a wildcard character to accomplish this like:

```un*.txt```


So, lets make a .gitignore file!

Inside the file lets add this comment and file type to ignore:
```
# Ignore all files with a .log extension
*.log
```

Now, in your local directory, in the root, create a file called "```hide.txt```", you can leave it blank. 

Inside your .gitignore add this line:
```
# Ignore specified files
hide.txt
```

Next, create a folder in your root directory called "```temp```" and inside your .gitignore add this line":

```
# Ignore the 'temp' directory
temp/
```

Next create another folder and make the name of it your first name. Inside the folder add a file that is your lastname.txt. Then inside the .gitignore write:
```
# Ignore all files inside your directory but not the directory itself:
rikki/*
```
^ but put your name, not mine, unless your name is also Rikki :)

Finally, create another folder in your root called "```now_you_see_me```" and inside create two files "```and_now_you_dont.txt```" and "```but_youll_see_this_one.txt```"

Inside your .gitignore enter this:
```
# Ignore all files in now_you_see_me except for but_youll_see_this_one.txt
now_you_see_me/*
!now_you_see_me/but_youll_see_this_one.txt
```

Go ahead and do a ```git status``` command and look at the list of files. 

It should look something like this:

```
Untracked files:
    ....
    .gitignore
    now_you_see_me/but_youll_see_this_one.txt
```

if there are other files listed you should check your .gitignore to make sure your spelling is correct.

Once everything is correct, go ahead and add, commit and push. Go to your repo on Github.com and see what folders/files made it online.

---

## Difference Between Tracked, Untracked, and Ignored Files

**Tracked** = Git is watching changes (```git add``` has been run).

**Untracked** = New files Git doesn’t know about yet.

**Ignored** = Files you’ve told Git to not save to the repo.

---

## Best Practices
- *Always* add a .gitignore file early in a project
- Use templates (i.e. GitHub's gitignore templates) and add to them as needed
- Never commit secrets or credentials, put them in separate files (like .env files) and add ignore them
- Keep .gitignore organized and readable. Use comments to block off sections (like technology specific sections or make it match your folder structure). It will help you out so much in the long run.

---

## OPTIONAL: Homework
- Google "basic .gitignore template". Choose one, and type it out in your .gitignore in this project. 
- Practice making files and folders in this project and ignoring them using the .gitignore.


---

## Next Up!
Next time we will be covering Intermediate Collaborations with Issues, Labels, Milestones, and Projects! See you then!