import time
import random

def send_packet(packet_id):
    delay = random.uniform(0.1, 1.5)
    print(f"Sending packet {packet_id}... (Delay: {delay:.2f}s)")
    time.sleep(delay)
    print(f"Packet {packet_id} received.\n")

def simulate_network_traffic(packet_count):
    for i in range(1, packet_count + 1):
        send_packet(i)

if __name__ == "__main__":
    n = int(input("Enter number of packets to send: "))
    simulate_network_traffic(n)
