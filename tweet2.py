#encoding:utf-8
import re
import glob
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
seq = {}

#
date = []
with open("date.txt","r",encoding = "utf-8") as f:
    date = f.read().splitlines()
    
data = []

#ファイルを開く(特殊文字があるのでエンコード指定必須)
with open("list.txt","r",encoding = "utf-8") as f:
    l = f.readlines()
    for i in range(len(l)):
        rankdate = []
        word = l[i].replace("\t\n","").split("\t")
        keyword = (word.pop(0))
        rankdate.append(keyword)

        length = len(word)
        seqrank = {}
        seqnum = {}
        n = 0
        s = 1
        for i in word:
            day,rank,number = i.split(",")

#日付に対応した順位と数を示す項目を作成する
            seqrank[day] = rank
#            print(seqrank)
            seqnum[day] = number
#            print(seqnum)

#try文　データがあれば表示　なければ2000を表示
        for d in date:
#             print(d)
            try:
                rankdate.append(int(seqrank[d]))
            except:
                rankdate.append(2000)
        data.append(rankdate)
#print(data)
date = date.insert(0,"keyword")
df = pd.DataFrame(data,columns=date)
print(df.head())
plt.plot(df)
plt.show()

            
#            print(day)

#            print(word[n:n+s:1])
#            n += s
#            if n >= length:
#                break

#キーワードが辞書になければ項目を新しく作成する
#        try:
#            seq[word[0]]
#        except KeyError:
#            seq[word[0]] = []

#        seq[word[0]].append(i + 1)
