# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:04:33 2023

@author: AJINKYA
"""

import qrcode as qr
img = qr.make("linkofwebsite")

img.save("nameforimage.png")
