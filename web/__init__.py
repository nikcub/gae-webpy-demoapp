#!/usr/bin/env python
"""web.py: makes web apps (http://webpy.org)"""

from __future__ import generators

__version__ = "0.34"
__author__ = [
    "Aaron Swartz <me@aaronsw.com>",
    "Anand Chitipothu <anandology@gmail.com>"
]
__license__ = "public domain"
__contributors__ = "see http://webpy.org/changes"

import utils, db, net, wsgi, http, webapi, httpserver, debugerror
import template, form

import session

from utils import *
from db import *
from net import *
from wsgi import *
from http import *
from webapi import *
from httpserver import *
from debugerror import *
from application import *
from browser import *
import test
try:
    import webopenid as openid
except ImportError:
    pass # requires openid module

def main():
    import doctest

    doctest.testmod(utils)
    doctest.testmod(db)
    doctest.testmod(net)
    doctest.testmod(wsgi)
    doctest.testmod(http)
    doctest.testmod(webapi)
    doctest.testmod(request)

    try:
        doctest.testmod(cheetah)
    except NameError:
        pass

    template.test()

    import sys
    urls = ('/web.py', 'source')
    class source:
        def GET(self):
            header('Content-Type', 'text/python')
            print open(sys.argv[0]).read()

    if listget(sys.argv, 1) != 'test':
        run(urls, locals())

if __name__ == "__main__": main()
