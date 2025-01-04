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


# pylint: disable=W0614,W0401
from samples.init import *


# pylint: disable=C0116
def run():
    echo('----------------------------------------------------------------')
    init_rpa(visual_automation=True, chrome_browser=False)
    echo('----------------------------------------------------------------')

    # robot.dclick(30, 35)
    robot.dclick('Recycler.png')

    echo('----------------------------------------------------------------')

    robot.close()
