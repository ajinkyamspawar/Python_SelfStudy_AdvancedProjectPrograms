# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:59:39 2023

@author: AJINKYA
"""

#Free Song Lyrics using Python

import lyricsgenius

api_key="genrate key"

genius = lyricsgenius.Genius(api_key)

name = input("Enter Artists Name")

artist = genius.search_artist(name)

song = input("Type your song for Lyrics:")

song = artist.song(song)

print(song.lyrics)