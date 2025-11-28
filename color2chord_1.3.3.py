"""Color to Chord 1.3.3 - Convert colors to chords.
Copyright (C) 2023  SymbolForm

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

import random
from random import randint
import tkinter as tk
from tkinter import colorchooser
import tkinter.ttk as ttk
import musicpy
from shutil import copyfile
from os import remove
import colorsys
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from tkinter import *
import os
import webbrowser
try:
    import pyi_splash
    pyi_splash.close()
except:
    True

notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
rgb_scale = 255
cmyk_scale = 100
steps=[[0, 2, 4, 5, 7, 9, 11, 0], [0, 2, 3, 5, 7, 9, 10, 0], [0, 1, 3, 5, 7, 8, 10, 0], [0, 2, 4, 6, 7, 9, 11, 0], [0, 2, 4, 5, 7, 9, 10, 0], [0, 2, 3, 5, 7, 8, 10, 0], [0, 1, 3, 5, 6, 8, 10, 0], [0, 2, 3, 5, 7, 9, 11, 0], [0, 1, 3, 5, 7, 9, 10, 0], [0, 2, 4, 6, 8, 9, 11, 0], [0, 2, 4, 6, 7, 9, 10, 0], [0, 2, 4, 5, 7, 8, 10, 0], [0, 2, 3, 5, 6, 8, 10, 0], [0, 1, 3, 4, 6, 8, 10, 0], [0, 2, 3, 5, 7, 8, 11, 0], [0, 2, 4, 6, 8, 10, 0], [0, 2, 3, 5, 6, 7, 8, 10, 0], [0, 2, 3, 5, 6, 8, 9, 11, 0], [0, 2, 3, 5, 6, 8, 9, 10, 0], [0, 1, 3, 4, 6, 7, 9, 10, 0], [0, 3, 5, 7, 10, 0], [0, 2, 4, 7, 9, 0], [0, 3, 5, 6, 7, 10, 0], [0, 2, 3, 4, 5, 7, 9, 10, 11, 0], [0, 2, 4, 5, 7, 8, 9, 11, 0], [0, 2, 3, 5, 7, 8, 10, 11, 0], [0, 2, 4, 5, 7, 9, 10, 11, 0]]
stepsnames=['Ionian', 'Dorian', 'Prhygian', 'Lydian', 'Mixolydian ', 'Aeolian ', 'Locrian', 'Melodic minor', 'Dorian b2', 'Lydian augmented', 'Lydian dominant ', 'Mixolydian b6 ', 'Aeolian b5 ', 'Altered scale', 'Minor Bebop', 'Whole Tone', 'Octatonic', 'Whole-Half Diminished', 'Whole-Half Diminished ', 'Half-Whole Diminished', 'Pentatonic minor ', 'Pentatonic major ', 'Blues scale ', 'Dorian Bebop ', 'Major Bebop', 'Harmonic Minor Bebop', 'Dominant Bebop']
stepsitem=[]
stepscale=[]
stepscales=[]
chord_play=[]
scales=[]

def init():
    global chordnotes
    global counter
    global chord
    global chordstring
    global notelist
    global occurrences
    global chordsteps
    global scale
    global stepstransposed
    global chordn
    global scalecombo
    

    chordnotes=[]
    chord=[]
    chordsteps=[]
    counter=1
    octave=4
    chordstring=""
    notelist=[]
    occurrences=[]
    clash_occ=[0,0,0,0,0,0,0,0,0,0,0,0]
    random.seed()
    scale=[]
    scalecombo=[]
    stepstransposed=[]

#Create app window
def create_app_window():
    global top
    global rootw
    img=b'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'
    rootw= tk.Tk()
    top= rootw
    top.geometry("470x440")
    top.resizable(0,0)
    top.title("Color to Chord")
    favicon=tk.PhotoImage(data=img) 
    rootw.wm_iconphoto(True, favicon)
    rootw.protocol("WM_DELETE_WINDOW", QuitApp)

    #Create settings entries

    global ColorDisplayFrame
    ColorDisplayFrame= tk.Frame(top)
    ColorDisplayFrame.place(x=25, y=20, height=90, width=265)
    ColorDisplayFrame.configure(relief='groove')
    ColorDisplayFrame.configure(borderwidth="2")
    ColorDisplayFrame.configure(relief="groove")
    ColorDisplayFrame.bind("<Button-1>",pick_color_frame)
 
    #chord display
    global chord_display
    global chord_display_entry
    global chord_display_label
    chord_display=tk.Text(top)
    chord_display.place(x=25,y=135,height=25,width=420)
    chord_display.configure(state='disabled')    
    chord_display_label=tk.Label(top)
    chord_display_label.place(x=25,y=160,width=200)
    chord_display_label.configure(text="Chord",anchor="w", justify="left",font=("Arial",12))
    #scales display
    global scales_display
    global scales_display_label
    scales_display=ttk.Combobox(top)
    scales_display.place(x=25,y=190,height=25,width=420)
    scales_display.configure(state="readonly",values=[" "])
    scales_display.bind("<<ComboboxSelected>>", scales_caption_display)
    scales_display_label=tk.Label(top)
    scales_display_label.place(x=25,y=215,width=420)
    scales_display_label.configure(text="Scale",anchor="w", justify="left",font=("Arial",12))
    #history display
    global history_display
    global history_display_entry
    history_display = tk.Text(top)
    history_display.place(x=25, y=250, height=160, width=405)
    scroll_1=tk.Scrollbar (top)
    scroll_1.place(x=440, y=250, height=160, anchor='n')
    history_display.configure(yscrollcommand=scroll_1.set)
    scroll_1.configure(command=history_display.yview)    
    #generate chord button
    """global generate_chord_button
    generate_chord_button=tk.Button(top)
    generate_chord_button.place(x=310,y=20,height=40,width=140)
    generate_chord_button.configure(text="Generate chord",font=("Arial",12))
    generate_chord_button.bind("<Button-1>",generate_chord_hotkey)"""
    #play chord button
    global play_chord_button
    play_chord_button=tk.Button(top)
    play_chord_button.place(x=310,y=20,height=40,width=140)
    play_chord_button.configure(text="Play chord",font=("Arial",12))
    play_chord_button.bind("<Button-1>",play_chord_hotkey)
    #play scale button
    global play_scale_button
    play_scale_button=tk.Button(top)
    play_scale_button.place(x=310,y=70,height=40,width=140)
    play_scale_button.configure(text="Play scale",font=("Arial",12))
    play_scale_button.bind("<Button-1>",play_scale_hotkey)    

    #file menu
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left",label="Save chord", command=save_chord, accelerator="Alt+C")
    sub_menu.add_command(compound="left",label="Save_scale", command=save_scale,accelerator="Alt+S")
    sub_menu.add_command(compound="left",label="Save history", command=save_history, accelerator="Alt+H")
    sub_menu.add_command(compound="left",label="Erase history", command=erase_history, accelerator="Alt+E")
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp,accelerator="Alt+Q")

    top.bind_all("<Alt-c>",save_chord_hotkey)
    top.bind_all("<Alt-s>",save_scale_hotkey)
    top.bind_all("<Alt-h>",save_history_hotkey)
    top.bind_all("<Alt-e>",erase_history_hotkey)
    top.bind_all("<Alt-q>",QuitApp_hotkey)
    
    #play menu
    global play_menu
    play_menu=tk.Menu(top,tearoff=0)
    menubar.add_cascade(menu=play_menu,compound="left", label="Play")
    play_menu.add_command(compound="left",label="Play chord", command=play_chord, accelerator="Alt+P")
    top.bind_all("<Alt-p>",play_chord_hotkey)
    play_menu.add_command(compound="left",label="Play scale", command=play_scale, accelerator="Alt+L")
    top.bind_all("<Alt-l>",play_scale_hotkey)

    #About menu
    about=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=about,compound="left", label="?")
    about.add_command(compound="left", label="Help", command=helpbox)
    about.add_command(compound="left", label="About", command=aboutbox)


#choose color
def pick_color():
    global color
    global RGBcolor
    global pickcheck
    global oldcolor
    global colorsave
    #RGBcolor=0
    color = colorchooser.askcolor(title ="Choose color")
    ColorDisplayFrame.configure(bg=color[1])
    colorconv=color[1]
    colorsave=str(color[1])
    if str(colorconv)!=("None"):        
        RGBcolor= hex_to_rgb(colorconv)
        oldcolor=colorconv
        pickcheck=1
    generate_chord(RGBcolor[0],RGBcolor[1],RGBcolor[2])

def pick_color_frame(event):
    pick_color()
    
#convert Hex to RGB
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    
def play_chord():
    global chord_play
    #print (chord_play)
    if chord_play!=[]:
        c_one=musicpy.chord(notes=chord_play,interval=0, duration=2)
        musicpy.play(c_one,100)
        copyfile("temp.mid","chord.mid")
        remove("temp.mid")

def play_chord_hotkey(event):
    play_chord()

def play_scale():
    global scales_display
    global scales
    if scales!=[]:
        index=scales_display.current()
        octave=5
        c=musicpy.chord(scales[index],interval=0.3,duration=0.3)
        musicpy.play(c,100)
        copyfile("temp.mid","scale.mid")
        remove ("temp.mid")

def play_scale_hotkey(event):
    play_scale()

def save_chord():
    global midifilename
    if os.path.exists("chord.mid")==False:
        play_chord()
    if os.path.exists("chord.mid"):
        data=[('MIDI','*.mid')]
        midifilename=asksaveasfilename(filetypes=data, defaultextension=data)
        if midifilename!='':
            copyfile('chord.mid',midifilename)
            remove ('chord.mid')

def save_chord_hotkey(event):
    save_chord()

def save_scale():
    global midifilename
    if os.path.exists("scale.mid")==False:
        play_scale()
    if os.path.exists("scale.mid"):
        data=[('MIDI','*.mid')]
        midifilename=asksaveasfilename(filetypes=data, defaultextension=data)
        if midifilename!='':
            copyfile('scale.mid',midifilename)
            remove('scale.mid')

def save_scale_hotkey(event):
    True

def save_history():
    history_display.configure(state="normal")
    history_text=history_display.get("1.0", tk.END)
    if history_text!='':
        data=[('TXT','*.txt')]
        historyfilename=asksaveasfilename(filetypes=data, defaultextension=data)
        if historyfilename!='':
            historyfile=open(historyfilename,'w')
            historyfile.write(history_text)
            historyfile.close()
    history_display.configure(state='disabled')

def save_history_hotkey(event):
    save_history()

def erase_history():
    history_display.configure(state="normal")
    history_display.delete("1.0", tk.END)

def erase_history_hotkey(event):
    erase_history()

def QuitApp():
    okcancel= messagebox.askokcancel("Quit?","Do you want to quit the app?",default="ok")
    if okcancel== True:
        top.destroy()

def QuitApp_hotkey(event):
    QuitApp()

#Name Chord
def name_chord():
    global chordname_string
    chord_length=len(chord)
    chordname=[]
    chord_notes=[]
    chordname_string=''
    for n in range (0,12):
        if chord[0]==notes[n]:
            index=n
            for i in range (0,12):
                chord_notes.append(notes[index])
                index=index+1
                if index>11:
                    index=0
    #print (chord_notes)

    chordname.append(chord[0])

    sus=False
    sus_index=999
    ninth=False
    ninth_index=999
    seventh_maj=False
    seventh_maj_index=999
    seventh=False
    seventh_index=999
    sixth=False
    sixth_index=999
    eleventh=False
    eleventh_index=999
    ninth_maj=False
    ninth_maj_index=999
    thirteenth=False
    maj=False
    minr=False
    plusninth=False
    mincheck=False
    bfive=False
    fifth=False
    dim=False
    aug=False
    add_fifth=False
    minr_index=999
    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1
        #print (step)
        if step==5:
            maj=True
            minr=False
        if step==4:
            minr=True
            maj=False
        if maj==True and minr==True and plusninth==False:
            plusninth=True
            minr=False
            chordname.append(" 9+")
            plusninth_index=len(chordname)
        elif minr==True and mincheck==False:
            chordname.append("m ")
            minr_index=len(chordname)
            mincheck=True
        if step==8:
            fifth=True

    for n in range (1,chord_length):
        step=chord_notes.index(chord[n])+1
        if step==6 and sus==False:
            sus=True
            chordname.append(" Sus")
            sus_index=len(chordname)
        if minr==True and step==7 and dim==False and fifth==False:
            dim=True
            chordname.append(" Dim")
            dim_index=len(chordname)
            if minr_index!=999:
                chordname[minr_index-1]='delete'
        if dim==False and step==7 and bfive==False:
            bfive=True
            chordname.append(" Add5b")
            bfive_index=len(chordname)
        if step==9 and fifth==False and aug==False:
            aug=True
            chordname.append(" Aug")
            aug_index=len(chordname)-1
        if step==9 and fifth==True and add_fifth==False:
            add_fifth_plus=True
            chordname.append(" Add5+")
            add_fifth_plus_index=len(chordname)
        if step==10:
            sixth=True
            chordname.append(" 6")
            sixth_index=len(chordname)
        if step==11:
            seventh=True
            chordname.append(" 7")
            seventh_index=len(chordname)
            #print (seventh_index)
        if step==12:
            seventh_maj=True
            chordname.append(" 7maj")
            seventh_maj_index=len(chordname)
        if step==3 and seventh==True:
            ninth=True
            chordname.append(" 9")
            ninth_index=len(chordname)
            if seventh_index!=999: 
                chordname[seventh_index-1]='delete'
        if step==3 and sus==False and seventh_maj==True:
            ninth_maj=True
            chordname.append(" 9maj")
            ninth_maj_index=len(chordname)
            if seventh_maj_index!=999:
                chordname[seventh_maj_index-1]='delete'
        if step==3 and seventh_maj==False and seventh==False:
            add_ninth=True
            chordname.append(" Add9")
            ninth_maj_index=len(chordname)
            if seventh_maj_index!=999:
                chordname[seventh_maj_index-1]='delete'        
        if step==2:
            ninthb=True
            chordname.append(" Add9b")
            ninthb_index=len(chordname)
        if ninth==True and sus==True and sixth==False and(seventh==True or seventh_maj==True):
            eleventh=True
            chordname.append(" 11")
            eleventh_index=len(chordname)
            #print (eleventh_index)
            chordname[ninth_index-1]='delete'
            chordname[sus_index-1]='delete'

        if ninth==True and sus==True and sixth==True and(seventh==True or seventh_maj==True):
            thirteenth=True
            chordname.append(" 13")
            thirteenth_index=len(chordname)
            if ninth_index!=999:
                chordname[ninth_index-1]='delete'
            if sixth_index!=999:
                chordname[sixth_index-1]='delete'
            if sus_index!=999:
                #print (sus_index)
                chordname[sus_index-1]='delete'
            if seventh_index!=999:
                #print (seventh_index)
                chordname[seventh_index-1]='delete'
            if eleventh_index!=999:
                chordname[eleventh_index-1]='delete'
            

    length=len(chordname)           
    for x in range(0,length):
        #print (x)
        if chordname[x]!='delete':
            chordname_string=chordname_string+chordname[x]

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

def generate_chord(R,G,B):
    global notesnumber
    global counter
    global chordnotes
    global counter
    global chord
    global chordstring
    global chord_play
    global notelist
    global occurrences
    global clash_occ
    global chordsteps
    global scale
    global scales
    global stepstransposed
    global root
    global trycheck
    global chordok
    global chordmem
    global rootvalue
    global Hvalue
    global notevalue
    global octave
    global scalenames

    scalenames=[]
    chord_play=[]
    scales=[]    
    cmyk=rgb_to_cmyk(R,G,B)
    r=R/255
    g=G/255
    b=B/255
    H,L,S=colorsys.rgb_to_hls(r, g, b)
    H=int(H*239)
    if H<=239 and H>=228:
        Hvalue=0
    if H<=227 and H>=217:
        Hvalue=1
    if H<=216 and H>=198:
        Hvalue=2
    if H<=197 and H>=179:
        Hvalue=3
    if H<=178 and H>=103:
        Hvalue=4
    if H<=102 and H>=76:
        Hvalue=5
    if H<=75 and H>=50:
        Hvalue=6
    if H<=49 and H>=42:
        Hvalue=7
    if H<=41 and H>=34:
        Hvalue=8
    if H<=33 and H>=23:
        Hvalue=9
    if H<=22 and H>=13:
        Hvalue=10
    if H<=12 and H>=0:
        Hvalue=11
    #print (H,Hvalue)
        
    chord=[]
    rootvalue=int(Hvalue)
    #print (rootvalue)
    root=notes[rootvalue]
    chord.append(root)
    chordsteps.append(notes[rootvalue])
    chord_play.append(notes[rootvalue]+'2')
    notevalue=rootvalue
    #print (notevalue,root)
    counter=1
    octave=4
    for value in cmyk:
        try:
            interval=int(value/16.66)+3
        except:
            interval=3
        notevalue=notevalue+interval

        if notevalue>11:
            notevalue=notevalue-11
            octave=octave+1
        validate_note()
        chord.append(notes[notevalue])
        chordsteps.append(notevalue)
        chord_play.append(notes[notevalue]+str(octave))          
        counter=counter+1
    counter =1
    
    name_chord()        
    chorddisplay=''
    for item in chord:
        chorddisplay= chorddisplay+item+" "
    #print ("\n"+"Chord: "+chorddisplay+"\n")
    history_display.configure(state='normal')
    history_display.insert(tk.END,"\n"+chorddisplay+"\n")
    chord_display.configure(state="normal")
    chord_display.delete(1.0,tk.END)
    chord_display.insert(tk.END,chorddisplay)
    history_display.yview('end')
    chord_display.configure(state="disabled")
    chord_display_label.configure(text="Chord: "+chordname_string,anchor="w", justify="left",font=("Arial",12))    
    guess_scale()
    init()


def generate_chord_hotkey(event):
    generate_chord(RGBcolor[0],RGBcolor[1],RGBcolor[2])

def validate_note():
    global notevalue
    global octave
    for chordnote in chord:
        if notes[notevalue]==chordnote:
            notevalue=notevalue+2
            if notevalue>11:
                notevalue=notevalue-11
                octave=octave+1
            validate_note()

def guess_scale():
    global match
    global matchlist
    global scale
    global scales
    global stepstransposed
    global stepsitem
    global root
    global stepscale
    global stepscales
    global scalenames
    match=0
    matchlist=[]
    stepscale=[]
    stepscales=[]
    chordlen=len(chordsteps)
    stepslen=len(steps)
    for n in range (0, stepslen):
        scalelen=len(steps[n])
        for m in range (0,scalelen):
            transpose=steps[n][m]+rootvalue
            if transpose>11:
                transpose=transpose-12
            stepsitem.append(transpose)
            transpose=0
        stepstransposed.append(stepsitem)
        stepsitem=[]
    #print (stepstransposed)
    #print (chord)
    for n in range (0, stepslen):
        scalelen=len(steps[n])
        for m in range (0,scalelen):
            for o in range (0,chordlen):
                #print (chordsteps[o],steps[n][m])
                if chordsteps[o]==stepstransposed[n][m]:
                    match=match+1
                    
        matchlist.append(match)
        match=0


    for n in range (0,stepslen):
        if matchlist[n]==max(matchlist):
            #print (steps[n])
            #print (stepstransposed[n])
            for x in range (0,7):
                noteindex=stepstransposed[n][x]
                scalenote=notes[noteindex]
                scale.append(scalenote)
                stepscale.append(noteindex)
            scalenames.append(stepsnames[n])
        if scale!=[]:
            scales.append(scale)
            stepscales.append(stepscale)
        scale=[]
        stepscale=[]
    scalestring=''
    #print ("Scales:")
    history_display.configure(state='normal')
    history_display.insert(tk.END,"\nScales:\n")
    guess=1
    i=0
    for item in scales:
        for note in item:
            scalestring=scalestring+note+" "
        #print ("Match",str(guess)+": ",scalestring)
        scalecombo.append(scalestring)
        history_display.insert(tk.END,"Match"+str(guess)+": "+str(scalestring)+scalenames[i]+"\n")
        guess=guess+1
        i=i+1
        scalestring=''
    scales_display.configure(value=scalecombo)
    scales_display.current(0)
    scales_display_label.configure(text=scalenames[0])
    guess=0
    #print ("\n")
    #history_display.insert(tk.END,"\n")
    history_display.yview('end')
    history_display.configure(state="disabled")
    #print (scales)

def scales_caption_display (event):
    
    scales_index = scales_display.current()
    scales_display_label.configure(text=scalenames[scales_index])


#CopyContextMenu
def create_context_menu():
    global menu
    menu = tk.Menu(rootw, tearoff = 0)
    menu.add_command(label="Copy", command=copy_text)
    rootw.bind("<Button-3>", context_menu)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
        
def copy_text():
        history_display.event_generate(("<<Copy>>"))

#About
def aboutbox():
    global aboutbox
    #print ('about')
    aboutbox=tk.Toplevel(top)
    aboutbox.geometry("500x240")
    aboutbox.resizable(0,0)
    aboutbox.title("About")
    about_label=Label(aboutbox)
    logo=b'iVBORw0KGgoAAAANSUhEUgAAAaQAAABaCAYAAAD3oyLoAAAmTElEQVR4nO2dd3RVxfbHv7ff3PROCkFISAESIglgeCAdHqigiEoRiFRBQH9IL5FiQ3Gh1LfyaFLUIE8CKB2SiJEuRIQQeISSEFJIbzf3nnPm9we/c34pN8k5yb0hkvmsdZaLeGbPvnNmZk/Zs0cGgIBCoVAolKeM/GkrQKFQKBQKQA0ShUKhUJoJ1CBRKBQKpVlADRKFQqFQmgXUIFEoFAqlWUANEoVCoVCaBdQgUSgUCqVZoKz+B7mc2igKhUKhWBZCCAipegy2ikFq3749tm7dChsbG3Ac16TKUSgUCqVloFKpsHHjRkRHR1f5exWDZGVlheeffx42NjZNqhyFQqFQWhaenp41/lbFIBFCYDAYwDBMjRmSTCazrHYUCoVCeeaoviwHAGq1GizL1vh7jT2k6sjlciiVSpOJKRQKhUKpDZlMBrlcDqPRaNIwVadOgySXy1FcXIxVq1bh2rVrZlOSQqFQKM82hBDI5XIMHjwYM2fOhFwur9co1WmQlEolfvrpJ6xdu9asilIoFAqlZXDq1ClEREQgIiICRqOxznfr9fHOzs42m2IUCoVCaVlwHIeCggJRfgii9pB42rZti8jISFFTLwqFQqG0PORyOUpKSrBx40YUFxcDEO8UV69Bqkzbtm0RFRUlXUMKhUKhtBgKCgqwc+dOwSCJRZJBYlkW5eXlUCqVdIZEoVAolBooFAqUlZU1yEbQOEEUCoVCaRZQg0ShUCiUZgE1SBQKhUJpFlCDRKFQKJRmgSSnBksjk8mEpzJ8mHLqSEGhUCjPLk/NICkUCigUiip/MxqNKCsrQ0VFhRA7T6FQQKlUwsrKClqttoYcU4FgKc0LtVot+l2xMa+edVQqleizG3W1gad9vxkdSFKk0KQGiQ/UCgCZmZlISUlBcnIyrl+/jvv37+Px48coLS2FXq8XDJJSqYRSqYROp4OdnR08PDzg5+cHPz8/tG/fHu3atYOzszNkMhkIIWAYhjaAZoJMJoPBYMC6detw//79OjtHQgisra3x4YcfwsHBoUUPMpRKJXbv3o3z58/XGLRVhxCCadOmISgoCAzDVPl/HMdBr9c/tUj9hBCh/VIoYmiSmsIbory8PJw4cQKxsbE4e/Ys0tLSGtXxaLVaeHl5oXPnzhg4cCBefPFFBAQEQKFQ0JlTM0Amk4FhGOzcuVNUcF4bGxtMnToVTk5OLfrbyeVyHDlyBN9//72o9wcPHoyOHTtW+ZtKpUJiYiImT578VA3SO++8g/nz59cbw4xCAZrAIKnVapSWlmLr1q3YsGED/vrrL7PJ1uv1uHPnDu7cuYOffvoJ9vb26Nu3L0aPHo0hQ4bA1taWGqZmgNglO41GQ+/d+j9UKpXod03NPGUyGUpLS5GSkmJOtSSTmZlJvylFNBZdYFar1UhJScGIESPw7rvvmtUYmaKwsBCxsbF46623MGDAAOzatQssy9a77EGhPIs0B0NA2x5FChYzSGq1GteuXcOwYcNw/PhxS2VTKxcuXMD48eMxfPhwpKen04ZBoVAozRyLGCS5XI7c3FxMmjQJt27dskQWolGpVLC1taWODhQKhdLMsYhBUiqViI6OxsWLFy0hXjRDhgzBzp07W7zXFoVCofwdMLtTg1wuF0KPS8He3h4dOnSAt7c3bG1toVKpYDAYUFZWhsePHyMjIwMPHjxAaWmpKHl9+/bFjh074ODgQD18KJSnBH98g0IRg9kNkkKhwI0bN3D37l1R78vlcsycOROzZs2Ch4cHrK2ta7yj1+sFw5SUlITffvsNJ06cQHJyskmZL7zwAnbu3Ak3NzcYDIZG/Z7mjqkDxjyEELAsK2l2WJc84MnZFpZlm3QJVCaTQaFQ1HvIk2VZi3WAfP5iHQU4jhOevwMKhQJt2rSBRqMx27dlWRYeHh6S0/Hf21TUFlMQQoSyflpL87W1G3PXycpnOU0hNb/65DV1eze7QZLJZMjIyEBFRYWo94ODg7F69WpotVowDFPjpD5fOe3t7eHo6Ah/f3+88cYbKCgoQEJCArZs2YIjR44IH6Fz587YvXs3vL29YTAYIJPJJLnQAtKjBUg5VQ/8/8l6qbpVNq58no8fP8bt27dx8+ZNZGdno6KiAjqdDh4eHujQoQN8fX1hZ2dXb0XlXbOzs7ORmpqKlJQUZGdnC/dfOTs7w9/fH/7+/vD09BQOvVoSvpEbjUakp6fj3r17uHv3LnJyclBeXg7gydklDw8P+Pv7w8fHBy4uLgDME/Gh8nfNy8tDbm4uHj58iPT0dOTl5aGkpARGoxFyuRxqtRp2dnZwdXWFj48P3N3d4eLiIgywLGkszYGdnR327duHgIAAs60oEEKElY76qNwxGgwGZGZmIjs7G/fv30d2djYKCgqECC585BYnJyd4eHigdevWcHFxgYuLi3CbtZQD8mLbIcdxVQ4fV06XlZWF9PR0ZGRkoLS0FEqlEnZ2dujUqRNcXV0FXRoatYRvC4WFhbhz5w6Sk5Px6NEjlJWVQaPRwM3NDYGBgfD394ezs3MNXavD1+38/HzcvXsXKSkpyMjIQFlZGWQyGRwdHdGuXTsEBgaidevWUKlUTRJFxSLnkKR0VI8fP8bNmzcRGhpaxVLzox3+v9UbtI2NDYYPH46XXnoJv/zyCxYsWACWZfHdd9/B19cXBoMBcrkceXl5iIqKQmFhoSh9HB0dsWrVKjg4OIjqQFQqFU6ePIlt27aJ/s2LFy9Gx44dkZ+fjxUrViAnJ6feNJ06dcKCBQuERp6SkoItW7bg559/xq1bt0yOxNVqNUJCQvDWW29hwoQJcHV1rfFt+Ip+7tw57NixA6dPn8adO3dMypPJZPD09ETfvn0xZcoU9OrVSxhBmRO+g09PT8fBgwdx8OBBXLlyBTk5ObU2CKVSCV9fX/Ts2ROjRo3Ciy++CLVaLdlo8p0MIQS3bt1CQkICTp8+jRs3biA1NVXUxWNyuRxOTk4ICAhAaGgoBg4ciIiICLi5udXbUTwtZDIZdDoddDqdWfWrL3QQX/+Kiopw6dIlnDx5EhcuXEBKSgoyMzNF6aLRaODj44OAgAD07t0b/fr1Q6dOnaBWq+vtRBUKBbKysrBgwYJ685o4cSL69+8PhmGgVCrBcRyOHz+OXbt2ITExEQ8ePKjRFqKiorBixQrByEdFReH27dv1/qZWrVrho48+go2NDZRKJTIyMrBjxw785z//wbVr10wOGuRyOQIDA/Hqq69i0qRJaNeuXY36zxv+5ORk7Ny5E4cPH0ZycnKtgxBnZ2f84x//wMSJEzF06FAolUqL11/CP8HBwSQ3N5cYjUZSUVFBCCHk888/F/5/7969SVlZGTEYDKSiosLkQwghsbGxpLLc+h5PT08yceJEsnHjRnL06FFy8eJFcuvWLZKVlUX0ej3hOI6YgmVZwjAMIYSQe/fukeTkZEIIqaIPwzDk/fffl6TP1q1ba8gx9RgMBmIwGMjAgQNFy+7evTspKCggHMeR9PR04uHhISpdr169CMdxhGVZsmnTJuLm5ibpNwUHB5NTp05V+V2EEJKVlUVmzJhBdDqdJHlarZbMnj2bFBYWEpZlTZaP0WgkBQUFJCwsTJRMZ2dnkp6eTkpKSsjnn39OfHx8JOnEPwqFggwdOpScO3eOEELqrK+VH47jCMMw5OTJk+TNN98kTk5ODcrf1OPn50cWLlxIbt26RQghQhurrQ2NHz9etOzDhw/XqK+EEHLs2DHRMpycnMiNGzcIx3Giyqqxj8FgIIQQ8ujRI7JmzRrSuXNnIpPJzFLWVlZWZMCAAeSHH34gpaWldbZljuNISkqKKLnr168X+p579+6R0aNHE4VCUWeaJUuWCHXQaDSKbgs+Pj4kOzubEELI/v37iZ+fn6Qy8Pb2Jrt3765S/1mWJSUlJWTlypXE2dlZkjyZTEbefPNNkpaWVm/fyDAMefjwYZW+rXodJYSQZcuWmcrr//9hDoPEcRy5dOmS5A6ueoVydXUl7dq1IyEhIaRfv35kzJgxZM6cOeSLL74ge/bsIXFxcSQ5OZkUFhYKRslU58MwDMnMzCQBAQGi8+/atSspLi6us9Pgy+fXX38lGo1GlFylUkmOHDlCCCHCR2vbtq2otAMGDCCEEPLRRx81uFwdHR3JwYMHhbK6efMm6d69e4PlASDDhw8nBQUFhGGYRhskNzc3cvLkSdK/f/9G6cQ/dnZ2ZMOGDYRl2XqNEl8eo0aNIiqVyiz5m3pcXV3JJ598QoqKimrt/J+GQXJ2diZ37941OfBrDLV1WAzDkB07dpD27dtbrKwBkD59+pBff/3VZN/A91e3bt0S1YY3b95MCCHkr7/+Ip06dRKV/9KlS4W8jUYj6dGjh6h0/v7+pKioiHz77bdEq9U26LcrlUqybt06QsiTwXtOTg559dVXG1WeYWFh5O7du7UOQhtrkMy+ZMeyLPz9/eHr6ysqfpkpysvLUV5eXudSFr9G6+zsjODgYERERKBPnz4IDg6GRqMRpuosy8Ld3R1Lly7F+PHjRa2BXrp0CUePHsXIkSPrXPIhhGDr1q2i98tefvll9O/fX9h3kIJGo8H333+PlStXSkpXmfz8fEybNg0BAQGwt7fHmDFj8McffzRYHgAcOHAAy5Ytw9dffy0EuG0oRUVFGDduHB49etQonSrLmzVrFoqLi4UlGVP6qdVqxMbGYvbs2UhLSzNL3rWRk5ODJUuWID4+HtHR0XjuueeaheNNeXk5tmzZAnd3d7MtwXp6emLYsGFQKBRCuSuVShQXF2Pu3LnYsmWLWfKpi/j4eAwdOhQff/wxZs2a1agNeqVSiYKCAkycONHiUWc0Gg3OnDmD999/H3q9vkEyGIbBggULhKXMyZMn48CBA43S6/Lly5gxYwb27dsHtVptEacdwTqZY4ZkKl1TPTqdjgwcOJDs27ePGI1GwYobDAai1+vJkCFDRMvq168f0ev1tc6SWJYl169fJ46OjqJ1+/3334VRgtQZUmhoqNlGkyNHjiRjxowxW7mr1eoay4ENmSFZ6lEqlWTv3r0mR+yEEPLDDz8QGxubJtfr+eefJ3fv3q0xUyKk6WdIlnjCw8NJaWmp0IaMRiMpLCwkr7322lPR5+OPPyYcx1Xpv6TMkLZv306WLl0qKc+GzpB8fX3N1m66detGPvzwQ7OWZXR0dJ0z4IbOkCxyMJZlWUyaNAldunSxhPhaKSsrw4kTJzBy5EhMmDAB2dnZUCqVIIRAo9Fg+fLlsLW1FSXr119/RXx8fK0ukXK5HLt27UJ+fr4oeaNHj8YLL7zQ4NFwUlKSqM1QMezbtw/fffedWWQBT5xYNm/eDJZlzR4/zcrKCh4eHvDx8YGnpyesrKwky2AYBosWLUJGRkYV11yVSoULFy5gxowZKCkpkSzXwcEBHh4ecHd3h06nk5z+ypUrmDp1KkpLS5/6vUWWoPq3ksvlWLZsGfbv3y9ZlkqlgqurKzw8PODs7NwgfZYvX46YmBjJXrfAE6eP69evN8msDgBSU1Nx+fJls8i6cOECvvrqK7PI4tm0aROKi4vNXm8tZpBcXFywZcsW+Pr6WiKLevnuu+8wZswY5OfnQ6FQwGAwoFu3bpg2bZqo9AzDCJ1sdRQKBR49eoQ9e/aIkuXk5IT/+Z//kaR/dUwtM9jY2EhyI60PrVZr8hyYGOLi4nDv3j2zxQzs1asXNm3ahPj4eJw7dw4XL17EuXPnkJCQgK+//hqdO3eWJO/OnTvYs2ePoJ9cLkdFRQWWLFmCvLw80XKsra0RGRmJ/fv348yZMzh79izOnj0rLMG9+OKLkvQ6ceIEtm3b9szfGaRWq3H69Gls3rxZUrqOHTti9erVOH36NH7//XecP38ev/32G44fP465c+fCzc1NtCyGYbB48eIaAxMxyOVyHDhwAFlZWZLSNRRT7d3a2rpBA7LaUKlUsLGxaVDaa9eu4dKlSxapt8J0yVxLdtU3il9++eWnMkUHQObNmycsiTAMQzIyMoivr6+otFZWViQxMdHkksq6desk6VB9eit1yY5/bGxsyAcffEDi4uJIUlISuXjxItm2bVujpvc9e/Yke/bsIZcvXyZXr14lhw4dIiNHjpTs9VR9WawhS3bW1tZk/fr1pLy8XNgYZxiGGI3GKs4r+fn5ZMaMGZL0CwsLE+ovIYQcPnyYyOVy0en9/PxIfHy8oAPvlceyrPA3vV5P1qxZI9rRBQAJDAwkubm5gmPIs7Jk16tXL2HJjmEY8sorr0hKP336dJKbmyuULe9VW7m8k5OTSZ8+fSTJ/fLLL4XykrJk15Bn0aJFDVqy4x+lUknefvttcvjwYXL16lXyxx9/kB9//JEMHjy4wTp16NCBbN68mVy4cIEkJSWRkydPknfffVey88TKlStNLts1Ky87U14s5eXlJCYmhgwcOLBR3ncNeZydncmdO3eE/SRCCNm+fbvoznbcuHFVDBK/Dh4aGioqvZeXF7l3714NL7SGGCSdTid0+nyHyPP48WMyYMAAyeXz5ptvkqKiohoyOY6TvF7+0UcfNcogyeVy8s033xBC6naL5vfw9Hq9pE7O1taWJCUlEY7jCMdxZNq0aaLT2tnZkd9++81kA6y+b0YIIVFRUZLKrnKDfdYMEu9aLXa/FQB5/fXXq+wD1zXoffDggaT91R49ehC9Xk8MBkOjDZJMJiMdO3Ykb7zxBpk9ezZZtGgR+fDDD8nkyZPJ4MGDyaZNm4R9K6kGSSaTkdWrV5ts73q9nkyePFmyvj169CDp6ekmZW7btk1SOYwYMeLvZ5B4o8Qrk5SURL755hsyduxYEh4eTlxcXBrs1ij22bFjh5A/7+AwaNAgUWkrd2J8mezdu1d03p999lmdH02KQZoyZYow2jLVMM+fPy/J4Ht6epLU1NRa9SstLSVdu3YVLS8yMrJRBik4OJgUFRXVa4wq/+ZTp07Vexak8hMbG0sIIaS8vJw8//zzkn+bmLrPsizJzMwkrVu3Fi0/KirqmTNI//jHP4RzQPv37xedzsrKipw9e7Ze41/5t65du1a0fDc3N/Lf//6XsCzbKIM0dOhQcvz4cZKXl0dMYTAYSGlpqdDvSDVIffr0EdqRqT41PT1dUh3TarWCC3x1efyqwahRo0TLe+GFF4S05jJITXJjbFpaGgwGA3x9fRESEoKQkBAQQlBaWoqioiKkpaXh4cOHePToER49eoSHDx8KT15eHsrKylBaWtpgd9TKLpqkkoPD77//Xu9mdnFxMaKjo7FhwwZh3+Hf//63qHwDAgIwadIks7jRKpVKvPHGG8JvqA7DMAgJCUHnzp1x9uxZUTIHDRqEtm3bmnS0YFkWOp0OI0aMEB21vaCgoFFuoF26dIGNjY3ok+Acx6F9+/Zwd3dHRkaGaB2BJy7hYiJk8PTu3RuA6bKvDr+HGhYWJtqN/MGDB6J1sQQymQxardZsm9SEkCqOHvfv3xed1sfHBx06dJAUESAiIgIajUbUEQw+DJSvr2+DXcDfe+89fPXVV9BoNGBZ1mREiMpRPxrCyJEja402YjQa4eXlhb59+4oOZB0WFoZu3bqZLFdex1GjRiEmJkaUzmVlZdDr9dDpdGYLKWRRg6RWq/HXX39h/PjxKCgowObNmzF48GAh3IxWq4WVlRU8PT2rpCOEwGg0gmEYFBUVISsrC9nZ2Xj48CFu3ryJn3/+GdevXxetR25ubpV/GwwGREREYNKkSfjmm2/qTR8TE4PZs2fD398fiYmJiI+PF5XvnDlzTIbraQhOTk5o165drR0+b2iDgoJEG6TQ0NB635HiKdnY39kQ76f6gkNWh284BoNB0kDB3t5ekl4ymUxSGr7sntYtr3Z2dti+fTuee+45s4SGIYTA1tZWcB6QcpbGysoKVlZWojs5QgisrKxEGySGYRr1G7t27YpPP/203jh9jemkZTKZKMedoKAg0TJDQ0Oh0Whq1ZkQIsS+FBNqrbHlaAqLGCR+ZJCQkIDIyEjcu3cPAPDaa6/hvffew5w5c+Dh4SHEp6veMfBRfnlXT3d39yoNdc6cORg0aBCSkpJE61MdjuMwd+5cHDhwQNCvNh4/fozt27fj008/RXR0tKjgk+Hh4Rg1apTZPphOp4OtrW2dBkkmk8HBwUG0TFdX13rfsbe3F33gtbGjpLt370oqL7lcjpycHGRnZ4tOw7v9W1tbS/JQlDqDYVlW0iFbXi9zjTSlolAoEBwcDD8/P7PJrBy3T0q9zM/PR15eHlxcXEQNGvggw2KvptFqtdBqtaL1qZ7X1KlTYWdnZ9EDzVqtVtTFolLKlQ88XBscx8HW1hY6nU507E9zY3a3b96QxMTE4LXXXqvS2ZeXl2PNmjXo2bMn1q5di8zMTKjVaqjVaiHcPAAhICP5v0gLRqMRBoMBRqMRHMfBzc1NVGfKY+rcAsMw8Pb2xuLFi0XJ2Lt3L+Li4nD48OF635XJZJg/fz7s7OzMdpJZoVCImglImS2ImZHI5fImu/794sWLuHHjhqSZ0sGDB0WPvrVaLby9vQE8cZn38fERnc+hQ4dER9hQqVRITk7GpUuXRMtv37696HctBb/sZDAYzPJUHlz4+fmJnv2lp6fjzJkzouodL/PAgQOiZ7xubm4NjkhhZ2eH3r17W/xakfqugeGR0t7FDMDEXPNiScyaM798snbtWkyYMKHWQ6OpqamYM2cOIiIiMHPmTBw7dgy5ubmQyWSCgTL1KJVKFBYW4ssvv8SZM2dE6xUSEmLy7wzDYOzYsejbt2+9Mu7fv4+pU6cKexB10a9fP7zyyivNMqpzc6aoqAiLFy9GYWEh1Gp1rR0YHw387Nmz2LBhg2j53t7e8Pf3B8uyUKlU6NOnj+i0cXFx+Ne//gWlUllrJ8DX35KSEixbtgxFRUWiZKtUKvTq1eupzY4sDcuyCAoKQuvWrUW/v3z5cty/f7/OeqBQKKBSqXD06FHs2LFDtD6hoaHCCo1UPD090apVq7/NPVd/N8y2ZMcfPl24cKHoU8FpaWnYuHEjNm/eDC8vL4SGhgr32tjb2wsbhqWlpcjOzsbt27dx9uxZSRELXF1d0bNnT5MViOM46HQ6LF++HOfOnRPu2DEFy7K4c+dOvfmp1WosXLgQWq22WcQo+7tx+PBhvP766/jkk0/QpUsXk6M6vV6Pn376CfPnz5fkmDBo0CA4OjoK92SNGDECa9euFRWlgeM4zJs3D7m5uZg+fTrc3d1rvEMIQVJSEpYsWYJffvlFtF69evVCSEjIMzuAYVkWnp6eGD58ONavXy8qzfXr1/Hqq6/iyy+/FK4SqU5xcTFiYmKwZMkS0cYfAN5+++0GzwIcHR2F6C8U82MWgySXy1FUVIRp06bhxx9/lJye4zikpaVZJLDl2LFj6wxgaTAY8OKLL+Kdd97Bpk2bGp3f8OHD0bdvX3pteiM4deoUEhMT0bt3b3Tv3h1t27aFTqdDWVkZbt++jYSEBCQmJkqSqdPpMGHCBKEj4b0SIyMjRc+yKioqsGLFCuzatQv9+/dHaGgonJ2dwTAM0tPTcf78eZw8eRLFxcWi9VKpVJg3b94zP4DhOA4zZ87E3r17RUc7uHr1KoYMGYLevXujZ8+eaNeuHbRaLYqKipCcnIy4uDhcuXJFkh79+/fHSy+91OD22VTL1y0Vs82Q+OWK5kRgYCDmzp1b79Sc4zjMnz8fhw4dapRRtLGxwbx58yCXy5v17aB/B/R6PY4dO4Zjx46ZRd7kyZPRtWvXKrMQQgiWLFmCc+fOSdrvSU1NRWpqqln0mjNnDgYPHvxMGyPgyQDA398fq1evlnQUgmEYnDp1CqdOnWq0Dp6enlizZg2srKzogLGZYpY9JN47Y/v27di0aRM8PDzMIbZReHt7Y/v27fDy8qq38jMMgzZt2mDRokWNynPs2LHo2rUrrewNRKPRWERuREQEli5dKtw+zMOyLFq1aoWdO3ciODjYInnXxdSpU7F8+fIWM3gxGo0YP348PvvssyaP3efu7o4dO3YgNDSUts9mjNmcGvhGNX36dCQkJGDKlCmws7Mzl3hJhIWFITY2VlJ0baPRiAkTJkgOjsnj4uKCDz74gG52NoJx48ZhxowZZpXZvXt37Nq1q1YXYoPBgKCgIBw8eBDDhg0za961YWNjg1WrVmH9+vVQqVQtps4QQsAwDObNm4dt27Y12cA1PDwcBw4cwMCBA5/5mejfHbN62fEuo35+foiOjkZCQgLee+890d41jcXNzQ2LFy/G0aNHERYWJqny8SfLly9f3qAzClOmTEFgYOAzuTHdVBu4PXr0wLp167BixYoGRyHmkcvliIyMRGxsLHx9fescFRsMBrRp0wYxMTGIjo5Ghw4dGpV3XTr985//xJEjR7B06dJmtbTbVN+YP/Q+btw4xMXFITIyssER5uvD09MTK1aswNGjR9G9e3eLHWK1BM1Nn6bCIg7n/Lmh0NBQbNiwAefOncP27dsxcuRIeHl5mTUvjUaDkJAQrFixAmfOnMEnn3wieFI1RO++ffti8uTJkk7M+/j4YMaMGQ0a6UqZwYlBSgcnRl/+LJgYajPGYnSXyWTo2LEjFAoFoqKicPz4cbz++uuSOyutVouBAwciNjYWW7ZsgZubm6gyNhqNUCqVmDJlChISErBlyxYMGjRI0sHD2vDy8kJkZCSOHj2KAwcOoGfPnjAYDHWWv5SBTW1ypNRHU6FvLAU/cPX398e2bdsQHx+POXPmwN/fv0HROipjbW2N7t2744svvkBiYiKioqLg4OBQrzES274au9wnJR8x30PKNxbTjvlvIwZLLH1adCGX/2Hu7u6IjIzEuHHjkJ2djcuXL+Pq1au4cuUKbty4gYKCAhQVFaGsrKxOeVZWVsK15UFBQejevTsiIiLQuXNn4VRzXYWpUqmqGBr+g1c3PgMGDEB0dLToDzNr1ix4e3tLMoL8vtv69evrveiK4zjY2dlBq9XWWUkZhsHo0aMRHBxcpzcQL6O2uFaV5T333HPYvXs3OI6r00hzHAcvL68qDYQQArVajU8//RS5ubm1/kb+vaCgIKEhRkREICYmBklJSTh69Cji4+Nx+/ZtFBQUoKKiAizLQqlUCnWiffv26NmzJwYMGICwsDCo1WrJnSzHcTAYDHB0dMSkSZMwbtw4pKam4vz58/jjjz/w559/Ii0tDSUlJSgvL4fRaBQuJVQoFNBoNNDpdLC3t4evry+6dOmCsLAwhIeHC8tT/GCtLhiGwfTp0zFo0CBR39GUyzjDMOjUqRO+/fbbel2c+bBTrVq1atIZm9FohEwmQ3h4OMLDw7F06VJcvXoVFy5cwNWrV5GSkoLHjx8LMdMYhgHHccIhcSsrK9jY2MDd3R0dO3ZEly5d0K1bN3To0AE6nU74nnXBsixcXV2xe/fuei+Y5DgO7u7ukMvlko03//7KlSuRnZ1d5zchhEClUsHT07PO78EwDPr06SPqGzMMgy5dutTZ3jmOg729PTZv3lzvpZEcx8HR0bHePkkqMjyJsgoACA4ORnx8vBBhQK1WY/Xq1Vi4cCGAJwEmjxw50mA/fJlMVuXkP8dxKCsrQ05ODnJycoTKxwdT5Q9A2tjYwNbWFg4ODnBzc0OrVq2qBILkK2pdKJVKxMTEICUlBcHBwfD09IROpxPiUeXk5ODPP/9EXFwcEhMTRR2ABZ50BqdPn4aDg4PkxsxHtRCLGINX3ejWhamwTdWRGivOlI5ivS+rG5DK5cMwDAoKCpCZmYmSkhIYjUZoNBrY2trC3d0d9vb2Qr0y12ifNzR8PWNZFiUlJcjNzUVRURH0er0QvUGlUkGn08HBwQHOzs7QaDRV0lV3qKgPKR6rtX1Hqd+uKWdJpqisLz+4zM/PR35+PkpLS4X4g0qlUvj2Tk5OsLOzg1KpFOq91N9hiXZYG1K+q5jfoVQqRZ+pqhzKqTbMURYKhQJZWVkIDw/Ho0ePADw5XzhkyBDhfbVajaioKKxatapK2iZ1deGXfyo3Ho1GgzZt2qBt27aiZPCBWaXu1cjlcpw5c6bKjZXW1tZQqVSoqKio81BsbSgUCixfvhzOzs4NqqRSpsdiMfc0Wswosz4amr5y+fBx+pydnasYXI7jhMfco3t+E55HJpPB2toatra2QrzF6u9X1qUx+4nmqBfm+HZNSXV95XI5XF1d4ebmVqPT5UOL8Ya+MfXeEu2wNsydj7n3rJuyLEzx1O9Nrt7oLUl1yy82GGNtvP322xg2bBh1I20CKndALVmHloSU/UvKs8HTi6L3N6dLly5YvXo1gJbrEUOhUCjmhBqkBhAQEIBdu3Y1OGIwhUKhUGpCDZJEevTogdjYWHTo0OFvtT5PoVAozR1qkERib2+PefPm4dChQwgMDKTGiEKhUMzMU3dqaM7IZDIEBgZiyJAhGD9+PDp37gyWZakxolAoFAvQYgwSwzCYOXMmunbtitu3byMjIwOFhYWoqKgQbhy1srKCtbU1XFxc0L59e4SGhiIoKAjOzs5P3R2SQqFQnnVajEHiOA6+vr5Vroqufi7K1DXhdEZEoVAoTUOLMUhAzUNk/MFG/tAdf8COunFTKBRK09OiDFJ1qOGhUCiU5gP1sqNQKBRKs4AaJAqFQqE0C6hBolAoFEqzQNIeklwuh1arlXR5HYVCoVBaFhqNpkF2QpJBysrKQkxMDBQKBXUIoFAoFEoN5HI5CgsLG3SlT70GqbLhuXHjBkaPHi05EwqFQqG0XMROYOrdQ7KxsWm0MhQKhUJpuWi1WlHv1TlDYlkWw4cPx8mTJ5GcnEz3jigUCoUiCkIIZDIZ+vXrh65du4q6yLReg+Tp6YkffvgBJSUlZlOUQqFQKC0DBwcHABB103K9e0gsy0KhUMDR0bHRilEoFAqlZcFxnOg9pCoGSSaTQaFQQKFQ0OU5CoVCoTQaPlaomL9XMUhGoxEZGRkoLi4WNb2iUCgUCkUqarUaRUVFNf4uAyDMpVQqFVxdXensiEKhUCgWgz+rVN0oVTFIFAqFQqE8LWgsOwqFQqE0C6hBolAoFEqzgBokCoVCoTQLqEGiUCgUSrOAGiQKhUKhNAuoQaJQKBRKs+B/AXqF+j60xHAuAAAAAElFTkSuQmCC'
    logoimg=tk.PhotoImage(data=logo)
    about_label.place(x=35,y=40,height=102,width=430)
    about_label.configure(image=logoimg)
    about_label.image=logoimg
    about_label.bind("<Button-1>", lambda e: callback("https://symbolform.com/"))

    url_title=Label(aboutbox)
    url_title.place(x=35,y=10,height=40,width=430)
    url_title.configure(text="Color to Chord 1.3.2", font=("Arial",15))
    url_title.bind("<Button-1>", lambda e: callback("https://symbolform.com/"))


    url_label=Label(aboutbox)
    url_label.place(x=35,y=152,height=15,width=430)
    url_label.configure(text="https://symbolform.com/")
    url_label.bind("<Button-1>", lambda e: callback("https://symbolform.com/"))

    url_label2=Label(aboutbox)
    url_label2.place(x=35,y=172,height=30,width=430)
    url_label2.configure(text="https://symbolform.com/turn-colors-into-chords/")
    url_label2.bind("<Button-1>", lambda e: callback("https://symbolform.com/turn-colors-into-chords/"))

    close_button=Button(aboutbox)
    close_button.place(x=220,y=200,height=30,width=40)
    close_button.configure(text="Close")
    close_button.bind("<Button-1>", close_aboutbox)
    
def close_aboutbox(event):
    aboutbox.destroy()

def callback(url):
    webbrowser.open_new_tab(url)

def helpbox():
    global helpbox
    helpbox=tk.Toplevel(top)
    helpbox.geometry("440x540")
    helpbox.resizable(0,0)
    helpbox.title("Help")
    
    textbox1 = Text(helpbox)
    textbox1.place(x=20, y=20, height=470, width=400)
    scroll_2=Scrollbar (helpbox)
    scroll_2.place(x=421, y=20, height=470, anchor='n')
    textbox1.configure(yscrollcommand=scroll_2.set, wrap=WORD)
    scroll_2.configure(command=textbox1.yview)
    textbox1.focus_set()
    textbox1.bind("<Button-3>", context_menu)
    readme="Color to Chord 1.3.2\n\
SymbolForm\n\
\n\
The program will convert colors to chords.\n\
\n\
- Run the program and click on the empty gray frame left of the “Play Chord”\
  and “Play Scale” buttons. A color chooser window will open.\n\
- Choose a color or input values for Red, Green, Blue or Hue, Saturation,\
  Lightness.\n\
- The color will be displayed in the frame and the corresponding chord will\
  appear in the “Chord” textbox, followed by the chord name.\n\
- All the scales matching the chord will be displayed in the “Scale” combobox.\
  Click the arrow on the right to select one.\n\
- Click on the \"Play chord\" button or Play menu- Play chord to play the chord.\n\
- File menu - Save chord or Alt-C to save the chord as a MIDI file.\n\
- Click on the \"Play scale\" button or Play menu - Play scale to play the scale\
  selected in the \"Scale\" box.\n\
- File menu - Save scale or Alt-S to save the scale as a MIDI file.\n\
- You can import the MIDI files into a DAW or another kind of scoring program\
  supporting MIDI import.\n\
\n\
The text in the chord box and in the history window can be copied for use in\
another program or for sharing through right click -.Copy, CTRL-V or CTRL-Ins.\n\
It can also be saved to a text file through File menu - Save history.\n\
File menu - Erase history to erase the history window.\n\
\n\
New in this version:\n\
\n\
- Help and About windows added"
    textbox1.insert(INSERT,readme)
    textbox1.configure(state=DISABLED)
    close_button1=Button(helpbox)
    close_button1.place(x=200,y=500,height=30,width=40)
    close_button1.configure(text="Close")
    close_button1.bind("<Button-1>", close_helpbox)

def close_helpbox(event):
    helpbox.destroy()

def main():
    init()
    create_app_window()
    create_context_menu()
    
main()
rootw.mainloop()
