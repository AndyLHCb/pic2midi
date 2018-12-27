import numpy as np
import sys
from PIL import Image

def StitchNotes(im, CmdLine):
    
    imArray = np.array(im)
    notes = np.array([])
    
    #contstant velocity
    if CmdLine['Vel'] and CmdLine['Stitching']:
        for i in range(imArray.shape[0]):
            for j,val in enumerate(imArray[i]):
                
                if val > 0:

                    #test if a note needs extending
                    extensionTest = False
                    
                    for n in notes:
                        if n.pitch == i:
                            pn = n.time + n.length #previous note
                            if pn == j:
                                n.length += 1
                                extensionTest = True       
                                
                    if extensionTest:
                        continue
                    else:
                        n = note(j , 1, val >> 1, i)
                        notes = np.append(notes, n)
    
    #not constant velocity (no stitching)
    else:
        for i in range(imArray.shape[0]):
            for j,val in enumerate(imArray[i]):
            
                n = note(j, 1, val >> 1, i)
                notes = np.append(notes, n)
    
    
    return notes
    
class note(object):
    def __init__(self, time = 0, length = 1, velocity = 127, pitch = 0):
        self.time = time
        self.length = length
        self.velocity = velocity
        self.pitch = pitch