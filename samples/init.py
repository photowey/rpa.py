# -*- coding:utf-8 -*-
"""
init module.
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


# pylint: disable=C0116
def utf8():
    os.system('chcp 65001')


# pylint: disable=C0116
def init_rpa():
    utf8()

    tagui_location = os.getenv('TAGUI_LOCATION')
    robot.tagui_location(tagui_location)

    robot.init()


# pylint: disable=C0116
def echo(message: str):
    robot.echo(message)


# pylint: disable=C0116
def close():
    robot.close()
