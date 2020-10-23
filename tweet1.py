#encoding:utf-8
import re
import glob
seq = {}

#ファイルからキーワードの順位と回数を抜き出す
def terms(f):
    global seq

    #ファイル名から日付を取り出す
    day = re.search("202\d-[0|1]\d-[0-3]\d",f).group()

    #ファイルを開く(特殊文字があるのでエンコード指定必須)
    with open(f,"r",encoding = "utf-8") as f:
        l = f.readlines()
        for i in range(len(l)):
           word = l[i].replace("\n","").split(",")

           #キーワードが辞書になければ項目を新しく作る
           try:
               seq[word[0]]
           except KeyError:
               seq[word[0]] = []

           #辞書にキーワードの日付と順位と回数を追加する
           seq[word[0]].append([day,i + 1,int(word[1])])
    return seq

#ファイル名を取得する
files = glob.glob('/home/takada/covid19_twitter/dailies/**', recursive=True) 

#ファイル名に1000termsを含むファイルだけを取り出す
files_1000 = [s for s in files if '1000terms' in s]

#全ファイルからキーワードと順位を抜き出す
for f in files_1000:
    terms(f)

#キーワードを取り出す(結果:5150単語)
#for mykey in seq.keys():
#    print(mykey)

#キーワードと値のペアを取り出す
for mykey, myvalue in seq.items():
    print(mykey,end="\t")
    for value in myvalue:
#        print(value)
        print(",".join(map(str,value)),end="\t")
    print("")
#print(seq)

    
    
    
