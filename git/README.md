# Git Tutorial

This tutorial explains briefly how to use Git, its basics commands, common workflows as well as GitHub.

## What is git?
Git is a version control system used for tracking changes in files and, especially, on code files.

## Why should you use it?
Git allows to mantain a history of the changes and updates that have been made to the code. 
What's more, it allows a team to work collaboratively on the same project.

## What is GitHub?
Although Git and GitHub sound similar, they are different things. 
GitHub is a code hosting platform, while Git is used to manage the version control of the files stored on GitHub.

## Remote repository vs. local repository
The remote repository is the one hosted on GitHub. It is unique. 
The local repository is a copy of the remote repository on your local machine. You can edit here the code. Each developer has its own local directory.

Git stores all the commits and all the information in a hidden folder called .git.

## Basic Git commands
Recommendation: Use the Git Bash to execute these commands.
1. Cloning a repository: ```git clone [url.git]```
2. Track a file: ```git add [filename]```. Use ```git add .``` to track everything.
3. Make a commit: ```git commit -m "message" -m "description"```.
4. Push your commit to the remote repository: ```git push [remote repository alias] [remote branch]```. Example: ```git push [origin] [master]```. Set -u to set up an upstreaming. 
5. Pull the change from the remote repository to your local repository: ```git pull [remote repository alias]```. 
6. To link an existing local directory to a remote repository:
6.1 Initialize the local directory as a git directory: ```git init```
6.2 Link the local directory to the remote directory: ```git remote add [remote repository alias] [url.git]```
6.3 (Optional) List the remote repositories: ```git remote -v```

## Branches
On every project, there is going to exist a master branch. This is the main branch. 
Also, it is common to have a development branch too. Both branches are permanent.

The rest of the branches are temporaly. You create a new branch when, for example:
- You are working on a new feature (feature branch). 
- You are fixing a bug (hot fix branch). 

When you create a new branch from master, both contain the same code. 
However, as you make and commit changes into the new branch, these are not going to be in master neither on other branches.
You have to finish your changes and merge them into master/development. 

## Common Git Workflows
Typically, you will be doing:
1. Create a new branch, typically from master or development.
2. Editing/writing the code in your local directory.
3. Track the files you have been editing.
4. Commit new changes. These won't appear on the remote repository yet.
5. Push your commits on a remote branch.
6. Make a Pull Request to merge your changes into another branch (typically, master/development). Often, someone else is going to review your code before accepting the PR. New commits can be made on this step.
7. Once the PR is accepted and your changes are merged into master/development/another branch, you should delete the created branch.

