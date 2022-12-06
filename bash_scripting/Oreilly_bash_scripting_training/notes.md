# Linux Bash Scripting training
O'Reilly Training - Oct. 27, 2022

Instructor: Sander van Vugt (mail@sandervanvugt.nl)
[Github page](https://github.com/sandervanvugt/bash-scripting)
 
---

## Variables
Variables are **only local to the current terminal** - once the shell is closed, variables are removed.
To make global shell variables, use `export`

---

## Exit codes
Exit codes give more information about the status of your shell code
* 0 = success
* anything other than 0 = failure

`echo $?` - get the status of the last command that was run

---

## Bash vs. other shells
`Bash` = "born-again shell". It is the default shell in Linux and is the remake from the "born shell" in Unix (`sh`)
The "born shell" is **always available** - bash is not always available depending on the system.
<br />

Another common shell is `zsh` which is the default on MacOS.
<br />

If you are writing shell scripts, **bash is the standard**, but there are some environments where bash might not be available like **linux in containers** or anywhere where very small linux instances are desired.

---

## Shell scripts
Shell scripts are the same as Python or C++ or any other programming language - except they are interpreted by a shell - not a language interpreter.

To ensure that bash scripts are interpreted correctly, we start bash scripts with `#!/bin/bash` - this is just telling the born shell which interpreter to use (called the `shebang`).

---

## script file extensions
Linux or unix systems do not require file extensions for scripts, **BUT** it's good practice to use `.sh` as this makes it clearer what file type it is.

---

## Internal commands vs. external commands
* internal commands = commands which are only available in the shell (faster)
* external commands = commands which are in another directory / using another service (including more functionality)

```
# See which commands are internal or external
type ls
type man
type echo
```

---

## Quotes & character escaping
`"` double quotes allow you to have values which have whitespace `echo "this is my $SHELL`
`'` single quotes denote that everything should be literal and not interpreted
`\` backslashes allow you to escape single characters

```
echo "this is my $SHELL"
echo 'this is my $SHELL'
echo this is my \$SHELL`
echo the value of \$SHELL is $SHELL
```

---

## Arguments vs. options
`ls -l /bin/bash`

* ls = command
* -l = option (additional or changed functionality)
* /bin/bash = argument (required input)

---

## Bits of code

`env` print variables
`echo $USER` print out **user** variable

However, a better way to get variables is to use **curly braces {}** - because it is more specifically telling bash that you're referencing a variable:
`echo ${USER}`

---

`key=value` assign **local** value to variable
`export key=value` assign **global** value to variable

---

`chmod +x myscript` make shell scripts executable (set execute permissions)
`bash myscript` - lets you run any scripts without changing execute permissions, but is less flexible

---

`# this is a comment` hash marks denote comments 

---

`echo $PATH` list directories where the shell is looking for files
Note: adding script files to `usr/local/bin` - then ALL users of the system can use the script

---

`cat myscript.sh` print out the script