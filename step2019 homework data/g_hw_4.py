# インポートする
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np



# nicknames一覧を辞書化しておく
def nicknames_dict(file1):
    with open(file1, 'r') as nn:
        nn_dict = {}
        for line in nn:
            #nn_list.append(line.split('\t', '\n'))
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

# 隣接リストにするぞ→やめて、辞書にする
def adjacency_dict(pre_list):
    rinsetsu = {} # 元 Link_setsu_list
    for a, b in pre_list:
        if a not in rinsetsu:
            rinsetsu[a] = []
            rinsetsu[a].append(b)
        if a>0 and a-1 not in rinsetsu:
            rinsetsu[a-1] = []
        else:
            rinsetsu[a].append(b)

    return rinsetsu

# グラフの画像を作りたい
def nodes_list(link_setsu_list):
    nodes = []
    for i, n in enumerate(link_setsu_list):
        nodes.append(i)
    return nodes

# なんとなく深さを優先したい
# ほぼ適当なサイトのコピペ ありがとうございます
#path_dict = {}

def get_keys_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None


def pre_search(goal_name, start_name):
    goal = get_keys_from_value(nn_dict, goal_name)
    start_num = get_keys_from_value(nn_dict, start_name)
    path = [start_num]
    return goal, path


path_list = []
def search(goal, path):
    n = path[-1]
    if n == goal:
        #print(path)
        #print(len(path))
        #path_dict[len(path)] = path
        path_list.append([len(path)])
    else:
        for x in rinsetsu[n]:
            if x not in path:
                path.append(x)
                search(goal, path)
                path.pop()
    return min(path_list)

'''
def depthFirstSearch(start, goal):
    stack = Stack()
    start.setVisited()
    stack.push( start )
    while not stack.empty():
        node = stack.top()
        if node == goal:
            return stack # stack には2頂点間の経路が入っている
        else:
            child = node.findUnvisitedChild()
            if child == none:
                stack.pop()
            else:
                child.setVisited()
                stack.push( child )
'''


# SNS
file1 = 'nicknames.txt'
file2 = 'links.txt'


# Wiki
#file1 = 'wikipedia_links/pages.txt'
#file2 = 'wikipedia_links/links.txt'

#goal_name = 'jacob'
goal_name = input('goal name: ')
#start_name = 'marshall'
start_name = input('start name: ')

nn_dict = nicknames_dict(file1)
pre_list = links_list(file2)
rinsetsu = adjacency_dict(pre_list)
#print(rinsetsu)
goal, path = pre_search(goal_name, start_name)
print(search(goal, path))
#min(path_dict) = search(23,[34])
#print(get_keys_from_value(nn_dict, 'ray'))

#print(path_dict)

#print(min(path_dict))

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

nx.draw_networkx(G)
plt.show()
'''
#from IPython.display import Image
#A = nx.nx_agraph.to_agraph(G)
#Image(A.draw(format='png', prog='dot'))
