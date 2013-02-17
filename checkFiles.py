import os
from fnmatch import fnmatch

root = './openehr'
pattern = "*.py"

files = []

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
        	filename = os.path.join(path, name)
        	execfile(filename)