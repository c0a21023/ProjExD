import pygame as pg
import random
import sys
import time
import math


class Screen:
    def __init__(self,title,wh,imb_path):#self,ウィンドウの名前、ウィンドウの大きさ、背景画像のパス
        pg.display.set_caption(title)#ウィンドウの名前
        self.sfc=pg.display.set_mode(wh)#ウィンドウの大きさ設定
        self.rct=self.sfc.get_rect()
        self.bgi_sfc=pg.image.load(imb_path)#背景用画像のロード
        self.bgi_rct=self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }
    key_orig={
        pg.K_1: "fig/1.png",
        pg.K_2: "fig/2.png",
        pg.K_3: "fig/3.png",
        pg.K_4: "fig/4.png",
        pg.K_5: "fig/5.png",
    }
    def __init__(self,img_path,ratio,xy):#self,画像パス、比率、座標タプル
            self.sfc = pg.image.load(img_path)#"fig/6.png"
            self.sfc = pg.transform.rotozoom(self.sfc,0,ratio)#tori_sfc, 0, 2.0
            self.rct = self.sfc.get_rect()
            self.rct.center = xy#900, 400
    
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        for key, delta in Bird.key_orig.items():
            if key_dct[key]:
                self.sfc=pg.image.load(delta)
                self.sfc=pg.transform.rotozoom(self.sfc,0,2.0) 
        self.blit(scr)


class Bomb:
    def __init__(self,color,rad,vxy,scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad)) # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc,color,(rad,rad),rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx,self.vy=vxy
    
    def dead(self):
        self.vx,self.vy=0,0

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr):
        self.rct.move_ip(self.vx,self.vy)
        self.sfc.blit(self.sfc, self.rct) 
        yoko, tate = check_bound(self.rct,scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)

        
def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def after_d(scr,bird):#フォントを生成する関数
    flag=False
    dict=pg.key.get_pressed()#辞書型
    font1=pg.font.SysFont("Meiryo UI",50)
    text1=font1.render("ゲームに失敗しました。",True,(0,0,150))
    text2=font1.render("もう一度遊ぶにはSpaceを押してください",True,(0,0,150))
    scr.sfc.blit(text1,(550,200))
    scr.sfc.blit(text2,(300,250))
    bird.sfc=pg.image.load("fig/8.png")
    x1,y1=0,0
    bird.rct.center=scr.rct.centerx,scr.rct.centery
    bird.sfc=pg.transform.rotozoom(bird.sfc,0,3.0)
    scr.sfc.blit(bird.sfc,bird.rct)
    if dict[pg.K_SPACE]: 
        flag=True
        main()

    return flag


def main():
    time_sta=time.time()
    clock =pg.time.Clock()
    count_up=0
    mov_flag=True

    scr=Screen("負けるな！こうかとん",(1500,750),"fig/pg_bg.jpg")
 
    TUTbird=Bird("fig/6.png",2.0,(900,400))
    TUTbird.update(scr)

    kbm_lst=[]
    bom_nm=1
    bom_ds=4
    for _ in range(bom_nm):
        spd=1
        vxy=(random.choice([-1*spd,spd]),random.choice([-1*spd,spd]))
        kbm=Bomb((255,0,0),10,vxy,scr)
        kbm_lst.append(kbm)
        kbm.update(scr)

    time1=time.time()-time_sta

    while True:
        scr.blit()
        time1=time.time()-time_sta
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
                
        if mov_flag:
            TUTbird.update(scr)
            if math.floor(time1)%bom_ds==0 and count_up!=math.floor(time1):
                spd=1
                vxy=(random.choice([-1*spd,spd]),random.choice([-1*spd,spd]))
                kbm=Bomb((255,0,0),10,vxy,scr)
                kbm_lst.append(kbm)
                kbm.update(scr)
                bom_nm+=1
                count_up=math.floor(time1)
            for i in range(bom_nm):
                # print(i)
                kbm_lst[i].update(scr)
                if TUTbird.rct.colliderect(kbm_lst[i].rct):
                    mov_flag=False
        else:
            for i in range(bom_nm):
                # print(i)
                kbm_lst[i].dead()    
                kbm_lst[i].update(scr)  
            mov_flag=after_d(scr,TUTbird)
            if mov_flag==True: return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()