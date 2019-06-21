# インポートする
import matplotlib.pyplot as plt
import networkx as nx



# nicknames一覧を辞書化しておく
def nicknames_dict(file1):
    with open(file1, 'r') as nn:
        nn_dict = {}
        for line in nn:
            #nn_list.append(line.split('\t', '\n')) ←めんどいだるいできない
            num, nickname = line.split()
            nn_dict[int(num)] = nickname
    return nn_dict
# links一覧はリスト化する
def links_list(file2):
    with open(file2, 'r') as links:
        pre_list = []
        for line in links:
            num1, num2 = line.split()
            pre_list.append([int(num1), int(num2)])
    return pre_list

# 隣接リストにするぞ
def adjacency_list(pre_list):
    link_setsu_list = [] # ダサい
    for i in range(49):
        follower_list = []
        link_setsu_list.append(follower_list)
        for j in pre_list:
            if j[0] == i:
                follower_list.append(j[1])
    return link_setsu_list

# グラフの画像を作りたい
def nodes_list(link_setsu_list):
    nodes = []
    for i, n in enumerate(link_setsu_list):
        nodes.append(i)
    return nodes

# なんとなく深さを優先したい
# ほぼ適当なサイトのコピペ ありがとうございます
path_dict = {}
path_list = []
def search(goal, path):
    n = path[-1]
    if n == goal:
        #print(path)
        #print(len(path))
        #path_dict[len(path)] = path
        path_list.append([len(path)])
    else:
        for x in link_setsu_list[n]:
            if x not in path:
                path.append(x)
                search(goal, path)
                path.pop()
    return path_list


nn_dict = nicknames_dict('nicknames.txt')
pre_list = links_list('links.txt')
link_setsu_list = adjacency_list(pre_list)
#path_dict = search(23,[34])
path_dict = search(23,[34])

#print(path_dict)
print(min(path_list)) #最短距離のみを出す
#print(min(path_dict))
#search(23,[34]) #23:jacobにたどり着くまでの34:marshallからのルートとその長さ
#print(link_setsu_list)

'''
最短(目視&手動w)は
[34, 29, 23]
3
[34, 42, 23]
3
'''

'''
nodes = nodes_list(link_setsu_list)
edges = pre_list

G = nx.DiGraph()
# ノード一覧を追加する。
G.add_nodes_from(nodes)
# エッジ一覧を追加する。
G.add_edges_from(edges)

from IPython.display import Image
A = nx.nx_agraph.to_agraph(G)
Image(A.draw(format='png', prog='dot'))
'''
