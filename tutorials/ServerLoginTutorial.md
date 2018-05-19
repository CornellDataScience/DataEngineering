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

## The hosts file
When you type `www.google.com` into your browser's URL, that request gets sent to a "Domain Name System" (DNS) server, which turns it into an ip address, like `172.217.19.238`.  That ip address is the real address of google's server, and is what the internet actually uses to communicate. Remembering it is hard for humans, which is why DNS lookups are nice.

The [hosts](https://en.wikipedia.org/wiki/Hosts_(file)) file is a file on your computer that can override such DNS lookups or provide custom ones. It is what will allow us to avoid having to remember the ip addresses of the CDS servers. It is located at `/etc/hosts` on Linux and Mac, and `C:\Windows\System32\drivers\etc\hosts` on Windows. The format is the ip address, followed by spaces or tabs, and then the domain name to map to that ip address.

You will need to add the mappings for `master`, `slave-1`, `slave-2`, and `slave-3` to your hosts file, which will allow you to use the domain names instead of IP addresses while logging in. Note that the gpu server cannot be added to the hosts file because it is not a mapping from domain name ip address. We will get around this later.

Your hosts file may look something like this:
```
127.0.0.1       localhost
128.84.48.178   master
128.84.48.177   slave-1
128.84.48.179   slave-2
128.84.48.180   slave-3
```
