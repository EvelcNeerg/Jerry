#!/usr/bin/env python3.6
"""
Compares encoded images with each other
"""

import os
import _thread
import PIL

__author__ = "Cleve Green"
__copyright__ = "Copyright 2019, Cleve Green"
__credits__ = ["Cleve Green"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Cleve Green"
__email__ = "clellandgreen0@gmail.com"
__status__ = "Production"


class ImageCompare:
    def __init__(self, img1, img2):
        self.img1, self.img2 = img1, img2
        with open(self.img1, "r") as imageEnc:
            self.img1Enc = list(imageEnc.read())
        with open(self.img2, "r") as imageEnc:
            self.img2Enc = list(imageEnc.read())
        prct = [0, 0]
        print("Image Name: " + str(img2).split('/')[-1])

        for count in range(len(self.img1Enc)):
            try:
                if self.img1Enc[count] == self.img2Enc[count]:
                    prct[0] += 1
                else:
                    prct[1] += 1
            except IndexError:
                print(count)
                break
        print("Image Ratio (True, False):", prct)
        print("Image %: {}\n".format(prct[0] / (prct[0] + prct[1])))
        try:
            os.mkdir("Data")
        except FileExistsError:
            pass
        with open("Data/accuracyData.txt", "a+") as file:
            pass
            file.write(str("{},{},{}\n".format(prct[0], prct[1], img2)))



