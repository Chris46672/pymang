import os
import shutil
import sys
import glob

class mg:
   def delete(self,file):
       os.remove(file)
       print(str(file)+" was removed from system")

   def transfer(self,file1,file2):
       shutil.move(file1,file2)
       print(str(file1)+" was moved to "+str(file2))

   def mkdiry(self,name):
       os.mkdiry(name)
       print(f"A new directory named '{name}' was created")

   def list():
       glob.glob("*")

   def copy(self,file1,file2):
       shutil.copy(file1,file2)
       print(f"{file1} was copied to {file2}")

   def newf(self,file,words):
       f=open(file,"w+")
       f.write(words)
       f.close()

   def exit(self):
       sys;exit()

   def rmdiry(self,name):
       os.rmdir(name)
       print(f"{name} was removed")
