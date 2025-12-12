import json

class Node:
    def __init__(self, script);
        self.script = script
        self.next_nodes = []
        self.run_time = ""

    def run(self):
        pass

    def run(self, time): #
        # wait for seconds till time then execute
        pass

    def add():

class Flow:
    def __init__(self, storage, concurrency):
        self.starting_nodes = []
        self.concurrency = concurrency
        self.load_nodes()

    def load_nodes(self):
        try:
            nodes_file = open("nodes.json")
        except FileNotFoundError:
            print("[CRITICAL] Cannot find nodes saves file!")

    def save_nodes(self):
        text = "" # change to nodes/json
        with open("nodes.json", "w") as nodes_file:
            nodes_file.write(text)

    def change_concurrency(self, new_concurrency):
        self.concurrency = new

    def on_close(self):
        self.save_nodes()

if __name__ == "__main__":
    # run Flow
    pass
