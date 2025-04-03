import random
import time

class Server:
    def __init__(self, id):
        self.id = id
        self.connections = 0

    def add_connection(self):
        self.connections += 1

    def remove_connection(self):
        if self.connections > 0:
            self.connections -= 1

class LoadBalancer:
    def __init__(self, num_servers=2, max_connections=6):
        self.servers = [Server(i) for i in range(1, num_servers + 1)]
        self.total_connections = 0
        self.max_connections = max_connections

    def assign_task(self):
        if self.total_connections < self.max_connections:
            server = min(self.servers, key=lambda s: s.connections)
            server.add_connection()
            self.total_connections += 1
            print(f"New connection assigned to Server {server.id}\n")

    def release_task(self):
        if random.random() < 0.5 and self.total_connections > 0:
            server = random.choice(self.servers)
            if server.connections > 0:
                server.remove_connection()
                self.total_connections -= 1
                print(f"Connection closed on Server {server.id}\n")

    def display_server_loads(self):
        print("Current Connections:")
        for server in self.servers:
            print(f"Server {server.id}: {server.connections} connections")
        print("-" * 30, "\n")

    def run_simulation(self, duration=15):
        start_time = time.time()
        while time.time() - start_time < duration and self.total_connections < self.max_connections:
            self.assign_task()
            time.sleep(0.5)
            self.release_task()
            time.sleep(0.5)
            self.display_server_loads()
            time.sleep(1)

        print("\nFinal Connections:")
        for server in self.servers:
            print(f"Server {server.id}: {server.connections} connections")
        print("-" * 30)

if __name__ == "__main__":
    lb = LoadBalancer()
    lb.run_simulation(duration=15)
