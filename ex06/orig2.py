import pygame as pg
import random
import sys
import time
import math

class Screen:
    def __init__(self,title,wh,num1,num2):#self,ウィンドウの名前、ウィンドウの大きさ、背景画像のパス
        pg.display.set_caption(title)#ウィンドウの名前
        self.sfc=pg.display.set_mode(wh,num1,num2)#ウィンドウの大きさ設定
        self.rct=self.sfc.get_rect()


    def blit(self):#Screenクラスのblit関数
        self.sfc.blit(self.sfc, self.rct) 

class bar:
    def __init__(self,collor,x,y,size,vxy,scr:Screen):
        self.sfc = pg.Surface((size))
        self.sfc.fill(collor)
        self.rct=self.sfc.get_rect()
        self.rct.centerx=x
        self.rct.centery=y
        self.vx,self.vy=None






def main():
    screen=Screen("pong",(640,480),0,32)
    clock = pg.time.Clock()
    font = pg.font.SysFont(None,40)

    #背景の設定
    back = pg.Surface((640,480))
    background = back.blit()
    screen.fill((0,0,0))

if __name__ == "__main__":
    main()