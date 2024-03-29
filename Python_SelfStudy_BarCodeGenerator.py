# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:04:29 2023

@author: AJINKYA
"""

import barcode
from barcode.writer import ImageWriter 

#Define content of the barcode as a string 
number = input("Enter the code to generate barcode")

#Get the required barcode format 
barcode_format = barcode.get_barcode_class('upc')

#Generate barcode and render as image 

my_barcode = barcode_format(number, writer=ImageWriter())

#Save barcode as png
my_barcode.save('generated barcode')