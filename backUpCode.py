import os
import shutil
source = input("Enter  Source Folder Name: ") 
dest = input("Enter Destination Folder Name: ")
source = source +"/"
dest = dest+"/"
listOfFiles= os.listdir(source)

for file in listOfFiles:
    shutil.copy((source+file),dest)