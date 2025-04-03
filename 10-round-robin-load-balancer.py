import time
import itertools

class RoundRobinLoadBalancer:
    def __init__(self, servers):
        self.servers = {server: 0 for server in servers}
        self.server_cycle = itertools.cycle(self.servers.keys())

    def distribute_request(self, request_id):
        server = next(self.server_cycle)
        self.servers[server] += 1
        print(f"[Request {request_id}] → {server} | Load: {self.servers[server]}")
        time.sleep(1.5)

    def process_requests(self, num_requests):
        for i in range(1, num_requests + 1):
            self.distribute_request(i)

    def show_server_loads(self):
        print("\nFinal Server Loads:")
        for server, load in self.servers.items():
            print(f"{server}: {load} requests")

if __name__ == "__main__":
    servers = ["Server1", "Server2"]
    load_balancer = RoundRobinLoadBalancer(servers)

    load_balancer.process_requests(7)
    load_balancer.show_server_loads()
