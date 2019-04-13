#!/usr/bin/python2.7
import os
import sys
try:
    sys.path.index(os.getcwd)
except ValueError:
    sys.path.append(os.getcwd)

def getdetails(filename,split):
    path = str(filename)
    temp = path.split("/")
    name = temp[-1]
    size = str(os.path.getsize(filename))+" bytes"
    if size == "None":
        size == "Null"
    print ("\n\tFilePath: "+path+"\n\tFileName: " +name+ "\n\tSize: " +size)
    if split:
        try:
            fname,ftype = name.split(".")
            print ("\n\tFilePath: "+path+"\n\tFileName: " +fname+ "\n\tSize: " +size+ "\n\tFileType: It is a "+ftype+"file")
        except:  print ("\n\tFilePath: "+path+"\n\tFileName: " +name+ "\n\tSize: " +size)


def directorytraversal(dirname):
    listeditems = os.listdir(dirname)
    for item in listeditems: 
     testfile = (dirname+"/"+item)
     if os.path.isdir(testfile):
            print("\n[!] "+item+": is a directory! ")
            getdetails(testfile,False)
            print("\n\n[!]Changing context \f")
            a = ["~"*100]
            print a
            directorytraversal(testfile)
            continue
     elif os.path.isfile(testfile):
            getdetails(testfile,True)
            continue

print("\n[!]CAUTION: This program will recursively dox all files in the given directory! \n")
rinput = str(raw_input("[+] Welcome, enter the full path of directory to be doxed:"))
print("\n\nResult generated : ")
print("\n[*]Details: \f")
directorytraversal(rinput)

