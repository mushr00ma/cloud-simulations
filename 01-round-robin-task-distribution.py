'''
Write a Python program that takes N worker nodes and distributes M tasks among them using round-robin scheduling. Simulate each node processing tasks and print results.
'''

import time
import random

class Worker:
    def __init__(self, id):
        self.id = id
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def process_tasks(self):
        for task in self.tasks:
            print(f"Worker {self.id} processing {task}...")
            time.sleep(random.uniform(0.5, 1.5))
        print(f"Worker {self.id} completed all tasks.")

class RoundRobinScheduler:
    def __init__(self, num_workers):
        self.workers = [Worker(i) for i in range(num_workers)]
        self.index = 0

    def distribute_tasks(self, tasks):
        for task in tasks:
            self.workers[self.index].add_task(task)
            self.index = (self.index + 1) % len(self.workers)

    def start_processing(self):
        for worker in self.workers:
            worker.process_tasks()

if __name__ == "__main__":
    N, M = 4, 10  
    tasks = [f"Task-{i+1}" for i in range(M)]
    
    scheduler = RoundRobinScheduler(N)
    scheduler.distribute_tasks(tasks)
    scheduler.start_processing()
