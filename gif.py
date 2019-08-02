import os
import random
from PIL import Image
import glob
import imageio
import re

def getImagesinFolder(folder):
    images = []
    files = glob.glob(folder+'/*.png')
    files = sorted(files, key=lambda x:float(re.findall("(\d+)",x)[0]))
    for filename in files: #assuming gif
        print(filename)
        im=Image.open(filename)
        images.append(im)
    return images

x = getImagesinFolder('testSaveFig')
print(len(x))

imageio.mimsave('surface1.gif', x, duration = 0.1)
