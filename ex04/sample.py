import pygame as pg
import sys
def main():
    clock=pg.time.Clock()
    time1=10
    rtime=1/time1


    pg.display.set_caption("初めてのPygame")
    scrn_sfc=pg.display.set_mode((800,600))
    
    tori_sfc=pg.image.load("fig/6.png")
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.topright=800,0
    scrn_sfc.blit(tori_sfc,tori_rct)


    pg.display.update()
    clock.tick(rtime)


if __name__=="__main__":

    pg.init()
    main()
    pg.quit()
    sys.exit()