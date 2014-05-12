'''
Created on May 12, 2014

@author: rbianchi
'''

class Trackpoint(object):
    '''
    A track point
    '''


    def __init__(self, lat, lon, ele, time, sym):
        '''
        Constructor
        '''
        
        ## The point latitude
        self.latitude= lat
        
        ## The point longitude
        self.longitude = lon
        
        ## The point elevation
        self.elevation = ele
        
        ## Extra point data
        self.sym = sym