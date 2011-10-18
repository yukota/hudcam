#!/usr/bin/env python
#coding:utf-8

#####################
#水平検出
#####################


class Horizon:
    #二値画像を引数に取る
    def __init__(self,binaryPict):
	self.__binaryPict = binaryPict;
	#
