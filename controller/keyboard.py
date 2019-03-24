from pynput.keyboard import Key,Controller
###
#from mouse import mouseController

class keyboardController:
    @classmethod
    def createKeyboardObject(cls):
        keyboard=Controller()
        return keyboard

    #按住key键
    #key:str
    @classmethod
    def keyboardPressKey(cls,keyName,keyboardObject=None):
        if keyboardObject==None:
            keyboard=Controller()
        else:
            keyboard=keyboardObject
        keyboard.press(keyName)

    #释放key键
    @classmethod
    def keyboardReleaseKey(cls,keyName,keyboardObject=None):
        if keyboardObject==None:
            keyboard=Controller()
        else:
            keyboard=keyboardObject
        keyboard.release(keyName)

    #输出一段话
    @classmethod
    def keyboardPrint(cls,msg,keyboardObject=None):
        if keyboardObject==None:
            keyboard=Controller()
        else:
            keyboard=keyboardObject
        keyboard.type(msg)

#test for keyboardController
# keyboard=keyboardController.createKeyboardObject()
# mouseController.mouseLeftClick()
# keyboardController.keyboardPressKey('A',keyboard)
# keyboardController.keyboardReleaseKey('A',keyboard)
# keyboardController.keyboardPrint('hello world!',keyboard)