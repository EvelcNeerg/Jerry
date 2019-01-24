#!/usr/bin/env python3.6
"""
This converts images into numbers in base64
"""
import base64
import os
from PIL import Image

__author__ = "Cleve Green"
__copyright__ = "Copyright 2019, Cleve Green"
__credits__ = ["Cleve Green"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Cleve Green"
__email__ = "clellandgreen0@gmail.com"
__status__ = "Production"


class ImageConverter:
    def __init__(self):
        self.brand_names = self.listdir_ig_hidden("images")
        for brand in self.brand_names:
            self.image_prep(brand)
            self.img_conversion(brand)
        for brand in self.listdir_ig_hidden("grayImages"):
            self.img_conversion(brand, gray=True)
        n_image = os.listdir("NewImage")

    def image_prep(self, brand_name, new_img=False):
        # Changes resolution of image so that it does not change.
        # And changes image size, because if it is not constant accuracy is lost.
        if not new_img:
            full_p = "images"
        else:
            full_p = "NewImage"
        for image in self.listdir_ig_hidden("{}/{}".format(full_p, brand_name)):
            if not new_img:
                im = Image.open("images/{}/{}".format(brand_name, image))
            else:
                im = Image.open("NewImage/{}".format(brand_name))
            im = im.resize((1000, 1000), Image.ANTIALIAS)
            try:
                if image.split('.')[-1].upper() == "JPG":
                    grayim = im.convert('L')
                else:
                    grayim = im.convert('LA')
            except OSError as e:
                print("[!] JPEGs are not recommended.")
                grayim = im
            try:
                os.mkdir("grayImages")
            except FileExistsError:
                pass
            try:
                os.mkdir("grayImages/Gray{}".format(brand_name))
            except FileExistsError:
                pass

            if not new_img:
                grayim.save("grayImages/Gray{}/Gray-{}".format(brand_name, image), dpi=(600, 600))
                im.save("images/{}/{}".format(brand_name, image), dpi=(600, 600))
            else:
                try:
                    os.mkdir("GrayNewImage")
                except FileExistsError:
                    pass
                grayim.save("GrayNewImage/{}".format(brand_name))
                im.save("NewImage/{}")

    def img_conversion(self, brand_name, gray=False):
        brandname_ne = brand_name
        if brand_name != "NewImage" and not gray:
            brand_name = "images/{}".format(brand_name)
        elif brand_name != "NewImage" and gray:
            brand_name = "grayImages/{}".format(brand_name)
        for image in self.listdir_ig_hidden(brand_name):
            # Gets image name without extension
            image_name = image.split(".")[0]
            # Opens image to read binary
            with open("{}/{}".format(brand_name, image), "rb") as image_file:
                # Converts image to base64
                encoded_string = base64.b64encode(image_file.read())
            # Organization of files and folders
            if brand_name not in os.listdir("encodedImages"):
                try:
                    # if gray:
                    #     brandname_ne = "Gray{}".format(brandname_ne)
                    os.mkdir("encodedImages/{}".format(brandname_ne))
                except FileExistsError:
                    pass
            with open("encodedImages/{}/{}.txt".format(brandname_ne, image_name), "w") as encoded_img:
                encoded_img.write(str(encoded_string))

    @staticmethod
    # Generator that returns non-hidden files.
    # Prevents it from using a .DS_Store as an image.
    def listdir_ig_hidden(path):
        for f in os.listdir(path):
            if not f.startswith('.'):
                yield f
