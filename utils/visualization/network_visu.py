from pyecharts import options as opts
from pyecharts.charts import Graph
import pickle
import numpy as np
from pyecharts.commons.utils import JsCode
from tqdm import tqdm


def load_data():
    # Load your data: keywords_set, keyword_info_map, coOccurrence_matrix
    with open('keyword/keywords_set.pkl', 'rb') as keywords_set_file:
        keywords_set = pickle.load(keywords_set_file)

    with open('keyword/keyword_info_map.pkl', 'rb') as keyword_info_map_file:
        keyword_info_map = pickle.load(keyword_info_map_file)

    coOccurrence_matrix = np.load('keyword/coOccurrence_matrix.npy')

    return keywords_set, keyword_info_map, coOccurrence_matrix


def nor(original_data,min_value, max_value):
    new_min = 5
    new_max = 50
    if max_value != min_value:
        normalized_value = (original_data - min_value) / (max_value - min_value)  # 归一化到 [0, 1]
        transformed_value = (normalized_value * (new_max - new_min)) + new_min  # 转换到 [new_min, new_max]
        return transformed_value

def create_keyword_network(keywords_set, keyword_info_map, coOccurrence_matrix):
    nodes = []
    edges = []

    # 创建进度条
    progress_bar = tqdm(total=len(keywords_set) * (len(keywords_set) - 1) // 2, desc="Creating Network")

    for idx, keyword_hash in enumerate(keywords_set):
        keyword_info = keyword_info_map[keyword_hash]
        keyword_name = keyword_info['keyword']
        # keyword_count = keyword_info['count']

        min_count = min(keyword_info_map[keyword_hash]['count'] for keyword_hash in keywords_set)
        max_count = max(keyword_info_map[keyword_hash]['count'] for keyword_hash in keywords_set)

        normalized_count = nor(keyword_info['count'],min_count,max_count)


        node = {
            "name": keyword_name,
            "symbolSize": normalized_count,
            "itemStyle": {
                "color": "rgba(142, 192, 173, 0.9)"  # 节点的颜色，透明度为0.9
            },
            "label": opts.LabelOpts(
                position="top",  # 标签位置
                font_size=10  # 标签字体大小
            ),
        }
        nodes.append(node)

        # nodes = sorted(nodes, key=lambda x: -x["symbolSize"])[:50]

        keywords_list = list(keywords_set)
        for j in range(idx + 1, len(keywords_set)):
            co_occurrence_count = coOccurrence_matrix[idx, j]
            if co_occurrence_count > 0:
                edge = {
                    "source": keyword_name,
                    "target": keyword_info_map[keywords_list[j]]['keyword'],
                    "value": co_occurrence_count,
                }
                edges.append(edge)
            # 更新进度条
            progress_bar.update(1)

    # 关闭进度条
    progress_bar.close()

    return nodes, edges


def visualize_keyword_network(nodes, edges, path):
    graph = (
        Graph()
        .add(
            "",
            nodes,
            edges,
            repulsion=500,  # You can adjust this value to control node spacing
            layout="force",
            label_opts=opts.LabelOpts(is_show=True),  # Hide node labels
            is_focusnode=True,
            is_roam=True,
            is_draggable=True,
            edge_label=True
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Keyword Co-Occurrence Network"),
        )
    )
    print('1111')
    graph.render("static\\"+path +"_network.html")



def network_visu(keywords_set, keyword_info_map, coOccurrence_matrix, path):
    # keywords_set, keyword_info_map, coOccurrence_matrix = load_data()
    nodes, edges = create_keyword_network(keywords_set, keyword_info_map, coOccurrence_matrix)
    visualize_keyword_network(nodes, edges, path)

