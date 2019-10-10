import os

srcpath = "E:/temp/example"
dstpath = srcpath #change this to move files to this path
extensionBefore = ".mp4"
extensionAfter = ".mp3" 

for filename in os.listdir(srcpath):
    name=filename[ :-len(extensionBefore)]
    #name can be modified here
	
    if filename[ len(name):] == extensionBefore:#renames all files with extensionBefore
        dst = dstpath + "/"+str(name) + extensionAfter
        src =srcpath + "/"+str(name) + extensionBefore
        os.rename(src, dst)
