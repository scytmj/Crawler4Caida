# coding:utf-8
"""
create on June 28, 2020 By Wenyan YU
Function:

ASlay算法三维坐标已可导出，Matplotlib和echarts均不支持大规模网络的三维展示
因此寻求Mayavi或Open3D作为解决方案

本程序主要研究ASlay plus Mayavi所带来的更多可能性

"""
import time


def read_as_graph(graph_nodes_file, graph_edges_file):
    """
    读取文件中的节点和连边关系数据
    :param graph_nodes_file:
    :param graph_edges_file:
    :return graph_nodes_list:
    :return graph_edges_list:
    """
    graph_nodes_list = []
    graph_edges_list = []
    graph_nodes_file_read = open(graph_nodes_file, 'r', encoding='utf-8')
    graph_edges_file_read = open(graph_edges_file, 'r', encoding='utf-8')

    for line in graph_nodes_file_read.readlines():
        line = line.strip().split(',')
        graph_nodes_list.append(line)
    for line in graph_edges_file_read.readlines():
        line = line.strip().split(',')
        graph_edges_list.append(line)

    return graph_nodes_list, graph_edges_list


def mayavi_draw(graph_nodes, graph_edges):
    """
    根据三维信息，绘制三维图例
    :param graph_nodes:
    :param graph_edges:
    :return:
    """
    print(graph_nodes)
    print(graph_edges)


if __name__ == "__main__":
    time_start = time.time()  # 记录启动时间
    my_graph_nodes_file = '../000LocalData/BGPlay/as_graph_3d_nodes.csv'
    my_graph_edges_file = '../000LocalData/BGPlay/as_graph_3d_edges.csv'
    my_graph_nodes, my_graph_edges = read_as_graph(my_graph_nodes_file, my_graph_edges_file)
    mayavi_draw(my_graph_nodes, my_graph_edges)
    time_end = time.time()  # 记录结束时间
    print("=>Scripts Finish, Time Consuming:", (time_end - time_start), "S")

