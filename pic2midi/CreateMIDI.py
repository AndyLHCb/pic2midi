from PIL import Image
from midiutil.MidiFile import MIDIFile
import numpy as np

def CreateMIDI(im, CmdLine):

    imArray = np.array(im)
    
    #highest note = note0
    note0 = 60 + round(CmdLine['range']/2) #60 = middle c
    
    #WRITE MIDIFILE
    mf = MIDIFile(1) # 1 track
    track = 0
    time = 0

    mf.addTrackName(track, time, "pic2midi output")
    mf.addTempo(track, time, CmdLine['tempo'])

    channel = 0
    duration = 1 #each note 1 beat

    for i in range( imArray.shape[0] ):
        for j,velocity in enumerate( imArray[i] ):
            pitch = note0 - i
            time = j

            mf.addNote(track, channel, pitch, time, duration, velocity)

    return mf


