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
from samples.init import *

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


# ----------------------------------------------------------------

def process_table(page_no: int, tr_index: int):
    page_index = page_no
    row_index = tr_index
    while True:
        table_tr_button_xpath = f'//table/tbody/tr[{row_index}]//button[contains(., "查看")]'

        if robot.exist(table_tr_button_xpath):
            echo(f"--- 点击 {page_index} 页, 第 {row_index} 行的 '查看' 按钮 ---")
            robot.click(table_tr_button_xpath)

            # 详情处理完了 -> 点击取消 -> 下一次 tr
            robot.click('取消')
            robot.wait(1)

            row_index += 1
        else:
            echo(f"没有更多的数据行查看了(当前页码: {page_no}, 行号: {row_index - 1}).")
            break

    # 遍历表格并处理分页
    while True:
        echo(f"处理分页, 当前页码: {page_no}...")

        # 检查是否存在“下一页”按钮
        next_page_xpath = "//button[@class='btn-next' and @aria-label='下一页']"
        next_page_disabled_xpath = "//button[@class='btn-next' and @aria-label='下一页' and @disabled]"
        if robot.exist(next_page_disabled_xpath):
            echo(f"当前页码 {page_no} 已经是最后一页啦,我要退出了")
            break

        echo(f"点击: 下一页 {page_no + 1}...")
        robot.click(next_page_xpath)
        robot.wait(1)
        process_table(page_no + 1, 1)


# ----------------------------------------------------------------

# pylint: disable=C0116
def table():
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

    echo('3.爬取表格')
    echo('3.1.点击: 超级表格')
    robot.click('超级表格')
    echo('3.2.点击: 使用 ProTable')
    robot.click('使用 ProTable')
    echo('3.3.点击: 最后一页')
    robot.click("//ul[@class='el-pager']/li[last()]")

    echo('3.4.点击: 每行 `查看` 按钮')
    process_table(200, 1)

    echo('----------------------------------------------------------------')

    echo('4.退出')
    echo('4.1.点击: 头像')
    robot.click('//*[@id="watermark"]/section/section/header/div[2]/div[2]/div/img')
    robot.wait()

    echo('4.2.点击: 退出登录')
    # pylint: disable=C0301
    logout_li = '//ul[contains(@class, "el-dropdown-menu")]/li[last()][contains(normalize-space(), "退出登录")]'
    robot.click(logout_li)
    robot.wait(1)

    echo('4.3.点击: 确定')
    robot.click('//*[@class="el-message-box__btns"]/button[2]')
    robot.wait()

    echo('----------------------------------------------------------------')

    echo('5.结束')
    close()
