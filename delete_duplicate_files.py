import filecmp
import os

files_list=os.listdir()

for pics in files_list:
    if pics != 'filename.png':  # the image being duplicated
        if filecmp.cmp("filename.png",pics):
            os.remove(pics)  #removing the duplicates
            print("similar")
        else: 
            print("not similar")
