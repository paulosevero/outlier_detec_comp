# Introduction

In this repository, we present the assets for a scientific study on the comparison of performance, accuracy, power consumption, and temperature impact of several anomaly detection techniques on edge devices.

# Motivation

The popularization and low-cost of electronic devices and the rise of large-scale environments such as clouds enable the storage and analysis of a large amount of data in real time. This set of capabilities drove the emergence of the Internet of Things (IoT), which is a distributed paradigm supported at the infrastructure level by a dynamic network infrastructure with self-configuration capabilities at execution time based on interoperable communication standards.

In most cases, sensors are seen as "things" dispersed in the environment, which send data via the network that is received and analyzed in real time. There are several applications of IoT such as eHealth, agriculture, and industry 4.0.  Any of these applications can be potentially harmful if one or more sensors are compromised, and this problem becomes harder to manage as the number of sensors increases.

Thus, several investigations have been focusing on mechanisms like anomaly detection algorithms to ensure the integrity of data being pre-processed by embedded systems at the edge of the network. However, none of these studies focus on the impact caused by anomaly detection algorithms to the power consumption and temperature of these devices. Thus, in this investigation, we compare six anomaly detection algorithms regarding performance, accuracy, power consumption, and temperature.

# Anomaly Detection Techniques

### Local Outlier Factor (LOF)

### Isolation Forest (iForest)

Isolation Forest creates random trees sub-sets of data, and anomalies are isolated closer to the root, whereas normal points are separated deeper in the tree.

### Histogram-based Outlier Score (HBOS)

### One-Class Support Vector Machines (OCSVM)

### Stochastic Outlier Selection (SOS)

### Clustering-Based Local Outlier Factor (CBLOF)

# Evaluation

# Results

# Conclusion

