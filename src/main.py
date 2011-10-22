#!/user/bin/env python
# coding: UTF-8

from Model import *
from Controller import *
from View import *

#modelの作成
model = Model()

#controllerの作成
controller = Controller(model)

#viewの作成
view = View(controller)
