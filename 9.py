import random
import time

class CloudServer:
    def __init__(self, id):
        self.id = id
        self.cpu_usage = random.randint(3, 7)

    def update_load(self):
        self.cpu_usage += random.randint(-3, 5)
        self.cpu_usage = max(0, min(15, self.cpu_usage))

class CloudManager:
    def __init__(self, scale_up_threshold=15, scale_down_threshold=5, max_instances=5):
        self.servers = [CloudServer(1)]
        self.scale_up_threshold = scale_up_threshold
        self.scale_down_threshold = scale_down_threshold
        self.max_instances = max_instances

    def check_cpu_usage(self):
        while True:
            overloaded = []
            for server in self.servers:
                server.update_load()
                print(f"Server {server.id}: CPU {server.cpu_usage}%")
                if server.cpu_usage >= self.scale_up_threshold:
                    overloaded.append(server.id)

            if overloaded and len(self.servers) < self.max_instances:
                print(f"High CPU usage detected on {overloaded}. Spawning new instance...")
                self.spawn_instance()
            elif len(self.servers) == self.max_instances:
                print("Max instances reached. No more scaling up.")

            if len(self.servers) > 1 and all(s.cpu_usage <= self.scale_down_threshold for s in self.servers):
                print("All servers under 5% CPU. Removing an instance...")
                self.remove_instance()

            if len(self.servers) == self.max_instances:
                print("\nMax instances reached. Exiting.")
                exit()

            time.sleep(2)

    def spawn_instance(self):
        new_id = len(self.servers) + 1
        self.servers.append(CloudServer(new_id))
        print(f"Instance {new_id} spawned.")

    def remove_instance(self):
        removed = self.servers.pop()
        print(f"Instance {removed.id} removed.")

if __name__ == "__main__":
    manager = CloudManager()
    manager.check_cpu_usage()
