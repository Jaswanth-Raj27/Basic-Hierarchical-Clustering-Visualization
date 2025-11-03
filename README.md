Hierarchical Clustering Visualization

This project demonstrates how hierarchical clustering works using Python. It generates random data points, groups them into clusters using the Ward linkage method, and visualizes the results with a dendrogram and a scatter plot.
Hierarchical clustering is an unsupervised learning technique that builds a tree-like structure (called a dendrogram) to show how data points are merged step by step into clusters. This approach helps in understanding the natural grouping within data.

In this project:

Random data is created using the make_blobs() function from scikit-learn.
The clustering is done using linkage() from SciPy with the "ward" method.
A dendrogram is plotted to show how points combine into clusters.
Finally, the data is divided into 3 clusters, and each cluster is displayed in a different color.

Required Libraries:
pandas
numpy
matplotlib
scipy
scikit-learn

You can install them by running:
pip install pandas numpy matplotlib scipy scikit-learn

Steps to run the program:

Save the code in a file (for example, hierarchical_clustering.py).
Open a terminal or command prompt in that folder.
Run python hierarchical_clustering.py.
You’ll first see a dendrogram showing the hierarchy, followed by a scatter plot displaying the 3 clusters in different colors.
You can modify the number of samples, centers, or the linkage method to experiment with different cluster shapes and structures.

Author: Jaswanth Raj
