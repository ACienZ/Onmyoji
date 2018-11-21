#ControllerNode
#user to control mouse and keyboard

#2018.11.21
#create class

from pynput.mouse import Button,Controller

class controllerNode:

    @classmethod
    def mouseteleport(cls,position1,position2):
        mouse=Controller()
        mouse.move(position1,position2)

    @classmethod
    def mouseMove(cls,position1,position2):
        mouse=Controller()
        positA,positB=mouse.position
        ###########
        print(positA,positB)
        for i in range(position1):
            for j in range(position2):

