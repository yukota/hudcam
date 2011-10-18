#!/usr/bin/env python
#coding:utf-8
from Camera import *

#instance of DataModel

class Controller:
    def __init__(self,model):
	#instance of DataModel
	self.__model = model 
	print "initController"
	self.bootSystem()


#使用インスタンスを作成
#Viewを先に構築するため__init__と分離
#各インスタンスの作成
#cameraControl
    def bootSystem(self):
	#opencv,カメラの設定
	self.__camera = Camera()

    def getCameraPict(self):
	print "next"
	cameraPil  = self.__camera.getPicturePILImage()
	return cameraPil

    #水平取得
    #単位はdegree
    def getHorizon(self):
	return 10

