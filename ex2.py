"""
Author: Julius Feigl
Matr.Nr.: k11829015
Exercise 2
"""

import os
import glob
from PIL import image
import tqdm
import numpy as np

#enter input direction
inp_dir = r"/home/osboxes/Documents/Python II/as1/Ex_1/data_pictures_small"

#enter output direction
out_dir = inp_dir + "_out"

#enter logfile direction
logfile = inp_dir + "_log"

def ex2(inp_dir, out_dir, logfile):
    image_files = sorted(glob.glob(os.path.abspath.join(inp_dir, '**',)))
    os.makedirs(out_dir)
    print('a')