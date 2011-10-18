#!/usr/bin/env python
#coding:utf-8

#モジュールサーチパスの設定

import os
import sys

currentDir = os.path.dirname(__file__)
extraPath = [
    currentDir + '/../src/'
    ]
sys.path = extraPath + sys.path

if __name__ == '__main__':
    print sys.path
