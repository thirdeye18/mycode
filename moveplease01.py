#!/usr/bin/env python3
"""A simple script to move 2 files into ceph_storage/"""

# importing the needed standard libraries
import shutil   #shell utilities to move the files
import os       #access to low level os operations (changing program start directory)


def main():
    """called at runtime"""
    # force app to start in the student home directory
    os.chdir('/home/student/mycode/')
    
    # moving file from source to destination folder, will overwrite the file if already exists
    shutil.move('raynor.obj', 'ceph_storage/raynor.obj')

    # prompt for new file name
    xname = input('What is the new name for kerigan.obj? ')
    # "renaming" file by moving old file and giving it new name in destination
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()  # calling the main function


