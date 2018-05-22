# Server Login Tutorial
CDS has several servers, the most important of which are `master` and `gpu1`. This document explains how to log into them. For first time setup, be sure to read the corresponding section.

Reminder: exercise caution when modifying system files. If you require help, please contact Haram Kim.

## Login Procedure

As a member of CDS your work on the servers will fall under the account associated with your project/subteam. This classification determines the account that you should use to login (i.e. a Data Visualization member also on Genomics should log in using the DV account for DV work, and the Genomics account for Genomics work).

The team-username mappings are given below:
* Data Engineering: serverteam_1
* Data Visualization: datavis_1
* Deep Learning: deeplearning_1
* Algorithmic Trading: algo_1
* Kaggle: kaggle_1
* Genomics: genomics_1
* Research/Yelp: yelp_1

The CDS Servers are hosted at the following locations:
* 128.84.48.178: master
* 128.84.48.177: slave-1
* 128.84.48.179: slave-2
* 128.84.48.180: slave-3
* server.ryanjbutler.com: gpu1

The syntax for logging in is as follows, with \[username\] replaced by the username for your team and \[servername\] replaced with the ip address or domain name of the server you want to connect to:
```
ssh [username]@[servername]
```
For example, a deep learning member connecting to `gpu1` would issue the following command:
```
ssh deeplearning_1@gpu1
```
Use ssh-keys to log in. If you need to, passwords will be provided by your team lead or PM. If you do not have one, please contact him/her.

This will provide you with remote terminal access to the server. From there you can use Bash commands to manipulate files and run programs.

## PySpark
You can start a Jupyter notebook for PySpark using the command:
```
pyspark_yarn
```
Be aware that this command will provide a URL similar to the following:
```
http://localhost:8888/?token=123456789123456789123456789123456789123456789123
```
This URL will not work if you paste it directly into your browser. You must first replace the "localhost" text with the server IP address (128.84.48.178, or master if you have aliased the IP in /etc/hosts).

## Accessing Cockpit
You can also access the cockpit monitoring system using your team account. To do this, connect to https://128.84.48.178:9090.

# First time setup
The first time you want to log into the server, there are several steps to take to ensure that it will be as easy as possible to connect in the future. You will only have to do this once, so follow the instructions carefully and things will be easy in the future.

## Getting SSH
You will first need to install SSH. On linux this is easy, on mac its pretty easy, and on windows its kinda hard. You should google how to do this - but whichever version you install, make sure that it is version 7.3 or later! Otherwise you won't easily be able to connect to the GPU servers. You can check your ssh version with `ssh -V`. On Ubuntu 16.04, the default version is 7.2 so you will have to either upgrade ssh or just install the latest LTS version of Ubuntu, Ubuntu 18.04, which comes with 7.6 by default.

## The hosts file
When you type `www.google.com` into your browser's URL, that request gets sent to a "Domain Name System" (DNS) server, which turns it into an ip address, like `172.217.19.238`.  That ip address is the real address of google's server, and is what the internet actually uses to communicate. Remembering it is hard for humans, which is why DNS lookups are nice.

