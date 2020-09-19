import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
#musicplayer.geometry("450 X 350")

directory = askdirectory()
os.chdir(directory) #chdir changes the current working directory to specified path.
songlist = os.listdir() #returns a list containing the names of the entries in the directory given by path
playlist = tkr.Listbox(musicplayer, font = "Helvetica 12 bold",bg = "yellow", selectmode = tkr.SINGLE)
#Select item
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos +1 #it will select a music and the position will be 1 next

#Pygame loads songs
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE)) #controlls streamed audio and also loads a music #ACTIVE makes the music active when the mouse is over it
    var.set(playlist.get(tkr.ACTIVE)) #set whatever the music is selected
    pygame.mixer.music.play() #plays the selected music

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(musicplayer, width = 5, height = 3, font = "Helvetica 12 bold", text = "PLAY", command = play, bg = "red", fg = "white") #we defined our button's atributes
Button2 = tkr.Button(musicplayer, width = 5, height = 3, font = "Helvetica 12 bold", text = "STOP", command = ExitMusicPlayer, bg = "red", fg = "white")
Button3 = tkr.Button(musicplayer, width = 5, height = 3, font = "Helvetica 12 bold", text = "PAUSE", command = pause, bg = "red", fg = "white")
Button4 = tkr.Button(musicplayer, width = 5, height = 3, font = "Helvetica 12 bold", text = "UNPAUSE", command = unpause, bg = "red", fg = "white")

var = tkr.StringVar #class that is used the changes of the variables in tkinter
songtitle = tkr.Label(musicplayer, font = "Helvetica 12 bold", textvariable = var)

songtitle.pack() #arrange the song in the app widget
Button1.pack(fill="x") #horizontal or vertical
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill = "both", expand = "yes") #both fills horizontally and vertically

musicplayer.mainloop() #runs the app