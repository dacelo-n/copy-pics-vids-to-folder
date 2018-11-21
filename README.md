# copy-pics-vids-to-folder
Copy: mp4,mov, flv, png, jpg, and img files from a target folder to a disgnated folder.This is can modified by adding more desired files such as pdf, mp3 or removing others. 

## Creating a file in the terminal

In the terminal you can create a file to store the command to reuse multiple times.

Enter `touch yourfilename` to create the file. Replace `yourfilename` with whatever name you like.

Next `sudo nano yourfilenmae` to begin editing it. Copy and paste the code below.

To save `ctrl o` , then `enter`, finally `ctrl x` to exit

Now we need to move the file to `/usr/bin/` with `sudo mv yourfilename /usr/bin`

Finally we need to change the permission on it so it can be called from anywhere.
Run `sudo chmod +x yourfilename`

### Open the terminal in the folder you wish to copy files from, and copy/paste this code in

### Remove `#!/bin/bash` if you are just using this once, and change `/your/folder/destination` with the path to your folder
```
#!/bin/bash

find . -type f -name "*.mp4" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.mov" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.mwv" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.avi" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.flv" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.png" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.jpg" -print0 | xargs -0 -I {} cp {} /your/folder/destination
find . -type f -name "*.img" -print0 | xargs -0 -I {} cp {} /your/folder/destination
```
