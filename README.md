NetGuard – Machine Learning-based Network Intrusion Detection System (In Progress)

NetGuard is a flow-based Network Intrusion Detection System (IDS) that leverages machine learning to detect suspicious or malicious network activity. The system is designed to provide a lightweight, easy-to-understand prototype for educational purposes and initial research in cybersecurity.

The project uses a Random Forest classifier trained on synthetic yet realistic network traffic flows, which allows it to distinguish between normal and attack flows based on 12 key network features. Each flow captures information such as connection duration, packet counts, byte counts, TCP/UDP flags, and indicators for anomalies like wrong fragments or urgent flags.

The project consists of two main modules:

Training Module (netguard_train.py) – generates synthetic flows, labels them as normal or attack, trains a Random Forest model, and saves the trained model along with the feature set.

Detection Module (netguard_detect.py) – loads the trained model, accepts network flow data, and predicts whether each flow is normal or malicious.

Key Features:

Flow-based detection with 12 descriptive features

Balanced synthetic dataset for model training

Random Forest classifier for robust prediction

Easy integration with new flows for testing

Project Status:
The project is still under active development. Future improvements will include:

Integration with real network traffic, using packet captures (.pcap) via tools like Scapy

Training on real-world datasets such as NSL-KDD or CICIDS2017 to improve detection accuracy

Visualization of detection results and model performance (confusion matrix, ROC curve, feature importance)

Potential development of a real-time monitoring dashboard for live intrusion detection

This repository is ideal for anyone looking to explore machine learning applications in network security, experiment with flow-based features, and extend the system into a full-fledged IDS.