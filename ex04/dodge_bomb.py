import pygame as pg
import sys

def main():
    clock=pg.time.Clock()


    pg.display.set_caption("逃げろこうかとん")#ウィンドウの名前
    scrn_sfc=pg.display.set_mode((1600,800))#ウィンドウの大きさ設定
    pgbg_sfc=pg.image.load("fig/pg_bg.jpg")#背景用画像のロード
    pgbg_rct=pgbg_sfc.get_rect()


    tori_sfc=pg.image.load("fig/6.png")#こうかとんの画像のロード
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400
    scrn_sfc.blit(tori_sfc,tori_rct)


    while True:
        scrn_sfc.blit(pgbg_sfc,pgbg_rct)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
        pg.display.update()
        clock.tick(1000)


if __name__=="__main__":
    pg.init()
    main()

    pg.quit()
    sys.exit()
