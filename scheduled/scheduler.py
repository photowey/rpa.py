# -*- coding:utf-8 -*-
"""
scheduler package.
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


import logging
import sched
import threading
import time
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

# logger = logging.getLogger('my_logger')
# logger.setLevel(logging.DEBUG)
#
# file_handler = logging.FileHandler('logfile.log', mode='w', encoding='utf-8')
# file_handler.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)


logging.basicConfig(
    filename='rpa.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    encoding='utf-8'
)

# 创建一个logger对象
logger = logging.getLogger('rpa')

logger.debug('这是一个 debug 级别的日志信息')
logger.info('这是一个 info 级别的日志信息')
logger.warning('这是一个 warning 级别的日志信息')
logger.error('这是一个 error 级别的日志信息')
logger.critical('这是一个 critical 级别的日志信息')
logger.fatal('这是一个 fatal 级别的日志信息')


def job():
    """normal job function"""
    logger.info("--- scheduled task running ---")


def threading_job():
    """threading job function"""
    logger.info("--- threading scheduled task running ---")


def cron_job():
    """cron job function"""
    logger.info(f'This job runs every 1 minutes using cron. Current time is {datetime.now()}')


def async_worker():
    logger.debug(f'这是来自线程 {threading.current_thread().name} 的调试信息')


def mian():
    """main function"""
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(10, 1, job)

    scheduler.run()


def mian2():
    """mian2 function"""
    threading.Timer(10, threading_job).start()


def mian3():
    """mian3 function"""
    scheduler = BlockingScheduler()

    # 1.scheduler.add_job(interval_job, 'interval', minutes=5)
    # 2.scheduler.add_job(cron_job, 'cron', minute='*/5')
    # 3.scheduler.add_job(cron_job, 'cron', hour=8, minute=30)

    # 4.cron_expr
    # * * * * *
    # | | | | |
    # | | | | +--- 星期几(0 - 7)(星期天为0和7)
    # | | | +----- 月份(1 - 12)
    # | | +------- 日期(1 - 31)
    # | +--------- 小时(0 - 23)
    # +----------- 分钟(0 - 59)
    cron_expr = '0-59/1 * * * *'
    trigger = CronTrigger.from_crontab(cron_expr)
    scheduler.add_job(cron_job, trigger)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.error('Received termination signal, shutting down gracefully.')
        scheduler.shutdown(wait=False)
    except Exception as e:
        logger.error(f'An error occurred: {e}')
        scheduler.shutdown(wait=False)
    finally:
        logger.info('Scheduler has been shut down.')


if __name__ == '__main__':
    thread = threading.Thread(target=async_worker, name='AsyncWorker')
    thread.start()
    thread.join()

    # mian()
    # mian2()
    mian3()
