import datetime
import random
def shutudai():
    quize_li=["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    return random.choice(quize_li)

def kaitou(quize):
    ans=input("答えてくれ:")
    ans_li=[["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
    if quize=="サザエの旦那の名前は？" and (ans in ans_li[0]) or quize=="カツオの妹の名前は？" and (ans in ans_li[1]) or quize=="タラオはカツオから見てどんな関係？" and (ans in ans_li[2]):
        return print("正解‼")
    else:
        print("出直しましょう")


if __name__=="__main__":
    quize=shutudai()
    print(quize)
    st = datetime.datetime.now()
    kaitou(quize)
    ed = datetime.datetime.now()
    print((ed-st).seconds)