'''
Created on 28.05.2010

@author: andrey
'''

import os

class FileEntry(object):
    '''
    stores file information
    '''


    def __init__(self, path):
        '''
        Constructor
        '''
        self.path = path
        self.size = None
        
    def get_size(self):
        '''
        Size of current file
        '''
        if self.size == None:
            self.size = os.stat(self.path).st_size 
        return self.size
    
    def get_name(self):
        '''
        Returns only name of file
        '''
        return self.path.split(os.path.sep)[-1]
    
    def get_containing_dir(self):
        '''
        Returns directory in which this file in
        '''
        return self.path.split(os.path.sep)[-2]