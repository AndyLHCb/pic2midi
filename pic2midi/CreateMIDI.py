from PIL import Image
from midiutil.MidiFile import MIDIFile
from pic2midi.StitchNotes import note
import numpy as np

def CreateMIDI(notes, CmdLine):
    
    #highest note = note0
    note0 = 64 + round(CmdLine['range']/2) #60 = middle C, 64 = E
    
    #WRITE MIDIFILE
    mf = MIDIFile(1) # 1 track
    track = 0
    time = 0

    mf.addTrackName(track, time, "pic2midi output")
    mf.addTempo(track, time, CmdLine['tempo'])

    channel = 0
    duration = 1 #each note 1 beat

    for n in notes:
            truePitch = note0 - n.pitch

            mf.addNote(track, channel, truePitch, n.time, n.length, n.velocity)

    return mf


