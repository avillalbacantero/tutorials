# Git Tutorial

This tutorial explains briefly how to use Git, its basics commands, common workflows as well as GitHub.

## What is git?
Git is a version control system used for tracking changes in files and, especially, on code files.

## Why should you use it?
Git allows to mantain a history of the changes and updates that have been made to the code. 
What's more, it allows a team to work collaboratively on the same project.

## What is GitHub?
Although Git and GitHub sound similar, they are different things. 
GitHub is a code **hosting platform**, while Git is used to manage the version control of the files stored on GitHub.

![Git vs. GitHub](https://www.decodingdevops.com/wp-content/uploads/2019/12/git-vs-github-difference.png)

## Remote repository vs. local repository
The remote repository is the one hosted on GitHub. It is unique. 
The local repository is a copy of the remote repository on your local machine. You can edit here the code. Each developer has its own local directory.

Git stores all the commits and all the information in a hidden folder called `.git`.

## Basic Git commands
> Recommendation: Use the **Git Bash** to execute these commands.
1. Cloning a repository: `git clone [url.git]`
2. Track a file: `git add [filename]`. Use `git add .` to track everything.
3. Make a commit: `git commit -m "message" -m "description"`.
4. Push your commit to the remote repository: `git push [remote repository alias] [remote branch]`. Example: `git push [origin] [master]`. Set -u to set up an upstreaming. 
5. Pull the change from the remote repository to your local repository: `git pull [remote repository alias]`. 
6. To link an existing local directory to a remote repository:
  - Initialize the local directory as a git directory: `git init`
  - Link the local directory to the remote directory: `git remote add [remote repository alias] [url.git]`
  - (Optional) List the remote repositories: `git remote -v`

## Branches
On every project, there is going to exist a master branch. This is the main branch. 
Also, it is common to have a development branch too. Both branches are permanent.

The rest of the branches are temporaly. You create a new branch when, for example:
  - You are working on a new feature (feature branch). 
  - You are fixing a bug (hot fix branch). 
 
 ![Branch Example](https://docs.wavemaker.com/learn/assets/branching-model.png#gh-dark-mode-only)

When you create a new branch from master, both contain the same code. 
However, as you make and commit changes into the new branch, these are not going to be in master neither on other branches.
You have to finish your changes and merge them into master/development. 
Typically, each local branch has a remote branch with the same name.

### Git Branches commands
These are the most used commands when working with branches:
1. To look at current branches: `git branch`. Use -a to see remote branches too. The * sign says your current branch.
2. To create and switch to a new branch: `git checkout -b [branch name]`. Typically, names contain things like "feature" "bugfix" or the number of the issue they are solving. 
3. To switch to a branch: `git checkout [branch name]`.
4. To merge a branch into another: from the branch we are merging to, `git merge [branch name being merged]`. For example, `git merge master`.
5. To see the differences between two branches on CLI: `git diff [branch name]`
6. To push the changes to a remote branch: (from the branch to push) `git push origin [branch name]`
7. To delete a branch: `git branch -d [branch name]`

## Merging conflicts
Sometimes two branches have edited the same piece of code. When merging, Git doesn't know what changes it must mantain or discard. So you will have to resolve these conflicts manually, either by selecting the one to keep or by manually editing the code to keep both. 

*master/development* usually are updated frequently since more devs are merging their changes into them. To minimize merge conflicts, it is a good practice to pull master/development changes on your local repository frequently (for example, each day) and merge them into the feature/bug branch you are working on. If there are conflicts, you should fix them by hand, but hopefully there won't be too many. The command to do this operation are:
- (from master) `git pull origin master`
- `git checkout [branch name]`
- (from the feature/bugfix branch) `git merge master`

To solve the merge conflicts, we can use the CLI, GitHub or the code editor (which is the recommended option). 

## Pull Request
A Pull Request (PR) is a request to merge your code to another branch, typically development or master. 
Often, more people will review your code (in a process called **code review**), and they may ask for changes. You can update the code with more commits until the PR is merged. Once this ocurrs, you should **delete your merged branch** (both locally and remotely). This is an iterative process, since to add more functionalities or bug fixes you will be creating a new branch, commiting changes and making PRs...

 ![Creating a Pull Request in GitHub](https://i.ytimg.com/vi/rgbCcBNZcdQ/maxresdefault.jpg)
 
 ![Opening a Pull Request in GitHub](https://david-estevez.gitbooks.io/the-git-the-bad-and-the-ugly/content/assets/github-pr-06.png)

## Common Git Workflows
Typically, you will be doing:
1. Create a new branch, typically from master or development.
2. Editing/writing the code in your local directory.
3. Track the files you have been editing.
4. Commit new changes. These won't appear on the remote repository yet.
5. Push your commits on a remote branch.
6. Make a Pull Request to merge your changes into another branch (typically, master/development). Often, someone else is going to review your code before accepting the PR.
7. Once the PR is accepted and your changes are merged into master/development/another branch, you should delete the created branch.

 ![Typical Git Workflow](https://www.researchgate.net/profile/Mateus-Santos-19/publication/326295010/figure/fig1/AS:646795940069388@1531219577548/GitHub-Pull-request-flow.png)

## Undoing in Git
Git commits and changes to the code can the undone easily. 
1. If you have made a commit but you want to switch back to the previous commit, you can do:
`git reset HEAD~1`, where HEAD = A pointer to the last commit (the one you want to undo)
2. If you want to come back to a specific commit:
`git log`, look for the hash of the commit you want to switch
`git reset [hash of the desired commit]`
3. In case 1 and 2, the changes to the code have been made but **unstaged**. If you want to **completely remove** the changes, do:
`git reset --hard [hash of the desired commit]`

## Forking
To fork a repository means to create a copy of it into your personal GitHub account. For example, you may want to fork the repository of *huggingface/transformers* to add new functionalities, so it will look like *your_account_name/transformers* after forking. 
In your forked repository you can have your own branches, commits or whatever you want. 
To integrate your changes into the original official repository, you have to make a PR and the owners of the original repository have to approve it.  

 ![Forking in GitHub](https://miro.medium.com/max/624/1*IelAxduwS_YtpsrlRe1d0Q.png)


## References
[Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)
