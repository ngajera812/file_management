import os
import os.path
import shutil
import SOECE13017_NENSHI_DILIPBHAI_GAJERA_gui

def file_extension(filename):
    split_tup = os.path.splitext(filename)
    return split_tup[1]

def directory_exists(temp_dest):
    return os.path.isdir(temp_dest)

def create_directory(d, dir):
    path=os.path.join(d, dir)
    os.mkdir(path)

def file_exists(f):
    return os.path.exists(f)

def movefile(s, d):
    shutil.move(s, d)

source = SOECE13017_NENSHI_DILIPBHAI_GAJERA_gui.source
destination = SOECE13017_NENSHI_DILIPBHAI_GAJERA_gui.destination

source += '/'
destination += '/'
for filename in os.listdir(source):

    extension=(file_extension(filename))
    extension=extension[1:]

    if extension == '':
        continue

    temp = destination + extension

    if not(directory_exists(temp)):
        create_directory(destination, extension)

    s = source + filename
    d = destination + extension + '/' + filename

    if file_exists(d):
        print(filename, " already exists")
        continue

    movefile(s, d)
