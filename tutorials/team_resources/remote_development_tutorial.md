## Remote Development with VSCode and rmate

# USE THE REMOTE - SSH extension by Microsoft

You can continue to use the method outlined below, but Microsoft has made a convient plugin that requires no server side software. This plugin is better.
-- -- -- 
This tutorial is for remote development with ssh pipelining on the CDS server with rmate. As we encourage more and more development on the CDS server `128.84.48.178`, the choice of development platform becomes more of an issue. So far we have either been developing remotely and then pushing to the server for deployment/testing, or developing directly on the server with vim. This is fine, but presents problems if you don't know VIM and increases development time if there's no need to seperate testing/deployment from development, as is the case in some CDS projects. 

You can continue to use VIM if you are familiar with that and are happy with that. This guide is suited for people who don't want to learn VIM and want to keep using an IDE for development. 

rmate is a remote pipeline utility that was originally used for the editor "TextMate", this is how you can use it with the more popular vscode. 

### Setting up Remote VS Code

In vscode open the command pallete (Ctrl-Shift-P) and search for `Install Extensions`. Search for the "Remote VSCode" extension by "Rafael Maiolla" and install it. 

#### Using Remote VS code
Open the command pallete (Ctrl-Shift-P) and search for `Start Server`, press enter.
Open the terminal, perferably the internal vs code terminal and type the following command:
```unix
>ssh -R 52698:127.0.0.1:52698 serverteam_1@128.84.48.178
```
Substitute serverteam_1 with the appropriate username, if you aren't on DE.

This opens up an SSH connection and an ssh pipline on port 52698 to your machine. This allows you to use rmate to pipline files from the server to your editor, and perform remote development. If the port is busy, you may need to use a different port, no issue. 

Log in as you would normally, (you should ideally have your ssh public key added to the server to make this easier). Navigate to any file you wish to edit within the filesystem

Then you can use the following command to open it

```unix
>rmate -p 52698 <filename>
```
This piplines <filename> through port 52689, if you used a different port, use that one. 

Now the file should open in vscode and you should be able to edit it normally. You can run it in the terminal as if you are on the server, because you are on the server. Saving should save directly to the server. This is the benefit of the rmate pipline. You can develop in your native environment, but execute on the server. 
