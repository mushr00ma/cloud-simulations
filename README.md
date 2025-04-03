# **Cloud Infrastructure Simulations**

## **Overview**
This repository contains various **cloud computing simulations and algorithms**, including **task scheduling, load balancing, virtualization, replication, and cloud deployment models**. The programs demonstrate fundamental cloud infrastructure concepts through Python-based simulations.

## **Contents**
### **1️⃣ Task Scheduling & Load Balancing**
- **Round-Robin Task Distribution**: Distributes `M` tasks across `N` worker nodes using round-robin scheduling.
- **Round-Robin Load Balancer**: Distributes requests across servers with a delay simulation.
- **Least Connections Load Balancer**: Assigns new tasks to the server with the fewest active connections.

### **2️⃣ Cloud Resource Management**
- **Virtualization Class**: Lists benefits/drawbacks of virtualization and suggests if it’s beneficial for a scenario.
- **Hypervisor Type Identification**: Determines if a hypervisor (e.g., VMware, KVM) is Type 1 or Type 2.
- **Virtual Server Operations**: Simulates virtual server operations (`start`, `stop`, `reboot`) using threading.

### **3️⃣ Data Replication & Networking**
- **Synchronous vs. Asynchronous Replication**: Simulates how data consistency is maintained or delayed using dictionaries.
- **Packet Transmission with Latency**: Introduces artificial network latency to simulate cloud-based app delays.

### **4️⃣ Cloud Deployment & Service Models**
- **Cloud Deployment Model Selector**: Recommends `Public`, `Private`, or `Hybrid` cloud based on security, budget, and scalability.
- **IaaS, PaaS, SaaS Simulation**: Demonstrates cloud service abstraction using classes.

### **5️⃣ Parallel Computing & Aggregation**
- **Task Aggregation Using Concurrent Futures**: Splits a large task across multiple nodes and merges results.
- **Cloud CPU Auto-Scaling**: Simulates auto-scaling when CPU usage exceeds a threshold.

## **Setup & Usage**
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Cloud-Infra-Simulations.git
   cd Cloud-Infra-Simulations
