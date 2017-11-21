# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor
import threading
from queue import Queue

from multiprocessing import Process
from multiprocessing.pool import Pool


def func():
    print('%s this is multi thread' % threading.current_thread())


def process():
    p = Process(target=func)
    p.start()


def process_pool():
    pool = Pool(processes=3)
    for i in range(6):
        pool.apply_async(func)

    pool.close()
    pool.join()


def start_pool():
    pool = ThreadPoolExecutor(64)
    for i in range(10):
        pool.submit(func)


# 用Queue来自己创建线程池：
class CustomThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        while True:
            cmd = self.__queue.get()
            cmd()
            self.__queue.task_done()


def custom_pool():
    queue = Queue(5)
    for i in range(queue.maxsize):
        t = CustomThread(queue)
        t.setDaemon(True)
        t.start()

    for i in range(20):
        queue.put(func)
    queue.join()


if __name__ == '__main__':
    custom_pool()