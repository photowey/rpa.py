# -*- coding:utf-8 -*-
"""
extension module.
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


# pylint: disable=W0622
def input(input_element_identifier=None, value_to_input=None, test_coordinate=None):
    """enter text at input element"""
    return robot.type(input_element_identifier, value_to_input, test_coordinate)


def button(button_element_identifier=None, test_coordinate=None):
    """left-click on button element"""
    return robot.click(button_element_identifier, test_coordinate)


def echo(message: str):
    """echo message"""
    robot.echo(message)
