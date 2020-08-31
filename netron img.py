# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:39:55 2020

@author: Bagavathi Priya
"""

#import pillow

'''
To view the structure of any neural network architecture, follow the below steps

1. Use any .h5 or similar kind of supported model files
2. Open that file in Netron
3. Using the blocks, export the kernel for any specific one
4. Use this code to view any exported kernel layer
'''

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


img_arr = np.load('Downloads/convb.npy')

img = Image.fromarray(img_arr[0][0])

img.show()