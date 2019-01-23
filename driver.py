#!/usr/bin/env python3.6
"""
Workflow
"""
import os
from ImageConvert import ImageConverter
from ImageComparison import ImageCompare
from mostAccurate import most_accurate
from indexingImages import Indexing

__author__ = "Cleve Green"
__copyright__ = "Copyright 2019, Cleve Green"
__credits__ = ["Cleve Green"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Cleve Green"
__email__ = "clellandgreen0@gmail.com"
__status__ = "Production"


class SFunctions:
    def __init__(self):
        try:
            os.remove("Data/accuracyData.txt")
            for file in os.listdir("encodedImages/NewImage"):
                os.remove("encodedImages/NewImage/{}".format(file))
        except FileNotFoundError:
            pass
        self.brand_names = ImageConverter.listdir_ig_hidden("images")
        ImageConverter().img_conversion("NewImage")
        image_tc = "".join(os.listdir("encodedImages/NewImage"))
        for brand in os.listdir("encodedImages"):
            if brand == "NewImage":
                continue
            for enc_image in os.listdir("encodedImages/{}".format(brand)):
                ImageCompare("encodedImages/NewImage/{}".format(image_tc),
                             "encodedImages/{}/{}".format(brand, enc_image))
        self.g_result = most_accurate()
        self.most_accurate = self.g_result[1][self.g_result[0]]
        self.most_accurate = self.most_accurate.split('/')[-1]
        print("Bag: {}".format(self.most_accurate))


if __name__ == '__main__':
    SFunctions()
