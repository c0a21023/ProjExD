import tkinter as tk
import tkinter.messagebox as tkm
#-/+のマイナス、プラスの反転は未実装である
w=5#デフォルトのボタンの幅
h=3#デフォルトのボタンの高さ
f1=30#デフォルトのボタンとテキストのフォントの大きさ
r, c = 2, 0
root=tk.Tk()
root.title("tk")
root.geometry("300x500")
root.configure(bg="black")
button_li=["÷","×","-","+","="]
sub_bli=["AC","+/-未実装","%"]
def button_click(event):
    btn=event.widget
    txt=btn["text"]
    num_2=len(entry.get())-1
    num=entry.get()
    if len(num)>=1 and txt in button_li:
        print(num[-1])
        if num[-1] in button_li:
            entry.delete(num_2,tk.END)
        else:pass
    if txt=="=":
        num=num.replace('×','*')
        num=num.replace('÷','/')
        ans=eval(num)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    else:
        entry.insert(tk.END,txt)
    if txt=="AC":
        entry.delete(0,tk.END)

for i in range(9,-1,-1):
    if i>=1:
        button=tk.Button(root,text=str(i),width=w,height=h,font=("",f1))
        button.grid(row=r, column=c)
        button.configure(bg="gray33")
        button.bind("<1>",button_click)
        button.pack
    if i==0:
        button=tk.Button(root,text=str(i),width=11,height=h,font=("",f1))
        button.grid(row=r, column=c,columnspan=2)
        button.configure(bg="gray33")
        button.bind("<1>",button_click)
        button.pack   
        button=tk.Button(root,text=".",width=w,height=h,font=("",f1))
        button.grid(row=r, column=c+2,)
        button.configure(bg="gray33")
        button.bind("<1>",button_click)     
    c += 1
    if c%3 == 0:
        r += 1
        c = 0

for num,i in enumerate(button_li,1):
    button=tk.Button(root,text=i,width=w,height=h,font=("",f1))
    button.configure(bg="gray33")
    button.grid(row=num, column=4)
    button.bind("<1>",button_click)
for num,i in enumerate(sub_bli):
    button=tk.Button(root,text=i,width=w,height=h,font=("",f1))
    button.configure(bg="gray33")
    button.grid(row=1, column=num)
    # print(num)
    button.bind("<1>",button_click)
entry=tk.Entry(width=25,font=("",f1))
# entry=tk.Entry(font=f1)
# entry.place(width=25,height=20,)
entry.insert(tk.END,"")
entry.configure(bg="black",fg="white")

entry.grid(row=0,column=0,columnspan=5)
entry.pack
root.mainloop()