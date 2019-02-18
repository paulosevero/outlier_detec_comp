# Introduction

In this repository, we present the assets for a scientific study on the comparison of performance, accuracy, power consumption, and temperature impact of several anomaly detection techniques on edge devices.

# Motivation

The popularization and low-cost of electronic devices and the rise of large-scale environments such as clouds enable the storage and analysis of a large amount of data in real time. This set of capabilities drove the emergence of the Internet of Things (IoT), which is a distributed paradigm supported at the infrastructure level by a dynamic network infrastructure with self-configuration capabilities at execution time based on interoperable communication standards.

In most cases, sensors are seen as "things" dispersed in the environment, which send data via the network that is received and analyzed in real time. There are several applications of IoT such as eHealth, agriculture, and industry 4.0.  Any of these applications can be potentially harmful if one or more sensors are compromised, and this problem becomes harder to manage as the number of sensors increases.

In this context, there is a discussion around mechanisms like anomaly detection algorithms to ensure the integrity of data being pre-processed by embedded systems at the edge of the network. Several investigations point to the relevance of controlling the temperature of embedded systems since it can affect not only the reliability, but also the performance, power, and cost of these devices. Besides, embedded systems are usually battery-dependent, so there is a concern in finding ways to reduce their power consumption without sacrificing performance. 

Several investigations point to the relevance of analyzing the feasibility of running anomaly detection algorithms in embedded devices to reduce the amount of data being transferred to the cloud and to minimize the response delay of these devices. However, none of these studies focus on the impact caused by anomaly detection algorithms to the power consumption and temperature of these devices. Thus, in this investigation, we compare six anomaly detection algorithms regarding performance, accuracy, power consumption, and temperature.

# Anomaly Detection Techniques

### Local Outlier Factor (LOF)

### Isolation Forest (iForest)

Isolation Forest creates random trees sub-sets of data, and anomalies are isolated closer to the root, whereas normal points are separated deeper in the tree.

### Histogram-based Outlier Score (HBOS)

### One-Class Support Vector Machines (OCSVM)

OCSVM creates a representational model of normal training data to detect outliers. It considers an outlier every instance that is too different from the built model.

### LSCP: Locally Selective Combination of Parallel Outlier Ensembles

Employs the concept of affinity to quantify the relationship from one data point to another data point. A data point is selected as an outlier when all the other data points have insufficient affinity with it. 

### Clustering-Based Local Outlier Factor (CBLOF)

### Principal Component Analysis (PCA)

# Evaluation

# Results

The results can be found here: [Google Drive](https://drive.google.com/drive/folders/1znZlmrKfY798fKJ0B9XrLu7yubk_PajU?usp=sharing)

# Conclusion

