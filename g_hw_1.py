# coding: UTF-8
# https://uxmilk.jp/8851
with open('dictionary.words.html', 'r') as f:
    # /usr/share/dict/wordsを使うとそんな単語はないよって言われる
  lines = f.readlines()
  d_list = list(lines)
  list1 = []
  dic1 = {}
  for i in d_list:
    dic1[i.replace('\n', '')] = ''.join(sorted(i.lower().replace('\n', '')))
  # 文字を小文字にして、改行をとって、アルファベット順にソート list1

#print(dic1)

import itertools
#s = 'omnsotarer'
s = input('問題の16文字を入力：')

list2 = []
for L in range(4,len(s)+1):
    for subset in itertools.combinations(s, L):
       list2.append(''.join(sorted(subset)))
# https://codeday.me/jp/qa/20190204/221918.html
# 全ての組み合わせ

#list3 = []
#for i in list2:
  #print(list(filter(lambda x:  x[1], dic1.items())))
  #keys = [k for k, v in dic1.items() if v == i]
  #for j in range(len(keys)):
    #list3.append(keys[j])
list3 = list(filter(lambda x: x[1] in list2, dic1.items()))
list4 = []
for i in list3:
    list4.append(i[0])

# 点数計算
ls1 = ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']
ls2 = ['j', 'k', 'q', 'x', 'z']
dic3 = {}
for i in range(len(list4)):
  score = len(list4[i])
  for j in list4[i]:
    if j in ls1:
      score += 1
    if j in ls2:
      score += 2
  dic3[list4[i]] = score
# print(dic3)
# こうすると値が最大値であるキーが取得できる
# https://note.nkmk.me/python-dict-value-max-min/
max_k = max(dic3, key=dic3.get)
print(max_k)
#print(dic3)
