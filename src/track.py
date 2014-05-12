'''
Created on May 12, 2014

@author: rbianchi
'''

class Track(object):
    '''
    classdocs
    '''


    def __init__(self, number, name):
        '''
        Constructor
        '''
        
        ## The track internal ID
        self.id = number
        
        ## The track name
        self.name = name
        
        ## List of TrackSegment of this Track
        self.segments= []