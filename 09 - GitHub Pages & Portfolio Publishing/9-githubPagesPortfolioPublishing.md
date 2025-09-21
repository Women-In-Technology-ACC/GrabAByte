# Lesson 9.1: GitHub Pages & Portfolio Publishing

Welcome to the Grab a Byte Lunchtime Learning Series! This semester we are learning GitHub!

Last week we learned more about collaboration with Issues, Labels, Milestones, and Projects. This week we learn about GitHub Pages and Publishing a Portfolio

---

## Table of Contents
- What is a Static Website?
- Introduction to GitHub Pages
- How to Publish on GitHub Pages
- OPTIONAL: Homework
- Next Up!

---

## What is a Static Website?
A static website displays static content, as in fixed HTML, CSS, and JavaScript. The content remains the same for every visitor unless a developer manually updates the source code. They are ideal for portfolios, resume sites, company info pages and documentation.

Dynamic pages use server-powered content. For beginners and for our purposes, static sites are simpler, easier, and perfect!

---

## Introduction to GitHub Pages
GitHub offers a free static site hosting service called GitHub Pages. It allows users to publish websites directly from a GitHub Repository. It takes HTML, CSS, and JavaScript files from a repo and publishes them as a live static website.

---

## How to Publish on GitHub Pages
We are going to publish an example portfolio website code created by our very own [Brittany Sifford](https://github.com/BrittanySifford)! She created this excellent [example portfolio](https://github.com/BrittanySifford/example-wit) that she has provided for free for you to use, edit, add to, etc. 

I have already downloaded the files (from [Brittany's repo](https://github.com/BrittanySifford/example-wit), click the "<> Code" button and select "Download ZIP"). I've moved the files into the "09-GitHub Pages & Portfolio Publishing" folder. Its the folder called "example-wit-main". 

1. First, you'll want to move all the files and folders inside the "example-wit-main into the main root of your GAB repo.
2. Make sure you run the ```git add .```, ```git commit -m``` with a message about moving the files and ```git push```. So that it appears in your GitHub repo.
3. Login to GitHub and go to your GAB Repo.
4. From the top menu, go to "Settings" (which is the last one)
5. In the left hand menu, in the "Code and automation" section select "Pages"
6. We are going to Deploy from a branch, so you can leave that section as is
7. In the next section, it is asking which branch we are deploying from, select the branch you are in (the one where you moved all the files into the root)
8. The next drop down is choosing the folder (the root folder or the /docs folder) we are using the root folder, so you can leave it as is.
9. Click save.

It can take several minutes for the page to deploy.

While we wait, here is a couple of things to think about when using GitHub Pages:
- Ensure your website is static (HTML, CSS, and JavaScript)
- Include an ```index.html``` file as the main landing page
- You can also deploy using a custom GitHub Actions workflow. We'll talk more about workflows next time
- After your deploy, you can make updates to your site by updating the repository, commit and push these changes. GitHub Pages will *automatically rebuild and redeploy your site* with the latest changes.



Once it deploys the URL for your static page is:
```
https://your-user-name.github.io/your-repo-name
```


---

## OPTIONAL: Homework
Create a new repo, download the files from [the example portfolio repo created by Brittany](https://github.com/BrittanySifford/example-wit) and edit it with your own projects and such. Publish it on Github pages in your new repo and make sure it works.

---

## Next Up!
Next we will be talking about Workflows, best practices and more!
