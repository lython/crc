#!/usr/bin/env python
# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

class Logging():
    def __init__(self, filename="./app.log"):
        self.basic_config()
        self.rotating_log(filename)
        
    def basic_config(self):
        logging.basicConfig(level=logging.INFO,
                format="[%(asctime)s][%(levelname)s]%(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                filemode='a')

    def print_console(self, level=logging.INFO):
        #打印到控制台
        console = logging.StreamHandler()
        console.setLevel(level)
        fmt = logging.Formatter("[%(asctime)s][%(levelname)s]%(message)s", "%Y-%m-%d %H:%M:%S")
        console.setFormatter(fmt)
        logging.getLogger('').addHandler(console)

    def rotating_log(self, filename):
        handler = RotatingFileHandler(filename, maxBytes=1024, backupCount=1)
        handler.setLevel(logging.INFO)
        fmt = logging.Formatter("[%(asctime)s][%(levelname)s]%(message)s", "%Y-%m-%d %H:%M:%S")
        handler.setFormatter(fmt)
        logging.getLogger('').addHandler(handler)

    def write_logs(self, txt, level):
        level(txt)

if __name__ == "__main__":
    import time
    t = Logging()
    localtime = lambda: time.ctime()
    t.write_logs(localtime(), logging.error)
    for x in range(20):
         t.write_logs(str(x+1) + localtime(), logging.error)
         time.sleep(1)
