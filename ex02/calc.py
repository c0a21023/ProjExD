import tkinter as tk
import tkinter.messagebox as tkm
    

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    if txt=="=":
        num=entry.get()
        ans=eval(num)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
    else:
        entry.insert(tk.END,txt)
root=tk.Tk()
root.title("tk")
root.geometry("300x500")
button0=tk.Button(root,text="0",width=4,height=2,font=30)
button0.grid(row=4,column=0,columnspan=1)
button0.bind("<1>",button_click)
button0.pack
button1=tk.Button(root,text="1",width=4,height=2,font=30)
button1.grid(row=3,column=2,columnspan=1)
button1.bind("<1>",button_click)
button1.pack
button2=tk.Button(root,text="2",width=4,height=2,font=30)
button2.grid(row=3,column=1,columnspan=1)
button2.bind("<1>",button_click)
button2.pack
button3=tk.Button(root,text="3",width=4,height=2,font=30)
button3.grid(row=3,column=0,columnspan=1)
button3.bind("<1>",button_click)
button3.pack
button4=tk.Button(root,text="4",width=4,height=2,font=30)
button4.grid(row=2,column=2,columnspan=1)
button4.bind("<1>",button_click)
button4.pack
button5=tk.Button(root,text="5",width=4,height=2,font=30)
button5.grid(row=2,column=1,columnspan=1)
button5.bind("<1>",button_click)
button5.pack
button6=tk.Button(root,text="6",width=4,height=2,font=30)
button6.grid(row=2,column=0,columnspan=1)
button6.bind("<1>",button_click)
button6.pack
button7=tk.Button(root,text="7",width=4,height=2,font=30)
button7.grid(row=1,column=2,columnspan=1)
button7.bind("<1>",button_click)
button7.pack
button8=tk.Button(root,text="8",width=4,height=2,font=30)
button8.grid(row=1,column=1,columnspan=1)
button8.bind("<1>",button_click)
button8.pack
button9=tk.Button(root,text="9",width=4,height=2,font=30)
button9.grid(row=1,column=0,columnspan=1)
button9.bind("<1>",button_click)
button9.pack
# for i in range(9,0,-1):
#     button=tk.Button(root,text=str(i),width=4,height=2,font=30)
#     row_n=(i%3)
#     column_n=3-(i//3)
button_p=tk.Button(root,text="+",width=4,height=2,font=30)
button_p.grid(row=4,column=1,columnspan=1)
button_p.bind("<1>",button_click)
button_p.pack
button_e=tk.Button(root,text="=",width=4,height=2,font=30)
button_e.grid(row=4,column=2,columnspan=1)
button_e.bind("<1>",button_click)
button_e.pack
entry=tk.Entry(width=30)
entry.insert(tk.END,"")
entry.grid(row=0,column=0,columnspan=3)
entry.pack
root.mainloop()