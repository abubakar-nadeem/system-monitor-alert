# System Monitor Alert

A lightweight Python script that monitors a specific directory in real-time. When a new file is added, it instantly triggers a native desktop notification pop-up.

## 🚀 How It Works
1. **Directory Baseline:** When started, the script takes a snapshot of the files inside the target folder (`secure_folder`).
2. **Continuous Comparison:** It runs an active loop that checks the folder every 2 seconds and compares it with the previous snapshot using Python sets.
3. **Instant Desktop Alert:** If a new file name is found, it uses the `plyer` library to dispatch a real-time system notification.

## 📋 Prerequisites
This project requires the `plyer` library to handle cross-platform desktop notifications:
```bash
pip install plyer
```
