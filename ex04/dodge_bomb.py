import pygame as pg
import sys

def main():

    pg.display.set_caption("逃げろこうかとん")#ウィンドウの名前
    scrn_sfc=pg.display.set_mode((1600,900))#ウィンドウの大きさ設定
    pgbg_sfc=pg.image.load("fig/pg_bg.jpg")#背景用画像のロード

if __name__=="__main__":
    pg.init()
    main()

    pg.quit()
    sys.exit()
