# -*- coding:utf-8 -*-
"""
admin module.
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

USERNAME = 'admin'
PASSWORD = '123456'
URL = 'http://localhost:8848'


#
# @see https://github.com/HalseySpicy/Geeker-Admin
#


# pylint: disable=C0116
def run():
    init_rpa()

    echo('----------------------------------------------------------------')
    echo('0:开始')
    echo('----------------------------------------------------------------')

    echo('1.访问: http://localhost:8848')
    robot.url(URL)
    robot.wait()
    echo('----------------------------------------------------------------')

    echo('2.登录')
    echo('2.1.输入: 账号')
    robot.type('//*[@type="text"]', USERNAME)

    echo('2.2.输入: 密码')
    robot.type('//*[@type="password"]', PASSWORD)
    echo('2.3.点击: 登录')
    robot.click('//*[@id="app"]/div/div/div[3]/div[2]/button[2]')
    echo('----------------------------------------------------------------')

    echo('3.退出')
    echo('3.1.点击: 头像')
    robot.click('//*[@id="watermark"]/section/section/header/div[2]/div[2]/div/img')
    robot.wait()

    echo('3.2.点击: 退出登录')
    # pylint: disable=C0301
    logout_li = '//ul[contains(@class, "el-dropdown-menu")]/li[last()][contains(normalize-space(), "退出登录")]'
    robot.click(logout_li)
    robot.wait(1)

    echo('3.3.点击: 确定')
    robot.click('//*[@class="el-message-box__btns"]/button[2]')
    robot.wait()

    echo('----------------------------------------------------------------')

    echo('5.结束')
    close()
