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

You made some changes on project files, first you need 