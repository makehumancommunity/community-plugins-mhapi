#!/usr/bin/python3

import log
import os
import gui3d
import inspect

class LogChannel():

    CRASH = 0
    ERROR = 1
    WARN = 2
    INFO = 3
    DEBUG = 4
    TRACE = 5

    _levels = ["CRASH", "ERROR", "WARN ", "INFO ", "DEBUG", "TRACE"]

    def __init__(self,name,defaultLevel = 4,mirrorToMHLog = True):
        self.name = name;
        self.level = defaultLevel;
        self.mirror = mirrorToMHLog
        self.api = gui3d.app.mhapi

        self.root = self.api.locations.getUserHomePath("plugin_logs")

        if not os.path.exists(self.root):
            os.makedirs(self.root)

        self.fileName = os.path.join(self.root,name + ".txt")

        with open(self.fileName,"wt") as f:
            f.write("--- " + self.fileName + " ---\n\n")

    def _logItem(self,level,message,item):
        if level > self.level:
            return

        stack = inspect.stack()
        (frame, filename, line_number, function_name, lines, index) = stack[2]

        loc = "{}/{}():{}".format(os.path.basename(filename),function_name, line_number)

        leveln = self._levels[level]
        outStr = ""
        if item is not None:
            outstr = "[{0}] {1} {2} {3}".format(leveln,loc,message,item)
        else:
            outstr = "[{0}] {1} {2}".format(leveln,loc,message)

        if self.mirror:
            log.debug(outstr)

        with open(self.fileName,"at") as f:
            f.write(outstr + "\n")

    def crash(self, message, item = None):
        self._logItem(self.CRASH,message,item)

    def error(self, message, item = None):
        self._logItem(self.ERROR,message,item)

    def warn(self, message, item = None):
        self._logItem(self.WARN,message,item)

    def info(self, message, item = None):
        self._logItem(self.INFO,message,item)

    def debug(self, message, item = None):
        self._logItem(self.DEBUG,message,item)

    def trace(self, message, item = None):
        self._logItem(self.TRACE,message,item)

