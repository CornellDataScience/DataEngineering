# Server Login Tutorial

## Server Addresses
CDS Servers are hosted at the following addresses:
* 128.84.48.178: master
* 128.84.48.177: slave-1
* 128.84.48.179: slave-2
* 128.84.48.180: slave-3

If you are using Linux or OSX, you might consider adding these mappings to your /etc/hosts file, which will allow you to use the text aliases instead of IP addresses while logging in. Reminder: exercise caution when modifying system files. If you require help, please contact Haram Kim or Dae Won Kim.

For your purposes, only the master node is relevant, as it is the portal for access to the spark cluster.

## Login Procedure

As a member of CDS your work on the servers will fall under either a project or domain team. This classification determines the account that you should use to login (i.e. a Data Visualization member also on Genomics should log in using the DV account for DV work, and the Genomics account for Genomics work).

The team-username mappings are given below:
* Data Engineering: serverteam_1
* Data Visualization: datavis_1
* Deep Learning: deeplearning_1
* Algorithmic Trading: algo_1
* Kaggle: kaggle_1
* Genomics: genomics_1
* Research/Yelp: yelp_1

The syntax for logging in (with \[username\] replaced by the username for your team) is as follows:
```
ssh [username]@128.84.48.178
```
Or, assuming a properly configured /etc/hosts:
```
ssh [username]@master
```

Passwords will be provided by your team lead or PM. If you do not have one, please contact him/her.

This will provide you with remote terminal access to the master server. From there you can use Bash commands to manipulate files and start a Jupyter notebook using the command:

```
pyspark_yarn
```

Be aware that this command will provide a URL similar to the following:
```
http://localhost:8888/?token=123456789123456789123456789123456789123456789123
```
This URL will not work if you paste it directly into your browser. You must first replace the "localhost" text with the server IP address (128.84.48.178, or master if you have aliased the IP in /etc/hosts).

## Accessing Cockpit

You can also access the cockpit monitoring system using your team account. To do this, connect to the following address: [link](https://128.84.48.178:9090)*.

Plain text form: https://128.84.48.178:9090
