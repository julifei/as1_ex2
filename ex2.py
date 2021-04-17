"""
Author: Julius Feigl
Matr.Nr.: k11829015
Exercise 2
"""

import os
import glob
from PIL import Image
import tqdm
import numpy as np

# enter input direction
inp_dir = r"C:\Users\Julius\Desktop\Phyton II\Unit04\04_supplements\04_supplements\04_dataset_preview\dataset_preview"

# enter output direction
out_dir = inp_dir + "_out"

# enter logfile direction
logfile = inp_dir + "_log"

def ex2(inp_dir, out_dir, logfile):
    correct_img = 0

    # Get list of all files in input directory
    image_files = sorted(glob.glob(os.path.join(inp_dir, '**'),
                                   recursive=True))
    # Check number of found files
    print(f"{len(image_files)} files found")

    # Make output directory
    try:
        os.makedirs(out_dir)
    except OSError:
        pass

    # define array for hash values of the images
    hash_list = []

    # loop checks all the conditions for every single file
    for i, image_files in tqdm(enumerate(image_files), desc="Processing files",
                              total=len(image_files)):
        if image_files[i].endswith('*.jpg'| '*.JPG' | '*.JPEG' | '*.jpeg'):
            print(f'file {image_files[i]} is an image')

        else:
            with open(logfile + r'/logfile.txt', 'a') as log:
                print(f'{image_files[i]}; 1', file=log)

    return correct_img

ex2(inp_dir, out_dir, logfile)
