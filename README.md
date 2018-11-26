## Desktop Automation
All these desktop automations are meant for Linux environments and will use either Bash or Python 3, importing os, shutil etc. Most of whats written in Bash can also be done in Python, with a few programs utilizing both. 
## Motivation
There are countless tasks we do daily that can be automated to save time and our sanity. A lot of these scripts can be used in combination with one another or you can can build a more robust program to fit your needs from them.
## Getting Started
For running the bash files, its best to create and save it on your system so you can call it easily from the terminal for multiple uses. Below I'll explain how to do that for any of the above `.sh` files. The `.py` programs can be executed either in the terminal or using Pycharm/ any IDE you choose.
## Creating a file in the terminal

In the terminal you can create a file to store the command to reuse multiple times.

Enter `touch yourfilename` to create the file. Replace `yourfilename` with whatever name you like.

Next `sudo nano yourfilenmae` to begin editing it. Copy and paste the code from the `.sh` file above that you want.

To save `ctrl o` , then `enter`, finally `ctrl x` to exit

Now we need to move the file to `/usr/bin/` with `sudo mv yourfilename /usr/bin`

Finally we need to change the permission on it so it can be called from anywhere.
Run `sudo chmod +x yourfilename`
## Running the Programs
By now you should've create a bash file containing any one of the scripts above. Simply open your terminal, and enter the name of the file, hit enter and it should run.
