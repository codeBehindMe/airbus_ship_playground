# This module makes the training masks from the csv file.

import cv2
import numpy as np
import pandas as pd

def decode_rule_and_save(name,rule):
	""" Makes new images from runlength encoding"""

	def rle_decode(mask_rle, shape=(768, 768)):
    img = np.zeros(shape[0]*shape[1], dtype=np.uint8)
    if isinstance(mask_rle,str):
        s = mask_rle.split()
        starts =  np.asarray(s[0::2], dtype=int)
        lengths = np.asarray(s[1::2], dtype=int)

        starts -= 1
        ends = starts + lengths
        for lo, hi in zip(starts, ends):
                img[lo:hi] = 1
    return img.reshape(shape).T

	def save_numpy_array_to_jpg(np_img):
		return


