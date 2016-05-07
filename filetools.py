'''
filetools.py

Access files in a directory

'''

from os import listdir
from os.path import isfile, join

def get_files(dir_path, substr=None):
    '''
    return a list of files in a directory
    '''
    if substr:
        return [f for f in listdir(dir_path) if isfile(join(dir_path, f)) and substr in join(dir_path, f)]

    else:
        return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

