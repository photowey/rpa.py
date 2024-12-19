# -*- coding:utf-8 -*-
"""
pro module.
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


def telegram(telegram_id=None, text_to_send=None, custom_endpoint=None):
    """send Telegram message"""
    robot.telegram(telegram_id, text_to_send, custom_endpoint)


def keyboard(keys_and_modifiers=None):
    """
    send keystrokes to screen \n
    using visual automation
    """
    return robot.keyboard(keys_and_modifiers)


def mouse(mouse_action=None):
    """
    sent mouse event to screen \n
    :mouse_action `down` or `up` \n
    using visual automation
    """
    return robot.mouse(mouse_action)


def focus(app_to_focus=None):
    """
    make application in focus
    :app_to_focus full name of app
    """
    return robot.focus(app_to_focus)


def wait(delay_in_seconds=5.0):
    """
    explicitly wait for some time \n
    default 5 seconds
    """
    return robot.wait(delay_in_seconds)


def table(element_identifier=None, filename_to_save=None):
    """save webpage table to CSV"""
    return robot.table(element_identifier, filename_to_save)


def bin(file_to_bin=None, password=None, server='https://tebel.org/bin/'):
    """secure temporary storage"""
    return robot.bin(file_to_bin, password, server)


def upload(element_identifier=None, filename_to_upload=None):
    """upload file to web element"""
    return robot.upload(element_identifier, filename_to_upload)


def download(download_url=None, filename_to_save=None):
    """
    function for python 2/3 compatible file download from url \n
    download from URL to file
    """
    return robot.download(download_url, filename_to_save)


def unzip(file_to_unzip=None, unzip_location=None):
    """unzip zip file to specified location"""
    return robot.unzip(file_to_unzip, unzip_location)


def frame(main_frame=None, sub_frame=None):
    """
    set web frame, frame() to reset \n
    :main_frame id or name \n
    :sub_frame optional
    """
    return robot.frame(main_frame, sub_frame)


def popup(string_in_url=None):
    """
    set context to web popup tab \n
    no parameter to reset to main page, especially important when used to control another browser tab
    """
    return robot.popup(string_in_url)


def run(command_to_run=None):
    """
    run OS command & return output \n
    use `;` between commands
    """
    return robot.run(command_to_run)


def dom(statement_to_run=None):
    """
    run code in DOM & return output \n
    JS code to run in browser
    """
    return robot.dom(statement_to_run)


def vision(command_to_run=None):
    """
    run custom SikuliX commands \n
    Python code for SikuliX
    """
    return robot.vision(command_to_run)


def timeout(timeout_in_seconds=None):
    """
    change wait timeout, default 10s \n
    blank  returns current timeout
    """
    robot.timeout(timeout_in_seconds)
