from PIL import Image, ImageFilter
import numpy as np

def ImageProcessing(im, commands):

    #MAKE THE PICTURE GREYSCALE
    im = im.convert('L') 

    #RUN EDGE DETECTION
    im = im.filter(ImageFilter.FIND_EDGES)

    #MAKE B&W
    imArray = np.array(im)
    for i in range(imArray.shape[0]):
        for j,val in enumerate(imArray[i]):
            imArray[i,j] = 0 if val < commands['threshold'] else 255

    #MAKE EDGES THICKER
    
    newArray = np.copy(imArray)

    for i in range(imArray.shape[0]):
        for j,val in enumerate(imArray[i]):
            if val == 255:
                newArray[i,j] = 255

                if i>0:
                    newArray[i-1,j] = 255
                if j>0:
                    newArray[i,j-1] = 255
                if i<imArray.shape[0]-1:
                    newArray[i+1,j] = 255
                if j<imArray.shape[1]-1:
                    newArray[i,j+1] = 255

    im = Image.fromarray(newArray)
    im.show('Preview of the image being drawn')

    #RESIZE
    im = im.resize((commands['length'], commands['range']), Image.ANTIALIAS)

    #NORMALISE
    imArray = np.array(im)
    ratio = 255./np.amax(imArray)

    if ratio != 1:
        for i in range(imArray.shape[0]):
            for j,val in enumerate(imArray[i]):
                imArray[i,j] = round(val*ratio)



    #READJUSTING TO B&W
    if commands['Vel']:
        imArray = np.array(im)
        for i in range(imArray.shape[0]):
            for j,val in enumerate(imArray[i]):
                imArray[i,j] = 0 if val < commands['VelThreshold'] else 255
        
        im = Image.fromarray(imArray)       

    return im
