# Setup

## Repo base
```
Last login: Thu Jul 29 22:05:17 on ttys000
MacBook-Pro-de-Alexandre:~ alexandre.c.sousa$ cd Documents/learning
MacBook-Pro-de-Alexandre:learning alexandre.c.sousa$ git clone https://github.com/alexandredesousa/everis_python_exercise.git
Cloning into 'everis_python_exercise'...
warning: You appear to have cloned an empty repository.
MacBook-Pro-de-Alexandre:learning alexandre.c.sousa$ cd everis_python_exercise
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ touch README.md
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ git add README.md
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ git commit -m "add README"
[master (root-commit) 8fe364b] add README
 Committer: alexandre.c.sousa <alexandre.c.sousa@MBPdeAlexandre.lan>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ git push -u origin master
Counting objects: 3, done.
Writing objects: 100% (3/3), 221 bytes | 221.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/alexandredesousa/everis_python_exercise.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ git checkout -b as_dev
Switched to a new branch 'as_dev'
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ mkdir src
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ mkdir docs
```

## Python env
```
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ python3.7 -m venv venv
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ . venv/bin/activate
(venv) MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ python --version
Python 3.7.9
(venv) MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ deactivate
MacBook-Pro-de-Alexandre:everis_python_exercise alexandre.c.sousa$ 
```