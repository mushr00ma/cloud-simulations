import threading
import time
import random

class VirtualServer:
    def __init__(self, name):
        self.name = name
        self.status = "Stopped"

    def start(self):
        if self.status == "Running":
            print(f"{self.name} is already running.")
            return
        print(f"{self.name} is starting...")
        time.sleep(random.uniform(1, 2))
        self.status = "Running"
        print(f"{self.name} is now Running.")

    def stop(self):
        if self.status == "Stopped":
            print(f"{self.name} is already stopped.")
            return
        print(f"{self.name} is stopping...")
        time.sleep(random.uniform(1, 2))
        self.status = "Stopped"
        print(f"{self.name} is now Stopped.")

    def reboot(self):
        if self.status == "Stopped":
            print(f"{self.name} is stopped. Starting before rebooting...")
            self.start()
        print(f"{self.name} is rebooting...")
        time.sleep(random.uniform(1, 2))
        print(f"{self.name} has rebooted.")

def run_operations(server, operation):
    if operation == "start":
        server.start()
    elif operation == "stop":
        server.stop()
    elif operation == "reboot":
        server.reboot()

if __name__ == "__main__":
    servers = [VirtualServer(f"Server{i+1}") for i in range(3)]
    operations = ["start", "stop", "reboot"]

    threads = []
    for i, server in enumerate(servers):
        operation = operations[i]  
        t = threading.Thread(target=run_operations, args=(server, operation))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