The [hosts](https://en.wikipedia.org/wiki/Hosts_(file)) file is a file on your computer that can override such DNS lookups or provide custom ones. It is what will allow us to avoid having to remember the ip addresses of the CDS servers. It is located at `/etc/hosts` on Linux and Mac, and `C:\Windows\System32\drivers\etc\hosts` on Windows. The format is the ip address, followed by spaces or tabs, and then the domain name to map to that ip address.

You will need to add the mappings for `master`, `slave-1`, `slave-2`, and `slave-3` to your hosts file, which will allow you to use the domain names instead of IP addresses while logging in. Note that the gpu server cannot be added to the hosts file because it is not a mapping from domain name ip address. We will get around this later.

Your hosts file may look something like this:
```
# This is a comment, localhost is the name that refers to your own computer
127.0.0.1       localhost

# The following are CDS servers
128.84.48.178   master
128.84.48.177   slave-1
128.84.48.179   slave-2
128.84.48.180   slave-3
```

## SSH Keys
Normally when you ssh into a server, you have to enter in the password associated with the account you are connecting with. This is both insecure and cumbersome. A better system is to use SSH keys. SSH keys use a public-private key exchange system called [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) to securely connect. An RSA key consists of a public key and a private key. The public key, usually stored in `~/.ssh/id_rsa.pub` on your computer, is what you place in servers' `~/.ssh/authorized_keys` file. It provides a way for anyone to identify you, and your private key remains secure even when distribuiting your public key across the internet. Your private key, usually stored in `~/.ssh/id_rsa` on your computer, will be used to actually verify you are who you say you are. You should never share the private key with anyone else, and it is usually encrypted by its own password to keep hackers from using it even if they copy it off of your computer.

SSH keys mean that as long as you can access the unencrypted private key on your computer, you can easily log into any server that has your public key. This will be useful for us because it will allow us to avoid having to enter our password every time we try to do something. It also means you can use your public key for multiple things at once - for example, you can [put your public on github](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/) and on the server too. The only password you will need to remember will be password encrypting your private key, if it exists.

### Generating an SSH key if you don't already have one
Your SSH keys will be stored in `~/.ssh`. If you see `id_rsa` and `id_rsa.pub` there already, skip to "Putting keys on the server".
To make your first ssh key, follow [these instructions](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows). Be sure to select a secure password! Once you finish, you should see both the public and private keys in `~/.ssh`. 

As an additional optional step to take if you're not on Linux, you might want to [configure SSH-agent](https://help.github.com/articles/working-with-ssh-key-passphrases/) to remember your private key after you enter your password once. SSH-agent is a process that runs and will safely store a secure version of your private ssh key after you have unencrypted it at least once with your password. If you don't have SSH-agent set up, you will still have to enter your password every time you commit in git or connect to the server, which is annoying. The way you enable ssh-agent depends a lot on whether you're on mac or windows and if you are using the built in command line or another application. This might take some googling to figure out.

### Copying public key to the server(s)
Any server that you anticipate that you will need to log in to, you must put your public key into the server's `~/.ssh/authorized_keys` file. To easily do this, first ensure you have the ssh keys generated. Then run the following:
```
ssh-copy-id [username]@[servername]
```
Where \[username\] is your team's username and \[servername\] is the server you want to put the key on. You can test it by trying to ssh into the server again with the `-v` option and seeing if it uses your key or not.

## Configuring your ssh config file
To further ease your ability to connect with the servers and also enable you to connect with secondary servers like `gpu1`, you must configure your ssh settings further. Your [config file](https://linux.die.net/man/5/ssh_config) is located at `~/.ssh/config` (or wherever the ssh folder is on windows).

First lets set up the necessary settings to connect to `gpu1`. Because the GPU server is firewalled off from people off-campus (even when using the VPN), we have to to a "multi-hop ssh". Basically, we can't get to `gpu1` from our computer, but `master` can ssh into `gpu1`, so if we ssh into `master` and then ssh into `gpu1` that will enable us to connect. However, running two ssh commands just to connect to `gpu1` is annoying, so there is a better automatic way. We will use the `ProxyJump` option to tell ssh to use `master` as the first hop on the path to `gpu1`. This option only became available in ssh version 7.3, so if you are running a prior version, either update or figure out [an alternative method](https://superuser.com/a/170592). We also want to be able to connect to `gpu1` rather than the actual address which is `server.ryanjbutler.com` for convenience purposes, so to do so we will use the `HostName` option:
```ssh_config
Host gpu1
  HostName server.ryanjbutler.com
  ProxyJump [username]@master
```
Now, lets set up some ease of life settings. Whenever using programs that open GUI windows, you can actually get those on your own computer through [X11 Forwarding](https://kb.iu.edu/d/bdnt). We also want to set up SSH agent forwarding so that you don't need to unecessarily re-enter your ssh private-key password. Finally, we can avoid typing in a username by providing a default username to connect with. The following is what a Deep Learning user might set their `~/.ssh/config` file up as:
```ssh_config
Host gpu1
  HostName server.ryanjbutler.com
  ProxyJump master

Host gpu1 master slave-1 slave-2 slave-3
  User deeplearning_1
  ForwardAgent yes
  ForwardX11 yes
  ForwardX11Trusted yes
```
That will make things as easy as possible - connecting to gpu1 will only require you to run `ssh gpu1` as the command.
