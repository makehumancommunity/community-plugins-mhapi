#!/usr/bin/python

from .namespace import NameSpace
import sys
import importlib
import importlib.util

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
        else:
            import urllib2
            self.urlrequest = urllib2

    def isPySideAvailable(self):
        return (importlib.util.find_spec("PySide") is not None)

    def isPyQtAvailable(self):
        pass

    def isPython3(self):
        return self.isPy3

    def getCompatibleUrlFetcher(self):
        return self.urlrequest


