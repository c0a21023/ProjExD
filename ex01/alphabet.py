import random
import datetime

al_li=random.sample([chr(ord("A")+i) for i in range(26)],10)
num=random.randint(1,4)
delal_li=random.sample(al_li,num)
status=False
count=0

def algame():
    global status,count
    count+=1
    te_li=al_li.copy()
    alsen=' '.join(al_li)
    dlsen=' '.join(delal_li)
    print(f"対称文字:\n{alsen}")
    print(f"欠損文字:\n{dlsen}")
    for i in delal_li:
        if i in te_li:
            te_li.remove(i)
    te_li=' '.join(te_li)
    print(f"表示文字:\n{te_li}")
    a=input("欠損文字はいくつあるでしょうか？")
    if int(a)==len(delal_li):
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(int(a)):
            b=input(f"{i+1}つ目の文字を打ってください:")
            if b not in delal_li:
                break
        
            status=True
    else:
        pass

if __name__=="__main__":
    st = datetime.datetime.now()
    while status==0 and count<=4:
        algame()
        life=5-count
        if status==0 and life>=1:
            print(f"不正解です。またチャレンジしてください。\nのこりのチャレンジ回数は{life}回です。\n","-"*60)
        if status==0 and life==0:
            print(f"不正解です。残りのチャレンジ回数はなくなってしまったのでチャレンジはできません。")
    ed = datetime.datetime.now()
    if status==1:
        print("すべて正解です。おめでとうございます。")
        print(f"所要時間は{(ed-st).seconds}秒でした。")

