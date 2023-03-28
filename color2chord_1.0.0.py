"""Color to Chord 1.0.0 - Convert colors to chords.
Copyright (C) 2023  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
rgb_scale = 255
cmyk_scale = 100

def inputRGB():
    global R
    global G
    global B
    global quitcheck
    print ("Input R, G, B values for a color in RGB format."+"\n")
    R=input("R (q to quit): ")
    if R=='q':
        quit()
    if R.isdigit()==False or int(R)<0:
        R=0
    if int(R)>255:
        R=255
    G=input("G (q to quit): ")
    if G=='q':
        quit()
    if G.isdigit()==False or int(G)<0:
        G=0
    if int(G)>255:
        G=255
    B=input("B (q to quit): ")
    if B=='q':
        quit()
    if B.isdigit()==False or int(B)<0:
        B=0
    if int(B)>255:
        B=255
    R=int(R)
    G=int(G)
    B=int(B)
    GenerateChord(R,G,B)
    

def rgb_to_cmyk(r,g,b):
    if (r == 0) and (g == 0) and (b == 0):
        # black
        return 0, 0, 0, cmyk_scale

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / float(rgb_scale)
    m = 1 - g / float(rgb_scale)
    y = 1 - b / float(rgb_scale)

    # extract out k [0,1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) 
    m = (m - min_cmy) 
    y = (y - min_cmy) 
    k = min_cmy

    # rescale to the range [0,cmyk_scale]
    cmyk=[ int(c*cmyk_scale), int(m*cmyk_scale), int(y*cmyk_scale), int(k*cmyk_scale)]
    return cmyk

#GenerateChord

def GenerateChord(R,G,B):
    cmyk=rgb_to_cmyk(R,G,B)
    chord=[]
    rootvalue=int(((R+G+B)/3)/21.25)
    root=notes[rootvalue]
    chord.append(root)
    notevalue=rootvalue
    #print (notevalue,root)
        
    for value in cmyk:
        try:
            interval=int(value/16.66)+3
        except:
            interval=3
        notevalue=notevalue+interval
        if notevalue>11:
            notevalue=notevalue-11
        chord.append(notes[notevalue])
    chorddisplay=''
    for item in chord:
        chorddisplay= chorddisplay+item+" "
    print ("\n"+"Chord: "+chorddisplay+"\n")

#main
def main():
    global R
    global G
    global B
    while True:
        inputRGB()

main()
