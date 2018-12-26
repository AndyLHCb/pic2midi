#################################################
#  pic2midi main file                           #
#  Andy Morris 2018                             #
#                                               #
#################################################

import sys
from pic2midi.ImageProcessing import ImageProcessing
from pic2midi.CreateMIDI import CreateMIDI
from pic2midi.SetCommandLine import SetCommandLine
from pic2midi.StitchMIDI import StitchMIDI
from PIL import Image
from midiutil.MidiFile import MIDIFile

#Command line inputs (with default values)
CmdLine = {'tempo':120, #tempo
           'length':64, #length of midi (beats)
           'range':60,  #range of midi (semitones)
           'threshold':40, #threshold1
           'Vel':True,  #constant velocity?
           'VelThreshold':20, #threshold2
           'inName':sys.argv[-1], #image name
           'outName':'a.midi'} #midi name
CmdLine = SetCommandLine(sys.argv,CmdLine)

#Processing the image
image = Image.open(CmdLine['inName'])

sys.stdout.buffer.write(b'Processing Image . . . ')
sys.stdout.flush()
image = ImageProcessing(image,CmdLine)
sys.stdout.buffer.write(b"complete\n")

image.show('Preview of the midi file')

#Generating the MIDI
sys.stdout.buffer.write(b'Creating MIDI . . . ')
sys.stdout.flush()
MIDI = CreateMIDI(image,CmdLine)
sys.stdout.buffer.write(b"complete\n")

#Stitching the MIDI (not implimented yet)
#i.e. if 2 pixels are next to each other make 1 long note
sys.stdout.buffer.write(b'Stitching MIDI . . . ')
sys.stdout.flush()
MIDI = StitchMIDI(MIDI)
sys.stdout.buffer.write(b'complete\n')

#Write MIDI
sys.stdout.buffer.write(b'Writing MIDI to File . . . ')
sys.stdout.flush()

with open(CmdLine['outName'], 'wb') as outf:
    MIDI.writeFile(outf)

sys.stdout.buffer.write(b"complete\n")