from pynput.mouse import Button,Controller
###
#import time

class mouseController:
    #创建鼠标对象
    @classmethod
    def createMouseObject(cls):
        mouse=Controller()
        return mouse

    #获取鼠标当前位置
    @classmethod
    def getMousePosition(cls,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        return mouse.position

    #鼠标移动(a,b)距离
    @classmethod
    def mouseTeleportDistance(cls,position1,position2,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.move(position1,position2)

    #鼠标传送到指定地点
    @classmethod
    def mouseTeleportToSP(cls,position1,position2,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.position=(position1,position2)

    #按像素移动鼠标至指定地点
    @classmethod
    def mouseMoveByStep(cls,position1,position2,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        positA,positB=mouse.position
        ###
        #print(positA,positB)
        disA=position1-positA
        disB=position2-positB

        if disA>0 and disB>0:
            for i in range(disA):
                mouse.move(1,0)
            for j in range(disB):
                mouse.move(0,1)
        if disA>0 and disB<0:
            for i in range(disA):
                mouse.move(1,0)
            for j in range(disB):
                mouse.move(0,-1)
        if disA<0 and disB>0:
            for i in range(disA):
                mouse.move(-1,0)
            for j in range(disB):
                mouse.move(0,1)
        if disA<0 and disB<0:
            for i in range(disA):
                mouse.move(-1,0)
            for j in range(disB):
                mouse.move(0,-1)
        ###
        #print(mouse.position)

    #按住鼠标左键
    @classmethod
    def mouseLeftPress(cls,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.press(Button.left)

    #释放鼠标左键
    @classmethod
    def mouseLeftRelease(cls,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.release(Button.left)

    #点击鼠标左键
    @classmethod
    def mouseLeftClick(cls,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.click(Button.left)

    #按住鼠标右键
    @classmethod
    def mouseRightPress(cls,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.press(Button.right)

    #释放鼠标右键
    @classmethod
    def mouseRightRelease(cls,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.release(Button.right)

    #点击鼠标右键
    @classmethod
    def mouseRightClick(cls,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.click(Button.right)

    #滚动鼠标dy距离 dy>0为向上滚动，dy<0为向下滚动
    @classmethod
    def mouseScroll(cls,dy,dx=0,mouseObject=None):
        if mouseObject==None:
            mouse=Controller()
        else:
            mouse=mouseObject
        mouse.scroll(dx,dy)

#test for mouseController
# mouse=mouseController.createMouseObject()

# position=mouseController.getMousePosition(mouse)
# print(position)

# mouseController.mouseTeleportDistance(-200,-500,mouse)
# time.sleep(3)
# position=mouseController.getMousePosition(mouse)
# print(position)

# mouseController.mouseTeleportToSP(1280,520)
# time.sleep(3)
# mouseController.mouseLeftPress(mouse)
# mouseController.mouseMoveByStep(1560,1040)
# time.sleep(5)
# print(mouse.position)
# mouseController.mouseLeftRelease(mouse)

# mouseController.mouseTeleportToSP(1280,520)
# mouseController.mouseRightPress(mouse)
# mouseController.mouseMoveByStep(1560,1040)
# time.sleep(5)
# print(mouse.position)
# mouseController.mouseRightRelease(mouse)
# time.sleep(6)

# mouseController.mouseTeleportToSP(1092,1325)
# mouseController.mouseLeftClick(mouse)
# time.sleep(3)
# mouseController.mouseRightClick(mouse)

# for i in range(100):
#     mouseController.mouseScroll(-10)