# -*- coding:utf-8 -*-
"""
helper module.
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


def exist(element_identifier=None):
    """Ture or False if element shows before timeout"""
    return robot.exist(element_identifier)


def present(element_identifier=None) -> bool:
    """Ture or False if element is present now"""
    return robot.present(element_identifier)


def count(element_identifier=None) -> int:
    """return number of web elements as integer"""
    return robot.count(element_identifier)


def clipboard(text_to_put=None):
    """put text or return clipboard text as string"""
    return robot.clipboard(text_to_put)


def get_text(source_text=None, left=None, right=None, count=1) -> str:
    """return text between left & right markers"""
    return robot.get_text(source_text, left, right, count)


def del_chars(source_text=None, characters=None):
    """return text after deleting given characters"""
    return robot.del_chars(source_text, characters)


def mouse_xy() -> (int, int):
    """return `(x,y)` coordinates of mouse as integer"""
    return robot.mouse_xy()


def mouse_x() -> int:
    """return `x` coordinate of mouse as integer"""
    return robot.mouse_x()


def mouse_y() -> int:
    """return `y` coordinate of mouse as integer"""
    return robot.mouse_y()


def title() -> str:
    """return page title of current web page as string"""
    return robot.title()


def text() -> str:
    """return text content of current web page as string"""
    return robot.text()


def timer() -> float:
    """return time elapsed in seconds between calls as float"""
    return robot.timer()
