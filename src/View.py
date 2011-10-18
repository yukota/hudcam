#!/usr/bin/env python
#coding:utf-8

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *

"""
viewを作成したらコールバック
"""

class View:

    def __init__(self,controller):
	
	#instance of DataModel
	self.__controller = controller
	print "initView"

	self.setup()

	glutMainLoop()


    def draw(self):
	#バッファのクリア
	glClearColor(0.0,0.0,0.0,0.0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	#OpenGL描画
	self.drawBase()
	glFlush()
	#ダブルバッファ交換
	glutSwapBuffers()

    """
    手前のUIの作成
    円
    中心照準
    """
    def drawBase(self):
	print "refresh"

	self.updateDisplay()
	r = 0.9
	for i in range(0,360):
	    i2 =  i+10
	    iRad = i / 180.0 * 3.14
	    i2Rad = i2 /180.0 *3.14


	    x1 = r * cos(iRad)
	    y1 = r * sin(iRad)


	    x2 = r * cos(i2Rad)
	    y2 = r * sin(i2Rad)

	    glBegin(GL_LINES)
	    glVertex2f(x1,y1)
	    glVertex2f(x2,y2)
	    glEnd()


	#カメラ画像用板
	#テクスチャの設定
	glEnable(GL_TEXTURE_2D)
	glBindTexture(GL_TEXTURE_2D, self.cameraTexture)
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
	#オブジェクトの作成
	glBegin(GL_QUADS)
	glTexCoord2f(1,1)
	glVertex2f(-0.5,-0.5)
	
	glTexCoord2f(1,0)
	glVertex2f(-0.5,0.5)

	glTexCoord2f(0,0)
	glVertex2f(0.5,0.5)

	glTexCoord2f(0,1)
	glVertex2f(0.5,-0.5)
	glEnd()
	glDisable(GL_TEXTURE_2D)


	#水平器の作成
	#内部半径,外部半径,分割数
	#角度取得,水平で0degree
	horizonArg = self.__controller.getHorizon()
	upperHorizonArg = -85 - horizonArg
	underHorizonArg = 95 - horizonArg

	#水平時上半分
	gluPartialDisk(gluNewQuadric(),0.8,0.85,32,32,upperHorizonArg,170)

	#水平時下半分
	gluPartialDisk(gluNewQuadric(),0.8,0.85,32,32,underHorizonArg,170)




    def setup(self):
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(640, 480)
	glutCreateWindow("MainView")

	#3d
	glMatrixMode(GL_PROJECTION)
	glutDisplayFunc(self.draw)

#	glEnable(GL_TEXTURE_2D)
	print "ss"
	#イベントがないときに更新
	#glutTimerFuncにするかは検討する
	glutIdleFunc(self.draw)
#	glutIdleFunc(self.updateDisplay)

    def updateDisplay(self):
	cameraData = self.__controller.getCameraPict()
	self.cameraTexture = self.__pil2texture(cameraData)


    #PIL画像をテクスチャに変換する
    def __pil2texture(self,pilData):

	cnvData =pilData.resize((128,128))
	pilData.save("temp.jpg")
	width,height = cnvData.size
	data = cnvData.tostring()
	#テクスチャ番号の取得
	print width
	tex = glGenTextures(1)
	print "b"
	glBindTexture(GL_TEXTURE_2D,tex)
	print "end"
	glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,width,height,\
	0,GL_RGB,GL_UNSIGNED_BYTE,data)
	print "end"
	return tex


