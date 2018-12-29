# pic2midi
Take a picture and have it processed into midi-art with python 3

This requires the following non-native python packages:

	numpy
	PIL
	midiutil

All of these packages are available using PIP.

### Using this package

once installed this package can be used with the terminal command:

	python main.py <options>

Where options can be viewed in full by adding -h to the command.
The most imporant options are -th and -vt, these are explained in more detail below. There is also the -o option allowing you to name your output file (.midi will be appened automatically if you forget it).


Once this package has been used, you will be presented with 2 pictures, the big one can be adjusted using the -th threshold. This image should look like line art of the input picture. The small one can be adjusted using the -vt theshold, this will be the midi that is output to file.
