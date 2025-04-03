'''
Simulate a simple failover system where if the primary server fails (randomly simulated), the system automatically redirects traffic to a secondary server and logs the event. 
'''

import random
import time

class Server:
    def __init__(self, name):
        self.name = name
        self.active = True
        self.failure_count = 0

    def fail(self):
        if self.active:
            self.active = False
            self.failure_count += 1
            return True
        return False

    def recover(self):
        if not self.active:
            self.active = True
            return True
        return False

class FailoverSystem:
    def __init__(self):
        self.primary = Server("Primary")
        self.secondary = Server("Secondary")
        self.log = []
        self.current_active = "primary"
        self.failover_start_time = None

    def log_event(self, message):
        timestamp = time.strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.log.append(log_entry)
        print(log_entry)

    def check_status(self):
        if not self.primary.active and self.current_active == "primary":
            self.log_event("Primary failed - Switching to Secondary")
            self.current_active = "secondary"
            self.failover_start_time = time.time()
        
        if self.primary.active and self.current_active == "secondary":
            duration = time.time() - self.failover_start_time
            self.log_event(f"Primary recovered - Reverting from Secondary (failover duration: {duration:.1f}s)")
            self.current_active = "primary"
            self.failover_start_time = None

    def simulate(self, duration=10):
        start_time = time.time()
        self.log_event("System started - Primary server active")
        
        while time.time() - start_time < duration:
            if random.random() < 0.3 and self.primary.active:
                if self.primary.fail():
                    self.log_event("Primary server failure detected")
            
            if random.random() < 0.4 and not self.primary.active:
                if self.primary.recover():
                    self.log_event("Primary server recovery detected")

            self.check_status()
            
            if self.current_active == "primary":
                self.log_event("Traffic handled by Primary")
            else:
                self.log_event("Traffic handled by Secondary")
            
            time.sleep(1.0 - ((time.time() - start_time) % 1.0))

        print("\n=== Full System Log ===")
        for entry in self.log:
            print(entry)
        
        print(f"\nTotal Primary Failures: {self.primary.failure_count}")
        if self.failover_start_time:
            print(f"Final Failover Duration: {time.time() - self.failover_start_time:.1f}s")

if __name__ == "__main__":
    system = FailoverSystem()
    system.simulate(duration=10)