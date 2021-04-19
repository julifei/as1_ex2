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
import hashlib
import shutil

def ex2(inp_dir, out_dir, logfile):
    # initialize variables
    correct_img = 0
    yet_copied = False
    i = 0
    # define list for hash values of the images
    hash_list = []

    # Get list of all files in input directory
    image_files = sorted(glob.glob(os.path.join(os.path.abspath(inp_dir), '**', '*'),
                                   recursive=True))

    # Make output directory, pass if already exists
    try:
        os.makedirs(out_dir)
    except OSError:
        pass

    # loop checks all the conditions for every single file
    while i < len(image_files):
        # check suffix with function .endswith()
        if image_files[i].endswith('.jpg') or image_files[i].endswith('.JPG') or image_files[i].endswith('.jpeg')\
                or image_files[i].endswith('.JPEG'):
            # check for correct size
            if os.path.getsize(image_files[i]) > 10000:
                # check if really an image
                # is not an image if PIL rises an exception
                real_img = True
                try:
                    image = Image.open(image_files[i]) # try loading as PIL file
                except OSError:
                    real_img = False
                if real_img == True:
                    # check if image is H & W >= 100 Pixels and without color
                    # get relevant information from PIL
                    if image.mode == 'L' and image.width >= 100 and image.height >= 100:
                        # convert to np array for the following tests
                        image = np.array(image)
                        # check if variance > 1 with numpy function
                        if np.var(image) > 1:
                            # check if already copied
                            # calculate hash value of current file first
                            hashing_function = hashlib.sha256()
                            hashing_function.update(image.tobytes())
                            image_hash = hashing_function.digest()
                            # check if hash value of current file is same as hash value of one of the copied files
                            for current_element in hash_list:
                                if image_hash == current_element:
                                    yet_copied = True
                                    break
                                else:
                                    yet_copied = False
                            # final step: renaming and copying the file
                            if yet_copied == False:
                                # append hash value of current file to list of hash values of copied files
                                hash_list.append(image_hash)
                                # adjust the filename
                                # calculate how many 0 so that the filename has 7 digits
                                str_correct_img = str(correct_img)
                                NOF_zeros = 7 - len(str_correct_img)
                                filename = NOF_zeros * '0' + f'{str_correct_img}'

                                shutil.copy(image_files[i], os.path.join(out_dir, filename + f'.jpg'))

                                correct_img = correct_img + 1
                                i = i + 1

                            # logfile entry: file yet copied
                            else:
                                # prints the error code and the filename in the logfile
                                with open(logfile, 'a') as log:
                                    print(f'{os.path.relpath(image_files[i], start=inp_dir)};6', file=log)
                                # counts to next element in while loop
                                i = i + 1
                        # logfile entry: error with variance
                        else:
                            # prints the error code and the filename in the logfile
                            with open(logfile, 'a') as log:
                                print(f'{os.path.relpath(image_files[i], start=inp_dir)};5', file=log)
                            # counts to next element in while loop
                            i = i + 1
                    # logfile entry: error with color or dimension
                    else:
                        # prints the error code and the filename in the logfile
                        with open(logfile, 'a') as log:
                            print(f'{os.path.relpath(image_files[i], start=inp_dir)};4', file=log)
                        # counts to next element in while loop
                        i = i + 1
                # logfile entry: error with readability
                else:
                    # prints the error code and the filename in the logfile
                    with open(logfile, 'a') as log:
                        print(f'{os.path.relpath(image_files[i], start=inp_dir)};3', file=log)
                    # counts to next element in while loop
                    i = i + 1
            # logfile entry: error with size
            else:
                # prints the error code and the filename in the logfile
                with open(logfile, 'a') as log:
                    print(f'{os.path.relpath(image_files[i], start=inp_dir)};2', file=log)
                # counts to next element in while loop
                i = i + 1
        # logfile entry: error with suffix
        else:
            # prints the error code and the filename in the logfile
            with open(logfile, 'a') as log:
                print(f'{os.path.relpath(image_files[i], start=inp_dir)};1', file=log)
            # counts to next element in while loop
            i = i + 1
    print("Done.")
    return correct_img