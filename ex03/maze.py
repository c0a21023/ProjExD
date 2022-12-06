import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm
import random
def key_down(event):
    global key
    key=event.keysym
def key_up(event):
    global key
    key=""

def finish(event):
    global wall_his
    ax=ans_bl[0]
    ay=ans_bl[1]
    if  ax==mx and ay==my:
        canvas.itemconfig(image=tori6, tagOrId="koukaton")
        tkm.showinfo("congrats!!",f"you made it!!\nit took {mov_his}steps!!")
    else:
        canvas.itemconfig(image=tori0, tagOrId="koukaton")
        wall_his=mov_his




def main_proc():
    global cx,cy,mx,my,mov_his,wall_his
    if maze_lst[mx][my]==0:
        if key=="Up":
            my-=1
            mov_his+=1
        if key=="Down":
            my+=1
            mov_his+=1
        if key=="Left":
            mx-=1
            mov_his+=1
        if key=="Right":
            mx+=1
            mov_his+=1
        
    if maze_lst[mx][my]==1:
        if key=="Up": my+=1
        if key=="Down": my-=1
        if key=="Left": mx+=1
        if key=="Right": mx-=1
        canvas.itemconfig(image=tori8, tagOrId="koukaton")
        wall_his=mov_his
    if mov_his-wall_his==1:
        canvas.itemconfig(image=tori3, tagOrId="koukaton")

    # print(mov_his)

        
    cx,cy=mx*100+50,my*100+50
    canvas.coords("koukaton",cx,cy)
    if key=="1":
        canvas.itemconfig(image=tori1, tagOrId="koukaton")
        wall_his=mov_his
        #canvas.create_image(cx,cy,image=tori3,tag="koukaton3")
        #canvas.pack()

    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    mov_his=0
    wall_his=0
    root.title("迷えるこうかとん")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_lst=mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)
    d_end=[]
    for x in range(1,14):
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
                d_end.append((x,y))
    # print(d_end)
    d_end.pop(0)
    ans_bl=random.choice(d_end)
    # ans_bl=d_end[1]
    # print(maze_lst)
    print(ans_bl)
    tori0=tk.PhotoImage(file="fig/0.png")
    tori1=tk.PhotoImage(file="fig/1.png")    
    tori3=tk.PhotoImage(file="fig/3.png")
    tori6=tk.PhotoImage(file="fig/6.png")
    tori8=tk.PhotoImage(file="fig/8.png")
    mx,my=1,1
    cx,cy=mx*100+50,my*100+50
    canvas.create_image(cx,cy,image=tori3,tag="koukaton")
    canvas.pack()
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.bind("<Return>",finish)
    root.mainloop()
