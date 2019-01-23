#!/usr/bin/env python3.6
"""
Creates an index of all the images
"""

import os

__author__ = "Cleve Green"
__copyright__ = "Copyright 2019, Cleve Green"
__credits__ = ["Cleve Green"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Cleve Green"
__email__ = "clellandgreen0@gmail.com"
__status__ = "Production"


class Indexing:
    def __init__(self):
        self.images = {}
        self.brands = os.listdir("images")
        count = 0
        for brand in self.brands:
            for bag in os.listdir("images/{}".format(brand)):
                self.images[bag] = count
                count += 1

    def g(self):
        return self.images


