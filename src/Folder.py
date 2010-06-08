'''
Created on 28.05.2010

@author: andrey
'''
from FileEntry import FileEntry
import os.path

class NoFileEx(Exception):
    '''
    Exception for the case if folder is not contain some file
    ''' 
    pass

class Folder(FileEntry):
    '''
    class represents disk folder, witch consist other folders
    and files
    '''

    def __init__(self, path, parent=None):
        '''
        Constructor
        '''
        super(Folder, self).__init__(path)
        self.parent = parent
        self.files = []
        self.walk()
        
    def walk(self):
        '''
        Walk over all files and folders inside directory
        '''
        try:
            dir_list = os.listdir(self.path)
        except OSError as detail:
            print "Can't add folder ", self.path, '.', detail
            return
        for curr_file in dir_list:
            self.add_file(os.path.join(self.path, curr_file))
        
    def add_file(self, filepath):
        '''
        adding file (or folder) into that folder
        '''
        if os.path.islink(filepath):
            return
        if (os.path.isdir(filepath)):
            if (self.parent == None):
                print "Add folder %s" % filepath
            self.files.append(Folder(filepath, self))
        else:
            self.files.append(FileEntry(filepath))
            
        
    def get_size(self):
        '''
        returns sum of all files sizes
        '''
        if (self.size == None):
            self.size = sum([f.get_size() for f in self.files])
        return self.size
    
    def __getitem__(self, key):
        for curr_file in self.files:
            if (curr_file.get_name() == key):
                return curr_file
        raise NoFileEx
    
        
    