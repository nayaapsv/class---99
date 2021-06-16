import os
import shutil
import time

deletedfolders = 0
deletedfiles = 0

path = "/Nayaa/WhiteHat/Python/Class - 99/backup/Project/deleted"
days = 1
seconds = time.time() - (days  * 60 * 60* 24)
print(path)

def getfolderage(path):

	curtime = os.stat(path).st_ctime
	return curtime



def removefile(path):

	if not os.remove(path):

		print(path+" is removed ")

	else:

		print("not able to delete the "+path)



def removefolder(path):
	if not shutil.rmtree(path):

		
		print(path+" is removed ")

	else:
		print("not able to delete the "+path)


if os.path.exists(path):
    for subfolder, folders, files in os.walk(path):
        
        if seconds >= getfolderage(subfolder):
            
            removefolder(subfolder)

            deletedfolders = deletedfolders +1
            
        else:
            for folder in folders:
                folderpath = os.path.join(subfolder,folder)
                if seconds >= getfolderage(folderpath):
                    removefolder(folderpath)
                    deletedfolders = deletedfolders +1
        
            for file in files:
                file_path = os.path.join(subfolder, file)
                if seconds >= getfolderage(file_path):
                    removefile(file_path)
                    deletedfiles = deletedfiles +1
    else:
        if seconds >= getfolderage(path):
            removefile(path)
            deletedfiles = deletedfiles +1

else:
        print(path+' is not found')
        deletedfiles = deletedfiles +1

	

print(deletedfolders)
print(deletedfiles)