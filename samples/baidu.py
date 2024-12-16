# -*- coding:utf-8 -*-
"""
baidu module.
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
from init import *


# pylint: disable=C0116
def run():
    echo('----------------------------------------------------------------')
    echo('0:开始')
    init_rpa()
    echo('----------------------------------------------------------------')

    echo('1.访问: https://www.baidu.com')
    robot.url('https://www.baidu.com')
    echo('----------------------------------------------------------------')

    echo('2.搜索: TagUI')
    robot.type('//*[@id="kw"]', 'TagUI[enter]')
    robot.wait()
    echo('----------------------------------------------------------------')

    echo('3.快照: 当前搜索页')
    robot.snap('page', 'baidu.png')
    robot.wait()
    echo('----------------------------------------------------------------')

    echo('4.退出')
    robot.close()
