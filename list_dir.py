import hashlib 
from os import walk, makedirs
import os.path
import shutil
import datetime
import sys
import codecs
import csv
import pathlib
import PyPDF2

def GetHash(file):
    f = open(file,'rb')
    c = f.read()
    f.close()
    hashmd5 = check = hashlib.md5(c).hexdigest()
    return hashmd5

def MakeFileList(path):
    present = datetime.datetime.now()
    for dir, subdirs, fnames in walk(path):
        for fname in fnames:
            print(fname)
            fullpath=str('{}'.format(dir))
            l_fname=fname.lower()
            
            #LAST MOD & CREATED DATE*
            lastmod=datetime.datetime.fromtimestamp(os.path.getmtime(fullpath+"/"+l_fname))
            created=datetime.datetime.fromtimestamp(os.path.getctime(fullpath+"/"+l_fname))
            
            #GET FILE EXTENSION AND RUN A HASH ON NON-ZIPS
            fname, file_extension = os.path.splitext(l_fname)
            hash=None
            if file_extension != ".zip": 
                hash = GetHash(fullpath+"/"+l_fname)

            vartexts=(fullpath,fname,created,lastmod,file_extension,hash)
            csvwriter.writerow(vartexts)

outfile = codecs.open("directorylist.csv",'w','utf-8')
csvwriter = csv.writer(outfile, quoting=csv.QUOTE_ALL)
header=("fullpath","filename","created","modified","extension","hash")
csvwriter.writerow(header)

MakeFileList("Sources")
outfile.close()

exit()
