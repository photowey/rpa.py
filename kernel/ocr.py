# -*- coding:utf-8 -*-
"""
ocr module.
"""

#  Copyright © 2024 the original author or authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import rpa as robot


def click(coordinate_x=0, coordinate_y=0):
    """left-click on desktop (x, y) coordinate"""
    return click_xy(coordinate_x, coordinate_y)


def dclick(coordinate_x=0, coordinate_y=0):
    """double-click on desktop (x, y) coordinate"""
    return dclick_xy(coordinate_x, coordinate_y)


# ----------------------------------------------------------------


def click_xy(coordinate_x=0, coordinate_y=0):
    """left-click on desktop (x, y) coordinate"""
    return robot.click(coordinate_x, coordinate_y)


def dclick_xy(coordinate_x=0, coordinate_y=0):
    """double-click on desktop (x, y) coordinate"""
    return robot.dclick(coordinate_x, coordinate_y)


# ----------------------------------------------------------------


def click_image(image):
    """left-click on desktop/browser image"""
    return robot.click(image)


def dclick_image(image):
    """double-click on desktop/browser image"""
    return robot.dclick(image)
