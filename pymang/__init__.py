import os
import shutil
import sys
import glob

'''
A file management library
'''
__all__ = ['Class']
class mg:
   #delete file
    def delete(self,file):
        '''This:
              delete file
              *arg
        '''
        os.remove(file)
        print(str(file)+" was removed from system")
   
   #transfer file
    def transfer(self,file1,file2):
        '''transfer file
        used to transfer file
        '''
        shutil.move(file1,file2)
        print(str(file1)+" was moved to "+str(file2))
    #make directory
    def mkdiry(self,name):
        '''Use:
              make a directory
        '''
        os.mkdiry(name)
        print(f"A new directory named '{name}' was created")

    #list 
    def list():
        '''list all directories'''
        glob.glob("*")
    
    #copy file
    def copy(self,file1,file2):
        '''copy file'''
        shutil.copy(file1,file2)
        print(f"{file1} was copied to {file2}")
    
    #new file
    def newf(self,file,words):
        '''create new file'''
        f=open(file,"w+")
        f.write(words)
        f.close()
    #exit
    def exit(self):
        '''exit system'''
        sys;exit()

    #remove directory
    def rmdiry(self,name):
        '''delete the directory'''
        os.rmdir(name)
        print(f"{name} was removed")