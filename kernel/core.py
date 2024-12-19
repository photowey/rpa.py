# -*- coding:utf-8 -*-
"""
core module.
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


import os

import rpa as robot


def utf8():
    """charset utf-8"""
    os.system('chcp 65001')


def init(visual_automation=False, chrome_browser=True, headless_mode=False, turbo_mode=False):
    """start TagUI, auto-setup on first run"""
    utf8()

    tagui_location = os.getenv('TAGUI_LOCATION')
    robot.tagui_location(tagui_location)

    return robot.init(visual_automation, chrome_browser, headless_mode, turbo_mode)


def close():
    """close TagUI, Chrome browser, SikuliX"""
    return robot.close()


def pack():
    """for deploying package without internet"""
    return robot.pack()


def update():
    """
    update update package and TagUI files \n
    for updating package without internet
    """
    return robot.update()


def error(on_off=None):
    """
    function to set mode to raise exception on error \n
    set to Ture to raise exception on error
    """
    return robot.error(on_off)


def debug(on_off=None):
    """
    function to set debug mode, eg print debug info \n
    print & log debug info to rpa_python.log
    """
    return robot.debug(on_off)
