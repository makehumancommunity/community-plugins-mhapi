#!/usr/bin/python

from .namespace import NameSpace
import sys
import os

from .logchannel import LogChannel

class Utility(NameSpace):
    """This namespace wraps various calls which are convenient but not necessarily MH-specific."""

    def __init__(self,api):
        self.api = api
        NameSpace.__init__(self)
        self.trace()

        self.isPy3 = (sys.version_info >= (3,0))

        if self.isPython3():
            import urllib.request
            self.urlrequest = urllib.request
            import importlib
            import importlib.util
            self.hasPySide = (importlib.util.find_spec("PySide") is not None)
            self.hasPyQt = (importlib.util.find_spec("PyQt4") is not None)
        else:
            import urllib2
            self.urlrequest = urllib2
            import pkgutil
            self.hasPySide = (pkgutil.find_loader("PySide") is not None)
            self.hasPyQt = (pkgutil.find_loader("PyQt4") is not None)

        self.logChannels = {}

    def isPySideAvailable(self):
        return self.hasPySide

    def isPyQtAvailable(self):
        return self.hasPyQt

    def isPython3(self):
        return self.isPy3

    def getCompatibleUrlFetcher(self):
        return self.urlrequest

    def getLogChannel(self, name, defaultLevel=2, mirrorToMHLog=False):
        if name not in self.logChannels:
            self.logChannels[name] = LogChannel(name,defaultLevel,mirrorToMHLog)
        return self.logChannels[name]

