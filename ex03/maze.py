import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import random
def key_down(event):#キーを押したときに押したキーの取得を行う関数
    global key
    key=event.keysym
def key_up(event):#キーを話したときに取得したキーをなくす関数
    global key
    key=""

def finish(event):#エンターを押したときに、ゴールかどうかを判定する関数
    global wall_his
    ax=ans_bl[0]
    ay=ans_bl[1]
    if  ax==mx and ay==my:#ゴールであるかの判定
        canvas.itemconfig(image=tori6, tagOrId="koukaton")#こうかとんの画像変更
        tkm.showinfo("congrats!!",f"you made it!!\nit took {mov_his}steps!!")#メッセ―ジの出力
    else:#ゴールではない場合
        canvas.itemconfig(image=tori0, tagOrId="koukaton")#こうかとんの画像変更
        wall_his=mov_his#画像変更場所の保存




def main_proc():#おもに行う処理
    global cx,cy,mx,my,mov_his,wall_his
    if maze_lst[mx][my]==0:#道へ移動する場合
        if key=="Up":
            my-=1
            mov_his+=1#歩数の保存
        if key=="Down":
            my+=1
            mov_his+=1
        if key=="Left":
            mx-=1
            mov_his+=1
        if key=="Right":
            mx+=1
            mov_his+=1
        
    if maze_lst[mx][my]==1:#壁へ移動する場合
        if key=="Up": my+=1
        if key=="Down": my-=1
        if key=="Left": mx+=1
        if key=="Right": mx-=1
        canvas.itemconfig(image=tori8, tagOrId="koukaton")#泣いているこうかとんへの変更
        wall_his=mov_his#画像変更場所の保存
    if mov_his-wall_his==1:#画像変更した場所から1マス移動した場合
        canvas.itemconfig(image=tori3, tagOrId="koukaton")#初期状態の画像への変更

    # print(mov_his)

        
    cx,cy=mx*100+50,my*100+50
    canvas.coords("koukaton",cx,cy)
    if key=="1":
        canvas.itemconfig(image=tori1, tagOrId="koukaton")
        wall_his=mov_his
        #canvas.create_image(cx,cy,image=tori3,tag="koukaton3")
        #canvas.pack()

    root.after(100,main_proc)#0.1秒ごとのmain_procの呼び出し

if __name__ == "__main__":
    root = tk.Tk()
    mov_his=0#歩数の変数
    wall_his=0#画像変更場所の保存変数
    root.title("迷えるこうかとん")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_lst=mm.make_maze(15,9)#迷路のリスト作成
    mm.show_maze(canvas,maze_lst)#迷路リストから迷路の出力
    d_end=[]
    for x in range(1,14):#作成された迷路からふくろこうじになっているマスの位置をリストとして保存
        for y in range(1,8):
            wall_num=0
            if maze_lst[x][y]==0:
                if maze_lst[x][y+1]==1:
                    wall_num+=1
                if maze_lst[x][y-1]==1:
                    wall_num+=1
                if maze_lst[x-1][y]==1:
                    wall_num+=1
                if maze_lst[x+1][y]==1:
                    wall_num+=1
            if wall_num==3:
                d_end.append((x,y))#暫定ゴールリストへの追加
    # print(d_end)
    d_end.pop(0)#暫定ゴールリストからスタート位置の削除
    ans_bl=random.choice(d_end)
    # ans_bl=d_end[1]
    # print(maze_lst)
    print(ans_bl)
    tori0=tk.PhotoImage(file="fig/0.png")#画像変数の作成
    tori1=tk.PhotoImage(file="fig/1.png")#画像変数の作成  
    tori3=tk.PhotoImage(file="fig/3.png")#画像変数の作成
    tori6=tk.PhotoImage(file="fig/6.png")#画像変数の作成
    tori8=tk.PhotoImage(file="fig/8.png")#画像変数の作成
    mx,my=1,1#マス座標の初期値の作成
    cx,cy=mx*100+50,my*100+50#こうかとんの座標変数
    canvas.create_image(cx,cy,image=tori3,tag="koukaton")#こうかとんの初期状態の作成
    canvas.pack()
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.bind("<Return>",finish)
    root.mainloop()
