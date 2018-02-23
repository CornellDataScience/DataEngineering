# UNIX/Linux Guide

Please note that the following information is an extremely truncated tutorial, which we expect to provide only the most critical information required to use a Linux machine. For more comprehensive tutorials, please see the Additional Resources section below.

## File system navigation

<br>

![](http://i1.wp.com/mycodinglab.com/wp-content/uploads/2014/01/Linux-File-System-Mycodinglab.jpg) 

All paths to files in a Unix system can be expressed in terms of their relation to the root directory (denoted by ‘/’). For example, to describe a file called text.txt that was stored in a folder called documents in the root directory, we would say /documents/text.txt. Forward slashes delimit folders, in addition to indicating the root directory. You can think of root like you might the C drive top-level folder on a Windows machine.

Note that ‘..’ denotes the parent directory, and ‘.’ denotes the current directory

### Navigation commands

#### cd: Change Directory

Takes either an absolute path (from the root directory down) or a relative path (directions from the current directory), and sets the shell’s directory to that argument. Usage: 'cd DIRECTORY'

#### ls: List (directory contents)

Lists the files and folders/directories present in the current shell’s directory. Usage: 'ls'

#### pwd: Print Working Directory

Prints the absolute path of the current shell’s directory. Usage: 'pwd'

### Modification commands

#### mkdir: Make Directory

Creates a new sub-directory with a provided name in the current directory. Usage 'mkdir \[OPTION\]... DIRECTORY...''

#### mv: Move

Moves a file from one location to another. Usage: 'mv \[OPTION\]... SOURCE DEST'

#### cp: Copy

Copies a file from one locatio to another. Usage: 'cp \[OPTION\]... SOURCE DEST'

#### rm: Remove

Removes a file from the current directory, or removes a subdirectory when the -r flag is specified. Usage: 'rm \[OPTION\]... \[FILE\]...'

## Server Access

Use of the CDS servers will require you to know the following two commands, which are used to interact with remote machines.

#### ssh: Secure Shell

Provides command line access to a remote server.

To connect to the CDS master node (located at 128.84.48.178), use:
```
ssh [username]@128.84.48.178
```
where \[username\] is your subteam username. You may use an alias set in /etc/hosts in place of the IP address if you choose to set one up.


#### scp: Secure Copy

Copies a file or directory between a local and remote server. 

To copy a file called 'text.txt' in the current working directory to a folder called 'temp' in your home directory on the server, use:
```
scp test.txt [username]@128.84.48.178:temp
```

To copy a folder called 'myfolder' in the current working directory to a folder called 'temp' in your home directory on the server, use:
```
scp -r myfolder [username]@128.84.48.178:temp
```

To copy a file called 'text.txt' in the folder mydata on the remote server to a to the current working directory, use:
```
scp [username]@128.84.48.178:mydata/test.txt .
```

To copy a folder called 'mydata' in your home directory on the remote server to a to the current working directory, use:
```
scp -r [username]@128.84.48.178:mydata .
```

## Piping

Output piping is a core feature of the Bash shell that allows you to use the output of one commmand as the input for another (hence, "piping"). Accomplished using the '|' character in the following configuration:

```
[command1] | [command2]
```
In this case, the output of command1 is provided as input for command2.

This construction probably doesn't seem very useful for the small set of commands we've covered so far (for more, see the Additional Materials section's Bash command basics link), but is is a very powerful tool when used in conjunction with a larger library of available functions. For example, the [grep](https://www.gnu.org/software/grep/manual/grep.html) command allows you to find lines that contain a particular string in some set of input lines. This functionality can allow you to easily check if a file named 'text' is present in the current directory using the command:
```
ls | grep text
```

## Redirection

On a Linux system, most programs started on the command line output on two channels: STDOUT (standard output) and STDERR (standard error), both of which are displayed in the terminal when a program prints to them. To suppress or record this output (useful for programs that produce a lot of log messages, for example), you can execute the program and redirect outputs to a file for examination later.

For example, if we have a program in the current directory called 'myprogram', you could:
*   Redirect just STDOUT: 
  ```
  ./myprogram > out.txt 
  ```
*   Redirect just STDERR
  ```
  ./myprogram 2> errors.txt 
  ```
*   Redirect both STDOUT and STDERR
  ```
  ./myprogram 2>&1 log.txt 
  ```
Conversely, you also may want to redirect the contents of a file into a program that normally accepts interactive text input. If we have 'myprogram' as previously, and a file 'inputs.txt' you can do the following:
```
./myprogram < inputs.txt
```
to convert the lines contained in the file into inputs that are passed to the program.

## Vim

Vim (Vi Improved) is a command line text editor, which you will likely need in order to edit configuration files and programs remotely. To edit a file called 'text.txt' in the current directory with vim, type:

```
vim text.txt
```
Note that if the file 'text.txt' does not exist, a new file will be created with that name when you save.

Vim has two modes that are relevant here: command mode and editing mode. When vim starts, it is in command mode, which we will discuss later. To start editing the file as you normally would, with arrow-key navigation and text input, press 'a' (append) or 'i' (insert). This will switch your vim session into editing mode, and allow you to make changes normally. To access more advanced functionality, such as undo, redo, save, and exit, you will have to switch back into command mode. This can be accomplished at any time by pressing the ESC key. In command mode, vim will respond to keyboard input as instructions, rather than text to add to the file. A few useful commands are listed below.

*   'a': append (switches to editing mode)
*   'i': insert (switches to editing mode)
*   'u': undo last change
*   'CTRL+r': redo (undo last undo)
*   ':w': write file (save current state of the file)
*   ':q': exit vim (will give a warning if you have unsaved changes)
*   ':!q': exit vim, overriding unsaved changes warning
*   ':wq' or ':x': save file and exit vim

Note that when entering commands that begin with ':' you should enter a ':' character while in command mode, which will allow you to edit a text command, which is executed when you press ENTER. For example, to save and exit a vim session in editing mode, you would press ESC to enter command mode, enter ':' (SHIFT+;) to allow line input, type either 'wc' or 'x', and press ENTER.

## More Bash Commands

Some additional commands:

sort: sorts the text in the file
uniq: displays only the unique lines in the text
wc: counts the number of words in the input
more: will display the file up to the point that fits onto the terminal screen
grep: will search lines with the given input string pattern.
less: similar to more but allows more flexibility in navigating forward and backward. It also does not require the linux kernel to read the entire file, which makes the reading more efficient 
tr: transforms string input to another output. tr ‘\[a-z\]’ ‘\[A-Z\]’ capitalizes all characters,

## Additional Resources

*   [Lecture slides for CS 2043: UNIX Tools and Scripting (sadly not currently offered)](https://cs2043-sp16.github.io/schedule.html)
*   [A Bash language and scripting tutorial](http://www.bash.academy)
*   [The Bash Guide for Beginners](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/)
*   [Bash command basics](https://www.unr.edu/it/research-resources/research-computing/hpc/the-grid/using-the-grid/bash-commands)
*   [Vim Cheat Sheet](https://vim.rtorr.com/)
*   [Interactive Vim tutorial](http://www.openvim.com)
*   [Comprehensive Vim tutorial](https://linuxconfig.org/vim-tutorial)

