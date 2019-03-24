#ControllerNode
#user to control mouse and keyboard

#2018.11.21
#create class

from mouse import mouseController
from keyboard import keyboardController
import sqlite3
import socket
###
#import time


#控制鼠标键盘具体实现
class ControllerNode:
    pass

#侦听线程
def listener():
    pass

#请求处理函数
def solver():
    pass

def controllerManager():
    #连接数据库
    conn=sqlite3.connect('./controller/test.db')
    cursor=conn.cursor()
    #开启侦听线程

    #接收请求调用ControllerNode进行处理

controllerManager()