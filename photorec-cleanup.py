import shutil
import os
# This program is meant to separate files recovered after using Photorec. In order to separate out the file types you
# want from the possibly thousands recovered after Photorec finishes its scan, it's best to save all the 'recup'
# folders produced by Photorec into one folder; preferably on the Desktop.
# Folders for each file type will be made, and store said files.
# The remaining folders can then be deleted at then end.
# Warning ::::: if you run this program in '/' or the recup folders are in 'home', you run the risk or moving
# all the searched file types from your system !


def pull_files(some_file):
    """ A new folder is made for each file type searched. Then all said files are moved
    into each said folder respectively. """
    # folder path created, if folder doesn't already exist
    folder_name = filesto + "/RECOVERED-" + some_file.upper()
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    # the file extension is searched and moved to the folder created
    os.system("find . -type f -name '*." + some_file + "' -print0 | xargs -0 -I {} mv {} " + folder_name)
    if len(os.listdir(folder_name)) == 0:
        os.rmdir(folder_name)
        print(some_file + ' = ' + str(0) + ' files found / or invalid file extension')
    else:

        print(some_file + ' = ' + str(len(os.listdir(folder_name))) + ' file(s) found')


# determine the folder path to the files you want to search
# determine where you want to store the saved files
# checks whether the source path is valid and if folder has content or not
x = True
while x:
    filesfrom = input('Enter the folder path to where the recup files are stored: \n')
    if os.path.isdir(filesfrom) and sum([len(files) for r, d, files in os.walk(filesfrom)]) > 0:
        x = False
    elif os.path.isdir(filesfrom) and sum([len(files) for r, d, files in os.walk(filesfrom)]) == 0:
        print("There are no files in '" + filesfrom + "' Please make sure this is the right folder.")
        x = True
    else:
        print("'" + filesfrom + "' is not a working directory, please try again.")
        x = True

x = True
while x:
    filesto = input('Enter the folder path to where you want your desired files stored: \n')
    if os.path.isdir(filesto):
        x = False
    else:
        print('Not a directory: try again')
        x = True
# clean up list, separating each entry by a comma and removing white spaces
typesOfFiles = list(input('which types of files are you looking for?: \n').split(','))
typesOfFiles = [x.strip() for x in typesOfFiles]

# changing current working directory to where the files are stored, count is done
os.chdir(filesfrom)
cpt1 = sum([len(files) for r, d, files in os.walk(filesfrom)])
print(str(cpt1) + ' file(s) in "' + filesfrom + '"')

# loops through all file types desired, passing it through a function
# to create a folder for each, and moving the files
for file in typesOfFiles:
    pull_files(file)

# count all files remaining
cpt2 = sum([len(files) for r, d, files in os.walk(filesfrom)])
print(str(cpt2) + ' file(s) remaining in "' + filesfrom + '" : '  + str(cpt1 - cpt2) + ' file(s) recovered')

# removing directories
res = input("Delete remaining file(s)? (Y/N): \n")
if res == ('Y' or 'y'):
    shutil.rmtree(filesfrom)
