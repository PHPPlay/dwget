from xml.etree import ElementTree as ET
from xml.etree.ElementTree import *

class Report():
    '''
    Class responsible for generating reports fur das Master Node.
    The Master Node giveth and the Master Node taketh away, blessed 
    be the name of the Master Node.
    '''
    
    # All the required elements.
    state = 0
    location = ''
    currentSpeed = 0
    averageSpeed = 0
    receivedSoFar = 0
    

    def __init__(self, slaveMgr, dlThread):
        self.state = slaveMgr.state
        if dlThread:
            self.location = dlThread.url
            self.currentSpeed = dlThread.speed
            self.averageSpeed = dlThread.speed5s
            self.receivedSoFar = dlThread.received # @TODO: This is not what should be sent -> fails after resume. Probably self.written. 
            
    def generateReport(self):
        '''
        Method generates the XML version of the report.
        
        @return ready XML string
        '''
        
        doc = Element("Report")
        SubElement(doc, u'status').text = '%d' % (self.state)
        SubElement(doc, u'url').text = self.location
        SubElement(doc, u'received').text = '%d' % (self.receivedSoFar)
        SubElement(doc, u'currentSpeed').text = '%f' % (self.currentSpeed)
        SubElement(doc, u'avgSpeed').text = '%f' % (self.averageSpeed)
        
        return ET.tostring(doc, 'utf-8')
            
        