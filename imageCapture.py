#!/usr/bin/env python3.6
"""
Captures video to analyze
"""

import os
import _thread
import PIL
import cv2
import time

__author__ = "Cleve Green"
__copyright__ = "Copyright 2019, Cleve Green"
__credits__ = ["Cleve Green"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Cleve Green"
__email__ = "clellandgreen0@gmail.com"
__status__ = "Production"


class ImageCapture:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        while True:
            _, frame = self.capture.read()
            cv2.imshow("frame", frame)
            k = cv2.waitKey(30) & 0xFF
            # Escape key
            if k == 27:
                break
        self.capture.release()
        cv2.destroyAllWindows()


ImageCapture()