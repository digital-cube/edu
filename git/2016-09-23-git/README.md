LESSON 2 Appendix
=================

Git introduction
----------------

- Cloning (checkout) repository
- Configure user information
- Make changes
- Branching
- Gitignore
- Sync changes

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
- Active Directory
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

When finish creating new or editing current files, First you must add them first to prepare for commit:

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

Branching means that you can separete from main line(master branch) of developement and continue to do work on you branch without messing with that master line.
