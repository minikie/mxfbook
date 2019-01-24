# -*- coding: utf-8 -*-

# Import the class
import kmapper as km
from sklearn import cluster, preprocessing, manifold, decomposition

# 1 - get data
# Some sample data
from sklearn import datasets
data, labels = datasets.make_circles(n_samples=5000, noise=0.03, factor=0.1)

# Initialize
mapper = km.KeplerMapper(verbose=1)

# distance_matrix

# filtering with distance_matrix
# Fit to and transform the data -> 여기서 normalize도 함.
projected_data = mapper.fit_transform(
    data,
    projection=[0],
    scaler=preprocessing.MinMaxScaler(),
    distance_matrix=False) # X-Y axis

# projected_data에 square distance matrix 가  나올 수 있음
# 지금은 그냥 scaling만 한거...
# map에서 square dist matrix가 드가면 뭘 따로 처리하나...?

# Create dictionary called 'graph' with nodes, edges and meta-information
graph = mapper.map(projected_data, data, nr_cubes=10)

# Visualize it
mapper.visualize(graph, path_html="make_circles_keplermapper_output.html",
                 title="make_circles(n_samples=5000, noise=0.03, factor=0.3)")

# 2 -