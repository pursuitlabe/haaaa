import sys
import numpy as np

sys.path.extend(['../'])
from graph import tools

num_node = 17
self_link = [(i, i) for i in range(num_node)]
inward = [(10, 8), (8, 6), (9, 7), (7, 5),  # arms
          (15, 13), (13, 11), (16, 14), (14, 12),  # legs
          (11, 5), (12, 6), (11, 12), (5, 6),  # torso
          (5, 0), (6, 0), (1, 0), (2, 0), (3, 1), (4, 2)]  # nose, eyes and ears
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward


class Graph:
    def __init__(self, labeling_mode='spatial'):
        self.num_node = num_node
        self.self_link = self_link
        self.inward = inward
        self.outward = outward
        self.neighbor = neighbor
        self.A = self.get_adjacency_matrix(labeling_mode)

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'spatial':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)
        else:
            raise ValueError()
        return A
