'''
Simulate synchronous and synchronous data replication using two dictionaries (source and replica). Show how data consistency is maintained or delayed based on replication type. 
'''

import time
import threading

class DataReplication:
    def __init__(self, mode):
        self.source_db = {}
        self.replica_db = {}
        self.mode = mode.lower()

    def insert(self, key, value):
        self.source_db[key] = value
        if self.mode == "synchronous":
            self.replica_db[key] = value

    def async_sync(self):
        if self.mode == "asynchronous":
            time.sleep(2) 
            self.replica_db = self.source_db.copy()

    def show_databases(self, label):
        print(f"\n{label}")
        print("Source:", self.source_db)
        print("Replica:", self.replica_db)

mode = input("Replication mode (synchronous/asynchronous): ").strip().lower()

replication = DataReplication(mode)

replication.insert("A", 100)
replication.insert("B", 200)

replication.show_databases("Before Replication")

if mode == "asynchronous":
    print("\nAsync replication in progress...")
    sync_thread = threading.Thread(target=replication.async_sync)
    sync_thread.start()
    sync_thread.join()

replication.show_databases("After Replication")
