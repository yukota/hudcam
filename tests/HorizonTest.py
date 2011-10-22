#!/usr/bin/env python
#coding:utf-8

####################
#Unit test of Horizon.py
####################

import unittest
#moduel serach path
import pathconf

import cv
#テスト対象
from Horizon import *


class HorizonTest(unittest.TestCase):

    #setUp
    def setUp(self):
	#create Grayscale picture for test
	testColorImg1 = cv.LoadImage("./HorizonTestData/test1.jpg",cv.CV_LOAD_IMAGE_COLOR)
	cv.Smooth(testColorImg1,testColorImg1,cv.CV_GAUSSIAN,13,0,0,0)
	testGrayImage1 = cv.CreateImage((testColorImg1.width,testColorImg1.height),cv.IPL_DEPTH_8U,1)
	cv.CvtColor(testColorImg1,testGrayImage1,cv.CV_BGR2GRAY)
	cv.EqualizeHist(testGrayImage1,testGrayImage1)
	#create instance
	self.horizon = Horizon(testGrayImage1)
	self.horizon.test(testColorImg1)
	

#    def testAll(self):
	#インスタンスが生成されていることを確認する
	#Tests exsit of instance
#	self.assertIsInstance(self.horizon,Horizon)

	
    #Tests calcHorizon
    def testDetectHough(self):
	self.assertIsInstance(self.horizon,Horizon)
	self.horizon.detectHorizon()





	




#test
def suite():
    return unittest.TestSuite((
	unittest.makeSuite(HorizonTest,'test'),
	))
if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
