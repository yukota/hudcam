#!/usr/bin/env python
#coding:utf-8
import cv
import sys

from Camera import *
from Horizon import *

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

    def getCameraCVPict(self):
	self.__cameraPict = self.__camera.getPicture()

    #水平取得
    #単位はdegree
    def getHorizon(self):
	try:
	    self.getCameraCVPict()
	    self.convertGray()
	    horizon = Horizon(self.__grayCameraPict)
	    horizon.detectHorizon()
	    degree = horizon.getHorizon()
	    print "degree:"+str(degree)
	    return degree
	except:
	    sys.exit(sys.exc_info()[:2])

    #画像変換
    def convertGray(self):
    	cv.Smooth(self.__cameraPict,self.__cameraPict,cv.CV_GAUSSIAN,13,0,0,0)
	grayCameraImage = cv.CreateImage((self.__cameraPict.width,self.__cameraPict.height),cv.IPL_DEPTH_8U,1)
	cv.CvtColor(self.__cameraPict,grayCameraImage,cv.CV_BGR2GRAY)
	cv.EqualizeHist(grayCameraImage,grayCameraImage)
	self.__grayCameraPict = grayCameraImage


