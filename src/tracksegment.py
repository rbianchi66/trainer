'''
Created on May 12, 2014

@author: rbianchi
'''

class TrackSegment(object):
    '''
    A segment of a Track
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        ## List of segments Trackpoint
        self.trackpoints = []