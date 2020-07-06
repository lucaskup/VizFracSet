# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 10:01:25 2020

@author: LKUPSSINSKU
"""
import cv2
import imageio

im = imageio.imread("Dados\\bisdom.tif")

cv2.imwrite('Dados\\bisdom.png', im[:,:,0:-1])
