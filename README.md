# Introduction

In this repository, we present the assets for a scientific study on the comparison of performance, accuracy, power consumption, and temperature impact of several anomaly detection techniques on edge devices.

# Motivation

The popularization and low-cost of electronic devices and the rise of large-scale environments such as clouds enable the storage and analysis of a large amount of data in real time. This set of capabilities drove the emergence of the Internet of Things (IoT), which is a distributed paradigm supported at the infrastructure level by a dynamic network infrastructure with self-configuration capabilities at execution time based on interoperable communication standards.

In most cases, sensors are seen as "things" dispersed in the environment, which send data via the network that is received and analyzed in real time. There are several applications of IoT such as eHealth, agriculture, and industry 4.0.  Any of these applications can be potentially harmful if one or more sensors are compromised, and this problem becomes harder to manage as the number of sensors increases.

In this context, there is a discussion around mechanisms like anomaly detection algorithms to ensure the integrity of data being pre-processed by embedded systems at the edge of the network. Several investigations point to the relevance of controlling the temperature of embedded systems since it can affect not only the reliability, but also the performance, power, and cost of these devices. Besides, embedded systems are usually battery-dependent, so there is a concern in finding ways to reduce their power consumption without sacrificing performance. 

Several investigations point to the relevance of analyzing the feasibility of running anomaly detection algorithms in embedded devices to reduce the amount of data being transferred to the cloud and to minimize the response delay of these devices. However, none of these studies focus on the impact caused by anomaly detection algorithms to the power consumption and temperature of these devices. Thus, in this investigation, we compare six anomaly detection algorithms regarding performance, accuracy, power consumption, and temperature.

# Anomaly Detection Techniques

### Isolation Forest

The Isolation Forest algorithm (iForest) uses random trees to detect anomalies based on the premise that after constructing isolation trees for a given dataset, anomalies are isolated closer to the root of the tree while normal points are isolated in the further nodes. The anomaly detection is composed of two stages: training and evaluation. In the training stage, a given dataset is separated into disjoint sub-sets from which isolation trees are constructed through continuous sub-sampling until either no more data is available or a cutoff value (tree height limit) is reached. The sub-sampling consists of designating points as left or right sub-trees using a randomly chosen attribute from the dataset along with a randomly picked split-point between its minimum and maximum values. In the evaluation stage, test instances are passed through the isolation trees and their anomaly scores are obtained.

### K-Nearest Neighbors

The K-Nearest Neighbors (kNN) algorithm computes for each point of a dataset the distance from it's Kth nearest neighbor. Then, it selects the top N points with the maximum distances as outliers. In order to minimize the computational cost, a clustering algorithm is used to partition in disjoin subsets the input data. Partitions that cannot contain outliers are pruned. On the remaining partitions, outliers are computed.

### Local Outlier Factor

Local Outlier Factor (LOF) applies the concept of local density to determine if a point is an outlier. The local density of a point is calculated using the distance of its k-nearest neighbors. A point is considered an outlier if by comparison it has lower density than it's neighbors.

### Cluster-Based Local Outlier Factor

FindCBLOF uses the Squeezer algorithm on a given dataset to obtain a set of clusters. Using the obtained Clusters and two numerical parameters, that are used to define a boundary, two new sets of clusters are derived: LC (Large Clusters) and SC (Small Clusters). For each record of the dataset, if the record's cluster belong to LC, the CBLOF value is calculated using the distance between the record and it's cluster, otherwise (it's cluster belong to SC) the distance is calculated using the minimal distance between the record and a Cluster belonging to LC.

### Histogram-Based Outlier Score

The Histogram-Based Outlier Score (HBOS) algorithm first creates an univariate histogram for each feature on the dataset. The histogram is created using different techniques considering the type of data that was provided (categorical or numerical). Then it normalizes the maximum height of each histogram to 1.0 which ensures an equal weight of each feature to the outlier score. Finally, the HBOS value (outlier score) of each instance of the dataset is calculated using a formula that may be interpreted as the inverse of a discrete Naive Bayes probability model.

### Angle-Based Outlier Detector

The Angle-Based Outlier Detector (ABOD) focuses in high-dimensional data, were common approaches tend to deteriorate due to the "curse of dimensionality". Contrary to popular algorithms, ABOD considers the variance of the angles between the different vectors of data objects as a property to measure if an object is an outlier. If the spectrum of observed angles for a point is broad, the point is surrounded by others and is probably located inside a cluster. Otherwise, it is believed to be outside of grouped sets of points, thus is considered an outlier. The measured distance between objects is used to normalize the results.

# Results

The results can be found here: [Google Drive](https://docs.google.com/spreadsheets/d/1PtBshYVUkUXGbmKk0uXUGOTbpasH3pdz1mF6wgll7uA/edit?usp=sharing)

# Conclusion

The advances of areas like computing and engineering drove into the advent of the Internet of Things, in which electronic devices called embedded systems such as sensors and actuators are distributed across the environment in order to collect data and help in decision-making based on events. In this context, there is a concern about ensuring the security of IoT networks since embedded systems used to collect and pre-process data usually are not physically protected against attackers. Thus, anomaly detection techniques have been used to improve the security of embedded systems and the reliability of the data being processed.

Embedded systems usually have resources constraints that may hamper the use of too expensive anomaly detection algorithms. Besides, these devices are typically battery-dependent, and high operating temperatures may impact its efficiency or even reduce its useful lifetime. Some previous investigations compare anomaly detection techniques, however to the best of our knowledge none of these studies cover the analysis of power consumption and temperature. In this sense, we present an analysis of six anomaly detection algorithms running on an embedded device, and we discuss the impact of each of these techniques regarding power consumption, temperature, precision, and performance.

The Histogram-Based Outlier Score algorithm presented the best results regarding performance and power consumption due to its lower resources requirements and its linear time complexity. On the other hand, Isolation Forest presented the highest precision due to its approach that focuses on identifying anomalies instead of profiling normal points.
