'''
Write a Python program that simulates CPU, memory, and network usage of cloud instances using random values. Log the metrics over time and raise alerts if thresholds are crossed. 
'''

import random
import time

class CloudInstance:
    def __init__(self, id):
        self.id = id

    def update_metrics(self):
        self.cpu_usage = random.randint(5, 100)
        self.memory_usage = random.randint(10, 100)
        self.network_usage = random.randint(1, 1000)

    def check_alerts(self):
        alerts = []
        if self.cpu_usage > 85:
            alerts.append(f"High CPU usage ({self.cpu_usage}%) on Instance {self.id}")
        if self.memory_usage > 90:
            alerts.append(f"High Memory usage ({self.memory_usage}%) on Instance {self.id}")
        if self.network_usage > 800:
            alerts.append(f"High Network usage ({self.network_usage} Mbps) on Instance {self.id}")
        return alerts

class CloudMonitor:
    def __init__(self, num_instances=3):
        self.instances = [CloudInstance(i+1) for i in range(num_instances)]

    def monitor(self, duration=15):
        start_time = time.time()
        while time.time() - start_time < duration:
            print("\n--- Cloud Instance Metrics ---")
            for instance in self.instances:
                instance.update_metrics()
                print(f"Instance {instance.id}: CPU {instance.cpu_usage}%, Memory {instance.memory_usage}%, Network {instance.network_usage} Mbps")
                alerts = instance.check_alerts()
                for alert in alerts:
                    print(alert)
            time.sleep(2)
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor = CloudMonitor(num_instances=3)
    monitor.monitor(duration=15)
