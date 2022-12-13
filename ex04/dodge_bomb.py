import pygame as pg
import random
import sys


def check_bound(obj_rct,scr_rct):
    #第1引数=こうかとん、bombのrect、第2引数=スクリーンrect
    yoko,tate=+1,+1
    if obj_rct.left<scr_rct.left or scr_rct.right < obj_rct.right: yoko=-1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: tate=-1
    return yoko,tate

def tori_mov(rct,s_rct):#こうかとんの動き方をまとめた関数
        dict=pg.key.get_pressed()#辞書型
        if dict[pg.K_UP]: rct.centery-=1#上キーを押した場合
        if dict[pg.K_DOWN]: rct.centery+=1#下キーを押した場合
        if dict[pg.K_LEFT]: rct.centerx-=1#左キーを押した場合
        if dict[pg.K_RIGHT]: rct.centerx+=1#右キーを押した場合
        if check_bound(rct,s_rct)!=(+1,+1):#画面外に出た判定があれば
            if dict[pg.K_UP]: rct.centery+=1#上キーを押した場合に元の位置に戻す
            if dict[pg.K_DOWN]: rct.centery-=1#下キーを押した場合に元の位置に戻す
            if dict[pg.K_LEFT]: rct.centerx+=1#左キーを押した場合に元の位置に戻す
            if dict[pg.K_RIGHT]: rct.centerx-=1#右キーを押した場合に元の位置に戻す    

def tori_dmov(rct,s_rct,flag):
    dict=pg.key.get_pressed()#辞書型
    rct.center=s_rct.centerx,s_rct.centery
    font_ren()
    if dict[pg.K_s]:
        flag=False
    return flag
    


def tori_change(tori_rct,tori_sfc,scrn_sfc):#こうかとんの画像変更関数
        dict=pg.key.get_pressed()#辞書型
        if dict[pg.K_1]:#1を押した場合
            tori_sfc=pg.image.load("fig/1.png")
            return pg.transform.rotozoom(tori_sfc,0,2.0)
        if dict[pg.K_2]:#2を押した場合
            tori_sfc=pg.image.load("fig/2.png")
            return pg.transform.rotozoom(tori_sfc,0,2.0)
        if dict[pg.K_3]:#3を押した場合
            tori_sfc=pg.image.load("fig/6.png")
            return pg.transform.rotozoom(tori_sfc,0,2.0)
        return tori_sfc#なにもなければ、tori_sfcを変更せずに返す

def bomb_make(scrn_rct):
    bomb_sfc=pg.Surface((20,20))#正方形の空のsurface
    bomb_sfc.set_colorkey(0)#黒の背景を取り除く
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)#円の描画設定
    bomb_rct=bomb_sfc.get_rect()
    bomb_rct.centerx=random.randint(0,scrn_rct.width)#x座標のランダム設定
    bomb_rct.centery=random.randint(0,scrn_rct.height)#y座標のランダム設定
    return bomb_sfc,bomb_rct

def bomb_mov(bomb_rct,scrn_rct,vx,vy):#爆弾の移動反転処理
    yoko,tate=check_bound(bomb_rct,scrn_rct)#check_bound関数で画面端に触れたか判定
    vx*=yoko#判定結果のx移動変数に反映
    vy*=tate #判定結果のy移動変数に反映
    return vx,vy#移動変数を返す


def font_ren():#フォントを生成する関数
   font1=pg.font.SysFont("Meiryo UI",50)
   text1=font1.render("ゲームに失敗しました。",True,(0,0,150))
   text2=font1.render("もう一度遊ぶにはEnterを押してください",True,(0,0,150))
   return text1,text2




def main():
    #ゲームの初期設定
    clock=pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん")#ウィンドウの名前
    scrn_sfc=pg.display.set_mode((1500,750))#ウィンドウの大きさ設定
    scrn_rct=scrn_sfc.get_rect()
    pgbg_sfc=pg.image.load("fig/pg_bg.jpg")#背景用画像のロード
    pgbg_rct=pgbg_sfc.get_rect()

    #こうかとんの初期設定
    tori_sfc=pg.image.load("fig/6.png")#こうかとんの画像のロード
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=scrn_rct.centerx,scrn_rct.centery
    scrn_sfc.blit(tori_sfc,tori_rct)
    mov_flag=False#こうかとんの状態を表す変数

    #爆弾の初期設定
    bomb_sfc,bomb_rct=bomb_make(scrn_rct)
    scrn_sfc.blit(bomb_sfc,bomb_rct)
    vx,vy= +1,+1
    bomb_sfc1,bomb_rct1=bomb_make(scrn_rct)
    scrn_sfc.blit(bomb_sfc1,bomb_rct1)
    vx1,vy1= +1,+1
    

    while True:
        
        scrn_sfc.blit(pgbg_sfc,pgbg_rct)#背景画像の呼び出し

        for event in pg.event.get():#×ボタンを押したときに処理を止める
            if event.type==pg.QUIT:
                return

        if mov_flag:#こうかとんの状態がTrue
            mov_flag=tori_dmov(tori_rct,scrn_rct,mov_flag)#こうかとんを動けなくさせる関数
            text1,text2=font_ren()
            scrn_sfc.blit(text1,(550,200))
            scrn_sfc.blit(text2,(300,250))
        else:
            tori_mov(tori_rct,scrn_rct)#こうかとんの動作関数
        tori_sfc=tori_change(tori_rct,tori_sfc,scrn_sfc)#こうかとんの画像変更関数

        
        scrn_sfc.blit(tori_sfc,tori_rct)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        scrn_sfc.blit(bomb_sfc1,bomb_rct1)
        
        bomb_rct.move_ip(vx,vy)
        bomb_rct1.move_ip(vx1,vy1)

 
        vx,vy=bomb_mov(bomb_rct,scrn_rct,vx,vy)
        vx1,vy1=bomb_mov(bomb_rct1,scrn_rct,vx1,vy1)
        

        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb_rct1):
            tori_sfc=pg.image.load("fig/8.png")
            tori_sfc=pg.transform.rotozoom(tori_sfc,0,3.0) 
            scrn_sfc.blit(tori_sfc,tori_rct)
            vx,vy=0,0
            vx1,vy1=0,0
            mov_flag=True




            

        pg.display.update()
        clock.tick(1000)


if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
