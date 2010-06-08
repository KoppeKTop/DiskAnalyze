'''
Created on 28.05.2010

@author: andrey
'''

from Folder import NoFileEx, Folder

max_files = 30

def repr_file_size(curr_sz):
    '''
    Represents file size in human readable form
    '''
    sz_type = ''
    if (curr_sz > 1024):
        curr_sz = curr_sz/1024.0
        sz_type = 'Kb'
    if (curr_sz > 1024):
        curr_sz = curr_sz/1024.0
        sz_type = 'Mb'
    if (curr_sz > 1024):
        curr_sz = curr_sz/1024.0
        sz_type = 'Gb'
    if (curr_sz > 1024):
        curr_sz = curr_sz/1024.0
        sz_type = 'Tb'
    return "%.1f%s" % (curr_sz, sz_type)

def print_name_size(name, size, max_len):
    '''
    Prints name and size (strings)
    '''
    print name, ' ' * (max_len-len(name)), '\t', size

def get_longest_name(files):
    '''
    Find longest name in list
    '''
    return max([len(f.get_name()) for f in files])

def print_infos(files, max_len):
    '''
    Print info for each file in list
    '''
    for curr_file in files:
        print_name_size(curr_file.get_name(), 
                        repr_file_size(curr_file.get_size()), max_len)

def print_files(fld):
    '''
    Display all files in a folder + sizes
    '''
    print 'Folder: %s\t Total size: %s' % \
           (fld.get_name(), repr_file_size(fld.get_size()))
    printed_files = sorted(fld.files, key = lambda x: x.get_size(), 
                           reverse=True)[:max_files]
    
    folders = filter(lambda x: isinstance(x, Folder), printed_files)
    files = filter(lambda x: not isinstance(x, Folder), printed_files)
    max_len = get_longest_name(printed_files)
    # print all folders first:
    print_name_size("Name", "size", max_len)
    if (folders):
        print "Folders:"
        print_infos(folders, max_len)
    if (files):
        print "Files:"
        print_infos(files, max_len)
    
def read_command():
    '''
    Get command from user
    '''
    command = raw_input('q - quit, u - up, h - home: ')
    return command

class UI(object):
    '''
    User interface
    '''


    def __init__(self, root_path):
        '''
        Constructor
        '''
        self.root = Folder(root_path)
        self.curr = self.root
        self.work = True
    
    def show(self):
        '''
        Start work with user
        '''
        while self.work:
            print_files(self.curr)
            cmd = read_command()
            self.process_cmd(cmd)
            
    def process_cmd(self, cmd):
        '''
        Processing of user commands
        '''
        if (cmd == 'q'):
            self.work = False
        elif (cmd == 'u'):
            parent = self.curr.parent
            if parent != None:
                self.curr = parent
        elif (cmd == 'h'):
            self.curr = self.root
        else:
            try:
                self.curr = self.curr[cmd]
            except NoFileEx:
                # stay in that folder
                pass
