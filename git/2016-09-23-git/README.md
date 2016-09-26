LESSON 2 Appendix
=================

Git introduction
----------------

- Cloning (checkout) repository
- Configure user information
- Make changes
- Branching
- Create a remote branch
- Git ignore
- Sync changes
- Conflict resolving

Cloning repositorium
--------------------

To obtain files(for example. some project) from repository using URL( copy from github or other).
Directory and project files will be downloaded in path you are currently in.

```bash
$ git clone URL
```

Configure user information
--------------------------

Before your first commit you must set name and email that you want to attach to your commmits.
Name and email are the one that you registered (for example to GitHub) with.

```bash
$ git config --global user.name "[name]"
$ git config --global user.email "[email address]"
```

Make changes
------------

Git is based on three tier structure:
- Repository
- Working Directory
- Local

![alt tag](https://raw.githubusercontent.com/digital-cube/edu/master/git/2016-09-23-git/git.png)


After you made some changes on project files, you can see all new or modified files that need to be commited:

```bash
$ git status
```

You can see differences in exact files on local and cloud repository:

```bash
$ git diff
```

When finish creating new or editing current files, you must add them first to prepare for commit:

 ```bash
$ git add [file]
 ```

If you want to revert changes made in local files:

```bash
$ git checkout [file]
```

When are all files added and changes ready, by commiting files are permanently saved in git version history:

```bash
$ git commit -m "[descriptive message]"
```

Branching
---------

Branching means that you can separate from main line(master branch) of development and continue to do work on you branch without messing with master line.
You can make multiple branches for and work simultaneously on different features on project. To list all local branches and see in which branch you are currently (marked with *):

```bash
$ git branch -a
```

To create new branch:

```bash
$ git branch [branch-name]
```

To switch to the specific branch and update the working directory:

```bash
$ git checkout [branch-name]
```

To merge changes on specified branch to current branch:

```bash
$ git merge [branch]
```

To delete specific branch:

```bash
$ git branch -d [branch-name]
```
Create a remote branch
----------------------
Remote references are references (pointers) in your remote repositories, including branches and tags.
You can get a full list of remote references explicitly with:

```bash
$ git ls-remote [remote]
```

or for remote branches as well as more information:

```bash
$ git remote show [remote]
```

Git ignore
----------

You can exclude some files like tempory files, paths, configs, logs hidden etc. from commit-ing. You need to add them in file named .gitignore in root project path(example):

```bash
# local settings
*settings.py

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# backup files
*~

# IntelJ files
.idea/

```

Sync changes
------------

To download latest version of project uploaded on repository and incorporate your changes:

```bash
$ git pull
```

To upload all local branch commits to repository:

```bash
$ git push
```

Conflict resolving
------------------

If multiple users commit changes on same files, git will try to merge files, and if it fail, you have to do it manually. You can check which file have merge
conflicts with 'git status'. Conflicts in file are marked with line breaks (\<\<\<, \>\>\>, \=\=\=) and to resolve conflict you must edit lines that git have trouble merging.
This mean to save just version of code you want to be saved, and discard unwanted changes.

After succesfull editing, Before commit resolve conflict file you must:

```bash
$ git add [edited file]
$ git commit
$ git push
```
