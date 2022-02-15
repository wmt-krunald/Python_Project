from importlib.resources import path
import os

def renameFiles():
    i = 0
    path = "/home/webmob/Krunal_Work_space/Python/Python_Project/Pro-12:Rename_Bulk_File/testFiles/"
    for filename in os.listdir(path):
        my_desti = "test" + str(i) + ".png"
        my_source = path + filename
        my_desti = path + my_desti
        os.rename(my_source, my_desti)
        i += 1

renameFiles()