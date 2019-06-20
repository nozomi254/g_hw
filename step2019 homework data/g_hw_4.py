# インポートする
import networkx as nx
import string

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


nn_dict = nicknames_dict('nicknames.txt')
pre_list = links_list('links.txt')
link_setsu_list = adjacency_list(pre_list)

print(link_setsu_list)
