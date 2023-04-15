# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:45:32 2023

@author: AJINKYA
"""

import qrcode
import PIL
from PIL import Image

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 20, border = 8)

qr.add_data("linkofwebsite")
qr.make(fit=True)

img = qr.make_image(fill_color="pink", back_color = "white")
img.save("nameforimage.png")
