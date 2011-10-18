#!/usr/bin/env python
#coding:utf-8

#instance of Camera
import cv 
import Image

class Camera:
    def __init__(self):
	print "initCamera"
#	cv.NamedWindow("camera",1)
	self.__capture = cv.CreateImage((640,480),cv.IPL_DEPTH_8U,1)
	#self.__capture = cv.CaptureFromCAM(0)
	self.__capture = cv.CaptureFromCAM(0)

    #カメラ画像を取り込み
    #PILで返す
    def getPicture(self):
	img = cv.QueryFrame(self.__capture)
	return img

    def getPicturePILImage(self):
	#カメラ画像の取得
	camImage = self.getPicture()
	#OpenCV to PIL Image
#	pilImage = Image.fromstring("L",cv.GetSize(camImage),camImage.tostring())

	pilImage = Image.fromstring('RGB', cv.GetSize(camImage),camImage.tostring(),'raw','BGR',camImage.width*3,0)

	return pilImage
