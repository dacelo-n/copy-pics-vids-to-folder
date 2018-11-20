# copy-pics-vids-to-folder
Copy  .mp4, .mov, .mwv, .flv, .png, .img and .jpg files from a target folder to a disgnated folder.

 make sure to replace destination folder with your own path
## Creating a file in the terminal

In the terminal you can create a file to store the command to reuse multiple times.

Enter `touch yourfilename` to create the file

Next `sudo nano yourfilenmae` to begin editing it. Copy and paste the code below.

To save `ctrl o` , then `enter`, finally `ctrl x` to exit

Now we need to move the file to `/usr/bin/` with `sudo mv yourfilename /usr/bin`

Finally we need to change the permission on it so it can be called from anywhere.
Run `sudo chmod +x yourfilename`

## Open terminal in folder you wish to copy files from
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
