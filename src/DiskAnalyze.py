#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
Created on 28.05.2010

@author: andrey
'''

from UI import UI
import sys
import os.path

def get_folder_from_user():
    '''
    Ask user for folder path, check it and returns
    '''
    while True:
        folderpath = raw_input('Enter folder path: ')
        folderpath = os.path.expanduser(folderpath)
        if os.path.isdir(folderpath):
            break
        print "No such folder..."
    return folderpath

def main():
    '''
    Main function for user iteractions
    '''
    if (len(sys.argv) == 1):
        folderpath = get_folder_from_user()
    else:
        folderpath = sys.argv[1]
        if not os.path.isdir(folderpath):
            folderpath = get_folder_from_user()
    user_interface = UI(folderpath)
    user_interface.show()

if __name__ == '__main__':
    main()