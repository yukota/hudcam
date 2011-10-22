#!/usr/bin/env python
#coding:utf-8

import Image
import cv
import math
#####################
#水平検出
#1.標準的Hough変換で直線を出す
#垂直と水平が一番多くなれば良い
#sin*cosが0に近くなる直線を取る :TODO検証
#水平，垂直の判断(1/4の選択なる)
#####################

class Horizon:
    #カメラからのグレースケール画像を取得
    def __init__(self,grayPict):
	#iplカラー画像
	self.__grayPict = grayPict;
	self.__degree = 0

    #標準ハフ変換を行う
    def __calcHough(self):
	#前処理
	#フィルタ
	#cv.Smooth(self.__grayPict,self.__grayPict,cv.CV_GAUSSIAN,11,0,0,0)
	#Cannyアルゴリズムによりエッジ検出
	cv.Canny(self.__grayPict,self.__grayPict,50,200,3)
	#計算領域の確保
	storage = cv.CreateMemStorage(0)
	#標準的ハフ変換により線の検出
	self.__lines = cv.HoughLines2(self.__grayPict,storage,cv.CV_HOUGH_STANDARD,1,cv.CV_PI/180.0,50,0,0)
	#self.__drawHoughLine(lines)
	

    #角度計算を行う．
    #計算結果は__degreeに格納．
    #__lines使用
    #TBD :ちゃんとした計算する．
    def __calcDegree(self):
	for i in range((len(self.__lines)/2)):
	    (rho,theta) = self.__lines[i]
	retDeg = theta * 180/math.pi
	self.__degree = retDeg

    #角度の計算
    def detectHorizon(self):
	self.__calcHough()
	self.__calcDegree()

    #水平を検出する
    #返り値:degree
    def getHorizon(self):
	print self.__degree
	return self.__degree


    ##テスト用メソッド
    def __drawHoughLine(self,lines):
	#for (rho,theta) in lines:
	for i in range(100):
	    (rho,theta) = lines[i]
	    a=math.cos(theta)
	    b=math.sin(theta)
	    x0 = a* rho
	    y0 = b* rho
	    pt1X = cv.Round(x0+1000*(-b))
	    pt1Y = cv.Round(y0+1000*(a))
	    pt2X = cv.Round(x0-1000*(-b))
	    pt2Y = cv.Round(y0-1000*(a))
	    #cv.Line(self.pictColor,(pt1X,pt1Y),(pt2X,pt2Y),cv.CV_RGB(255,0,0),1,8,0)
	    cv.Line(self.__grayPict,(pt1X,pt1Y),(pt2X,pt2Y),cv.CV_RGB(255,255,255),1,8,0)

#	pilImage = Image.fromstring('RGB', cv.GetSize(self.pictColor),self.pictColor.tostring(),'raw','BGR',self.pictColor.width*3,0)

#	pilImage.save("./test.jpg")
	
	cv.ShowImage("test",self.pictColor)
	#cv.ShowImage("test",self.__grayPict)
	cv.WaitKey(0)

    def test(self,pictColor):
	self.pictColor = pictColor
    
