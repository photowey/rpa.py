# -*- coding:utf-8 -*-
"""
basic module.
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


def url(webpage_url=None):
    """go to web URL"""
    return robot.url(webpage_url)


def click(element_identifier=None, test_coordinate=None):
    """left-click on element"""
    return robot.click(element_identifier, test_coordinate)


def rclick(element_identifier=None, test_coordinate=None):
    """right-click on element"""
    return robot.rclick(element_identifier, test_coordinate)


def dclick(element_identifier=None, test_coordinate=None):
    """double-click on element"""
    return robot.dclick(element_identifier, test_coordinate)


def hover(element_identifier=None, test_coordinate=None):
    """move mouse to element"""
    return robot.hover(element_identifier, test_coordinate)


# pylint: disable=W0622
def type(element_identifier=None, text_to_type=None, test_coordinate=None):
    """enter text at element"""
    return robot.type(element_identifier, text_to_type, test_coordinate)


# pylint: disable=C0301
def select(element_identifier=None, option_value=None, test_coordinate1=None, test_coordinate2=None):
    """choose dropdown option"""
    return robot.select(element_identifier, option_value, test_coordinate1, test_coordinate2)


# pylint: disable=C0301
def read(element_identifier=None, test_coordinate1=None, test_coordinate2=None, test_coordinate3=None):
    """return element text"""
    return robot.read(element_identifier, test_coordinate1, test_coordinate2, test_coordinate3)


# pylint: disable=C0301
def snap(element_identifier=None, filename_to_save=None, test_coord1=None, test_coord2=None, test_coord3=None):
    """save screenshot to file"""
    return robot.snap(element_identifier, filename_to_save, test_coord1, test_coord2, test_coord3)


def load(filename_to_load=None):
    """return file content"""
    return robot.load(filename_to_load)


def dump(text_to_dump=None, filename_to_save=None):
    """save text to file"""
    return robot.dump(text_to_dump, filename_to_save)


def write(text_to_write=None, filename_to_save=None):
    """append text to file"""
    return robot.write(text_to_write, filename_to_save)


def ask(text_to_prompt=''):
    """ask & return user input"""
    return robot.ask(text_to_prompt)
