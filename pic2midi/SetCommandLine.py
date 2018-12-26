import sys

def SetCommandLine(argv,commands):
    retCmds = commands

    for i,arg in enumerate(argv):
        if arg == '-h' or arg == '--help':
            printHelp()
            sys.exit() #if help is printed, end program
        
        if arg == '-t': #length
            length = int(argv[i+1])
            assert(length <= 255)
            assert(length >= 0)
            retCmds['length'] = length

        if arg == '-T': #tempo
            tempo = int(argv[i+1]) 
            retCmds['tempo'] = tempo

        if arg == '-o': #output file name
            name = argv[i+1]
            if name[-5::] != '.midi':
                name += '.midi'
            retCmds['outName'] = name
			
        if arg == '-i': #input file name
            retCmds['inName'] = argv[i+1]
        
        if arg == '-v': #Constant velocity?
            vel = False if argv[i+1] == 'False' else True
            retCmds['Vel'] = vel

        if arg == '-vt': #threshold 2
            BWth = int(argv[i+1])
            assert(BWth <= 255)
            assert(BWth >= 0)
            retCmds['VelThreshold'] = BWth

        if arg == '-th': #threshold 1
            th = int(argv[i+1])
            assert(th <= 255)
            assert(th >= 0)
            retCmds['threshold'] = th
   
        if arg == '-r': #range
            rang = int(argv[i+1])
            assert(rang > 0)
            assert(rang < 128)
            retCmds['range'] = rang
            
    return retCmds

def printHelp():
    sys.stdout.buffer.write(b'\nThe possible CmdLine arguments are:\n'+
                            b'\n'+
                            b'-h or --help prints this help message\n'+
                            b'\n'+
                            b'-t  Set the length of the midi (in beats)\n'+
                            b'-r  Set the range of the midi (in semitones)\n'+
                            b'-T  Set the tempo of the midi (in bpm)\n'+
                            b'-o  Set the output file name (.midi will be appended)\n'+
							b'-i  Set the input file name (if not the last argument)\n'+
                            b'-th Set the threshold for the image brightness (default 40)\n'+
                            b'-v  Set whether the output will have constant Velocity (True/False)\n'+
                            b'-vt Set the threshold for a hit note if the Velocity is Constant (default 20)\n'+
                            b"- The final argument must be the filename of the input image unless it's given with -i\n"+
                            b'\n'+
                            b"If the big picture shown doesn't look right, play with '-th'\n"+
                            b"If the small picture shown doesn't look right, play with '-vt'\n"+
                            b'For both of these options, a lower number means more pixels drawn (maximum values are 255)\n')
    return
