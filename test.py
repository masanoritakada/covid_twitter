#encoding:utf-8
#% matplotlib inline
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
# ここにグラフを描画してファイルに保存する処理

x = [100, 200, 300, 400, 500, 600]
y = [10, 20, 30, 50, 80, 130]

plt.plot(x, y);
plt.savefig("hoge.png")

#データの読み込み
df1 = pd.read_csv('test.txt', sep='\t', index_col=0)

df1.plot()
a = df1.plot()
a.savefig("hoge.png")
